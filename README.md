# Système de Gestion de Bibliothèque Universitaire

## Description du Projet
Ce projet a été réalisé dans le cadre de l'évaluation du second semestre de Licence 2 Réseaux Informatiques à l'ISI Dakar. Il implémente une application de gestion de bibliothèque universitaire en appliquant les concepts de la Programmation Orientée Objet (POO) en Python, une persistance hybride (JSON pour le catalogue et SQLite pour les adhérents), ainsi qu'une gestion rigoureuse des exceptions et de la journalisation (Logs).

## 🛠️ Fonctionnalités Implémentées
- **Architecture POO** : Classe abstraite `DocumentBase` et héritage pour les classes filles `Livre`, `Revue`, `DVD`, et `Memoire`.
- **Calcul d'amendes** : Implémentation polymorphique de la méthode `calculer_amende()` selon le type de document (200 FCFA/jour pour Livre, 100 FCFA pour Revue, 500 FCFA pour DVD, 1000 FCFA pour Mémoire).
- **Persistance des données** : Sauvegarde et chargement automatique du catalogue au format JSON. Persistance des adhérents dans une base SQLite.
- **Robustesse** : Gestion des erreurs utilisateurs avec levée d'exceptions personnalisées.
- **Journalisation (Logs)** : Traçabilité complète de l'application consignée dans `logs/app.log`.

##  Installation et Exécution

1. **Cloner le projet** :
   ```bash
   git clone https://github.com
   cd projet_bibliotheque
   ```

2. **Lancer l'application** :
   ```bash
   python -m src.app
   ```
