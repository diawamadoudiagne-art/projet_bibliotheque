from enum import Enum

class StatutDocument(Enum):
    DISPONIBLE = "DISPONIBLE"
    EMPRUNTE = "EMPRUNTE"
    RESERVE = "RESERVE"
    PERDU = "PERDU"

class CategorieAdherent(Enum):
    ETUDIANT = "ETUDIANT"
    ENSEIGNANT = "ENSEIGNANT"
    EXTERNE = "EXTERNE"
