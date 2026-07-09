import sqlite3

DB_PATH = "database/bibliotheque.db"

def initialiser_base_de_donnees():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS adherents (
            identifiant TEXT PRIMARY KEY,
            nom TEXT NOT NULL,
            categorie TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emprunts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            adherent_id TEXT,
            document_ref TEXT NOT NULL,
            date_emprunt TEXT NOT NULL,
            date_retour_prevue TEXT NOT NULL,
            date_retour_effective TEXT,
            FOREIGN KEY(adherent_id) REFERENCES adherents(identifiant)
        )
    ''')
    conn.commit()
    conn.close()

def enregistrer_adherent(identifiant: str, nom: str, categorie: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO adherents (identifiant, nom, categorie) VALUES (?, ?, ?)",
            (identifiant, nom, categorie)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()