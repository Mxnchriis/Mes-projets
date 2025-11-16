import mysql.connector
from Utilisateur import Utilisateur

class ManagerUtilisateursSQL:
    def __init__(self):
        # Connexion à la base de données MySQL
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',          # Remplacez par votre nom d'utilisateur MySQL
            password='First-In-Slot972',           # Remplacez par votre mot de passe MySQL
            database='bibli'       # Nom de la base de données MySQL
        )
        self.cursor = self.conn.cursor()
        self.listUser = self.charger_utilisateurs()

    def sauvegarder_utilisateur(self, utilisateur):
        try:
            # Prépare la requête SQL d'insertion
            self.cursor.execute('''
                INSERT INTO utilisateurs (username, mot_de_passe, nom, prenom, groupe)
                VALUES (%s, %s, %s, %s, %s)
            ''', (utilisateur.username, utilisateur.mot_de_passe, utilisateur.nom, utilisateur.prenom, utilisateur.groupe))
            
            # Confirme l'insertion dans la base de données
            self.conn.commit()
            print("Utilisateur ajouté avec succès.")
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'insertion dans la base MySQL : {e}")

    def charger_utilisateurs(self):
        self.listUser = []
        try:
            # Récupère tous les utilisateurs depuis la table
            self.cursor.execute("SELECT * FROM utilisateurs")
            rows = self.cursor.fetchall()

            # Création d'une liste d'objets Utilisateur à partir des données récupérées
            return [Utilisateur(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
        except mysql.connector.Error as e:
            print(f"Erreur lors du chargement des utilisateurs : {e}")
            return []

    def close(self):
        # Fermer la connexion MySQL proprement
        self.cursor.close()
        self.conn.close()
