from datetime import date
from typing import List, Optional
from src.enums import CategorieAdherent
from src.models.document import DocumentBase

class Emprunt:
    """Relation de composition : Un adhérent possède ses propres objets Emprunt."""
    def __init__(self, document: DocumentBase, date_emprunt: date, date_retour_prevue: date):
        self.document = document
        self.date_emprunt = date_emprunt
        self.date_retour_prevue = date_retour_prevue
        self.date_retour_effective: Optional[date] = None

class Adherent:
    def __init__(self, nom: str, identifiant: str, categorie: CategorieAdherent):
        self.nom = nom
        self.identifiant = identifiant
        self.categorie = categorie
        # Relation d'agrégation : L'adhérent contient une liste d'emprunts
        self.emprunts: List[Emprunt] = []

    def ajouter_emprunt(self, emprunt: Emprunt):
        self.emprunts.append(emprunt)
