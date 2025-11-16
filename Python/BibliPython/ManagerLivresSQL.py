import mysql.connector
from Livre import Livre


class ManagerLivresSQL:
    def __init__(self, db_name="bibli"):
        # Connexion à la base de données MySQL
        self.connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',          # Remplacez par votre nom d'utilisateur MySQL
            password='First-In-Slot972',           # Remplacez par votre mot de passe MySQL
            database=db_name       # Nom de la base de données MySQL
        )
        self.cursor = self.connection.cursor()
        self.create_table()
        self.listLivres = self.charger_livres()

    def create_table(self):
        # Création de la table 'livres' si elle n'existe pas encore
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS livres (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255) NOT NULL,
                auteur VARCHAR(255) NOT NULL,
                disponibilite BOOLEAN NOT NULL,
                emprunteur VARCHAR(255)
            )
        ''')
        self.connection.commit()

    def charger_livres(self):
        # Chargement de tous les livres depuis la base de données MySQL
        self.listLivres = []
        self.cursor.execute('SELECT id, nom, auteur, disponibilite, emprunteur FROM livres')
        rows = self.cursor.fetchall()
        return [Livre(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    def sauvegarder_livres(self, livre):
        # Sauvegarder les livres dans la base de données
        self.cursor.execute('''
            INSERT INTO livres (nom, auteur, disponibilite, emprunteur) 
            VALUES (%s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE nom=%s, auteur=%s, disponibilite=%s, emprunteur=%s
        ''', (
            livre.nom, livre.auteur, livre.disponibilite, livre.emprunteur,
            livre.nom, livre.auteur, livre.disponibilite, livre.emprunteur
        ))
        self.connection.commit()

    def ajouter_livre(self, livre):
        # Ajouter un livre à la liste et sauvegarder dans la base de données
        self.listLivres.append(livre)
        self.sauvegarder_livres(livre)

    def close(self):
        # Fermer la connexion MySQL proprement
        self.cursor.close()
        self.connection.close()
