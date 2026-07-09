from abc import ABC, abstractmethod
from src.enums import StatutDocument

class DocumentBase(ABC):
    """Classe abstraite représentant la base d'un document de la bibliothèque."""
    
    def __init__(self, titre: str, reference: str, statut: StatutDocument = StatutDocument.DISPONIBLE):
        self.titre = titre
        self.reference = reference
        self.statut = statut

    @abstractmethod
    def calculer_amende(self, jours_retard: int) -> float:
        """Méthode abstraite imposant le calcul de l'amende selon le type de document."""
        pass

class Livre(DocumentBase):
    def __init__(self, titre: str, reference: str, auteur: str, statut: StatutDocument = StatutDocument.DISPONIBLE):
        super().__init__(titre, reference, statut)
        self.auteur = auteur

    def calculer_amende(self, jours_retard: int) -> float:
        # 200 FCFA par jour de retard pour un livre
        return max(0.0, jours_retard * 200.0)

class Revue(DocumentBase):
    def __init__(self, titre: str, reference: str, numero: int, statut: StatutDocument = StatutDocument.DISPONIBLE):
        super().__init__(titre, reference, statut)
        self.numero = numero

    def calculer_amende(self, jours_retard: int) -> float:
        # 100 FCFA par jour de retard pour une revue
        return max(0.0, jours_retard * 100.0)

class DVD(DocumentBase):
    def __init__(self, titre: str, reference: str, realisateur: str, statut: StatutDocument = StatutDocument.DISPONIBLE):
        super().__init__(titre, reference, statut)
        self.realisateur = realisateur

    def calculer_amende(self, jours_retard: int) -> float:
        # 500 FCFA par jour de retard pour un DVD
        return max(0.0, jours_retard * 500.0)

class Memoire(DocumentBase):
    def __init__(self, titre: str, reference: str, etudiant: str, statut: StatutDocument = StatutDocument.DISPONIBLE):
        super().__init__(titre, reference, statut)
        self.etudiant = etudiant

    def calculer_amende(self, jours_retard: int) -> float:
        # Amende forte pour un mémoire : 1000 FCFA par jour de retard
        return max(0.0, jours_retard * 1000.0)
