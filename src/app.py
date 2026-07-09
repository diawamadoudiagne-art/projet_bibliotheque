import logging
import sys
from src.enums import StatutDocument, CategorieAdherent
from src.models.document import Livre, Revue, DVD, Memoire
from src.repository.json_storage import sauvegarder_catalogue_json, charger_catalogue_json
from src.repository.db_manager import initialiser_base_de_donnees, enregistrer_adherent

# Configuration du système de Logs (Exigence du prof)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

def afficher_menu():
    print("\n========================================")
    print("  GESTION DE BIBLIOTHÈQUE UNIVERSITAIRE ")
    print("========================================")
    print("1. Ajouter un document au catalogue")
    print("2. Afficher le catalogue (JSON)")
    print("3. Enregistrer un nouvel adhérent")
    print("4. Simuler un emprunt de document")
    print("5. Calculer une amende de retard")
    print("6. Quitter l'application")
    print("========================================")

def executer_application():
    logging.info("Démarrage de l'application de la bibliothèque.")
    initialiser_base_de_donnees()
    catalogue = charger_catalogue_json()
    
    while True:
        afficher_menu()
        choix = input("Veuillez choisir une option (1-6) : ").strip()
        
        try:
            if choix == "1":
                print("\n--- AJOUT D'UN DOCUMENT ---")
                type_doc = input("Type (Livre / Revue / DVD / Memoire) : ").strip()
                titre = input("Titre du document : ").strip()
                ref = input("Référence unique : ").strip()
                
                if not titre or not ref:
                    raise ValueError("Le titre et la référence ne peuvent pas être vides.")
                
                if type_doc.lower() == "livre":
                    auteur = input("Auteur : ").strip()
                    doc = Livre(titre, ref, auteur)
                elif type_doc.lower() == "revue":
                    numero = int(input("Numéro de la revue : "))
                    doc = Revue(titre, ref, numero)
                elif type_doc.lower() == "dvd":
                    realisateur = input("Réalisateur : ").strip()
                    doc = DVD(titre, ref, realisateur)
                elif type_doc.lower() == "memoire":
                    etudiant = input("Nom de l'étudiant : ").strip()
                    doc = Memoire(titre, ref, etudiant)
                else:
                    print("❌ Type de document inconnu.")
                    continue
                    
                catalogue.append(doc)
                sauvegarder_catalogue_json(catalogue)
                print(f"✅ {type_doc} ajouté avec succès au catalogue JSON.")
                logging.info(f"Document ajouté : {titre} (Ref: {ref})")

            elif choix == "2":
                print("\n--- CATALOGUE DES DOCUMENTS ---")
                if not catalogue:
                    print("Le catalogue est actuellement vide.")
                for doc in catalogue:
                    print(f"[{doc.__class__.__name__}] Ref: {doc.reference} | Titre: {doc.titre} | Statut: {doc.statut.value}")

            elif choix == "3":
                print("\n--- ENREGISTRER UN ADHÉRENT ---")
                nom = input("Nom complet : ").strip()
                identifiant = input("Identifiant unique : ").strip()
                print("Catégories : ETUDIANT, ENSEIGNANT, EXTERNE")
                cat_input = input("Catégorie : ").strip().upper()
                
                if cat_input not in [c.value for c in CategorieAdherent]:
                    raise ValueError("Catégorie d'adhérent invalide.")
                
                enregistrer_adherent(identifiant, nom, cat_input)
                print(f"✅ Adhérent {nom} enregistré avec succès en base SQLite.")
                logging.info(f"Nouvel adhérent créé : {nom} ({identifiant})")

            elif choix == "4":
                print("\n--- SIMULATION D'EMPRUNT ---")
                ref = input("Référence du document à emprunter : ").strip()
                document_trouve = next((d for d in catalogue if d.reference == ref), None)
                
                if not document_trouve:
                    print("❌ Document introuvable dans le catalogue.")
                    continue
                if document_trouve.statut != StatutDocument.DISPONIBLE:
                    print(f"❌ Ce document n'est pas disponible (Statut actuel : {document_trouve.statut.value}).")
                    continue
                
                document_trouve.statut = StatutDocument.EMPRUNTE
                sauvegarder_catalogue_json(catalogue)
                print(f"✅ Le document '{document_trouve.titre}' a changé de statut : EMPRUNTE.")
                logging.info(f"Emprunt simulé pour le document Ref: {ref}")

            elif choix == "5":
                print("\n--- CALCUL DE L'AMENDE DE RETARD ---")
                ref = input("Référence du document concerné : ").strip()
                document_trouve = next((d for d in catalogue if d.reference == ref), None)
                
                if not document_trouve:
                    print("❌ Document introuvable dans le catalogue.")
                    continue
                    
                jours = int(input("Nombre de jours de retard : "))
                amende = document_trouve.calculer_amende(jours)
                print(f"💰 Le montant de l'amende pour ce {document_trouve.__class__.__name__} est de : {amende} FCFA.")

            elif choix == "6":
                print("Fermeture de l'application. Au revoir !")
                logging.info("Fermeture normale de l'application.")
                sys.exit(0)
                
            else:
                print("❌ Choix invalide, veuillez entrer un nombre entre 1 et 6.")
                
        except ValueError as ve:
            print(f"⚠️ Erreur de saisie : {ve}")
            logging.error(f"Erreur de saisie utilisateur : {ve}")
        except Exception as e:
            print(f"💥 Une erreur inattendue est survenue : {e}")
            logging.error(f"Erreur critique : {e}")

if __name__ == "__main__":
    executer_application()
