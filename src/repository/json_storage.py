import json
import os
from typing import List
from src.enums import StatutDocument
from src.models.document import DocumentBase, Livre, Revue, DVD, Memoire

FICHIER_JSON = "config/catalogue.json"

def sauvegarder_catalogue_json(documents: List[DocumentBase]):
    data = []
    for doc in documents:
        doc_data = {
            "type": doc.__class__.__name__,
            "titre": doc.titre,
            "reference": doc.reference,
            "statut": doc.statut.value
        }
        if isinstance(doc, Livre):
            doc_data["auteur"] = doc.auteur
        elif isinstance(doc, Revue):
            doc_data["numero"] = doc.numero
        elif isinstance(doc, DVD):
            doc_data["realisateur"] = doc.realisateur
        elif isinstance(doc, Memoire):
            doc_data["etudiant"] = doc.etudiant
        data.append(doc_data)
        
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def charger_catalogue_json() -> List[DocumentBase]:
    if not os.path.exists(FICHIER_JSON):
        return []
    with open(FICHIER_JSON, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []
            
    documents = []
    for item in data:
        statut = StatutDocument(item["statut"])
        if item["type"] == "Livre":
            doc = Livre(item["titre"], item["reference"], item["auteur"], statut)
        elif item["type"] == "Revue":
            doc = Revue(item["titre"], item["reference"], item["numero"], statut)
        elif item["type"] == "DVD":
            doc = DVD(item["titre"], item["reference"], item["realisateur"], statut)
        elif item["type"] == "Memoire":
            doc = Memoire(item["titre"], item["reference"], item["etudiant"], statut)
        documents.append(doc)
    return documents