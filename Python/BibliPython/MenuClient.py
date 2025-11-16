import mysql.connector
from ManagerLivresSQL import ManagerLivresSQL
from ManagerUtilisateursSQL import ManagerUtilisateursSQL
from Livre import Livre

class MenuClient:
    def run_menu(self, utilisateur):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='First-In-Slot972',
            database='bibli'
        )
        self.cursor = self.conn.cursor()

        while True:
            print("=========================================")
            print("    BIBLIOTHÈQUE - MENU CLIENT           ")
            print("=========================================")
            print("1 - Voir tous les livres")
            print("2 - Emprunter un livre")
            print("3 - Rendre un livre")
            print("4 - Se déconnecter")

            try:
                choice = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                continue

            if choice == 1:
                print("LISTE DES LIVRES :")
                self.cursor.execute("SELECT nom, auteur, disponibilite FROM livres")
                livres = self.cursor.fetchall()
                for livre in livres:
                    disponible = "Disponible" if livre[2] else "Non disponible"
                    print(f"{livre[0]} - {livre[1]} - {disponible}")

            elif choice == 2:
                emprunt = MenuEmprunt()
                emprunt.run_menu(utilisateur)

            elif choice == 3:
                rendu = MenuRendu()
                rendu.run_menu(utilisateur)

            elif choice == 4:
                break

        self.conn.close()  # Fermeture de la connexion à la base de données


class MenuRendu:
    def run_menu(self, utilisateur):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='First-In-Slot972',
            database='bibli'
        )
        # print("test " + utilisateur.prenom)
        self.cursor = self.conn.cursor()
        self.manager_livres = ManagerLivresSQL()
        for livre in self.manager_livres.listLivres:
            if livre.emprunteur == utilisateur.prenom:
                livre.emprunteur = None
                livre.disponibilite = True
                requete = """
                    UPDATE livres
                    SET disponibilite = %s, emprunteur = %s 
                    WHERE id = %s
                """
                valeurs = (True, None, livre.id)
                self.cursor.execute(requete, valeurs)
                self.conn.commit()
                print(f"Vous avez rendu {livre.nom}, merci !")
                # self.manager_livres.charger_livres()

        self.cursor.close()
        self.conn.close()

class MenuEmprunt:
    def run_menu(self, utilisateur):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='First-In-Slot972',
            database='bibli'
        )
        self.cursor = self.conn.cursor()
        self.manager_livres = ManagerLivresSQL()
        print("=========================================")
        print("    BIBLIOTHEQUE - MENU CLIENT           ")
        print("=========================================")

        print("VOICI TOUT LES LIVRES DISPONIBLES ACTUELLEMENT :")
        for livre in self.manager_livres.listLivres:
            if livre.disponibilite:
                print(str(livre.id) + " - " + livre.nom + " - " + livre.auteur)

        livre_id = input("Veuillez saisir l'id du livre à emprunter : ")
        emprunt_realise = False

        for livre in self.manager_livres.listLivres:
            if livre.disponibilite and livre.id == int(livre_id):
                livre.emprunteur = utilisateur.prenom
                livre.disponibilite = False
                print(f"Vous avez bien emprunté {livre.nom}")
                emprunt_realise = True
                requete = """
                    UPDATE livres 
                    SET disponibilite = %s, emprunteur = %s 
                    WHERE id = %s
                """
                valeurs = (False, livre.emprunteur, livre.id)
                self.cursor.execute(requete, valeurs)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()
                break

        if not emprunt_realise:
            print("Vous n'avez pas saisi de nom de livre valide, retour au menu précédent.")
        # else :
        #     requete = "UPDATE livres SET disponibilite = %s, emprunteur = %s WHERE id = %s"
        #     valeurs = (livre.disponibilite, livre.emprunteur, livre.id)
        #     self.cursor.execute(requete, valeurs)
        #     self.conn.commit()

        # self.cursor.close()
        # self.conn.close()
