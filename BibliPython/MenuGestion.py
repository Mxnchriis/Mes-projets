import uuid
import mysql.connector
from ManagerLivresSQL import ManagerLivresSQL
from ManagerUtilisateursSQL import ManagerUtilisateursSQL
from Livre import Livre

class MenuGestionnaire:
    def run_menu(self, manager_livres):
        self.manager_livres = ManagerLivresSQL()
        self.manager_user = ManagerUtilisateursSQL()
        while True:
            print("=========================================")
            print("    BIBLIOTHEQUE - MENU GESTION          ")
            print("=========================================")
            print("1 - Ajouter un livre")
            print("2 - Voir tous les livres")
            print("3 - Modifier un livre")
            print("4 - Supprimer un livre")
            print("5 - Voir tout les utilisateurs")
            print("6 - Modifier un utilisateur")
            print("7 - Se déconnecter")

            choice = int(input("Choisissez une option : "))

            if choice == 1:
                MenuAjoutLivre.run_menu(self)
            elif choice == 2:
                self.manager_livres.listLivres = self.manager_livres.charger_livres()
                print("LISTE DES LIVRES :")
                for livre in self.manager_livres.listLivres:
                    # print(livre)
                    disponible = "Disponible" if livre.disponibilite else "Non disponible"
                    emprunteur = "Personne" if livre.emprunteur == None else livre.emprunteur
                    print(f"{livre.id} - {livre.nom} - {livre.auteur} - {disponible} - {emprunteur}")

            elif choice == 3:
                # print("La fonctionnalité est en cours de développement")
                EditLivre = MenuEditLivre()
                EditLivre.run_menu()

            elif choice == 4:
                DeleteLivre = MenuDeleteLivre()
                DeleteLivre.run_menu()

            elif choice == 5:
                self.manager_user.listUser = self.manager_user.charger_utilisateurs()
                print("LISTE DES UTILISATEURS :")
                for user in self.manager_user.listUser:
                    print(str(user.id) + " - " + user.username + " - " + user.mot_de_passe + " - " + user.nom + " - " + user.prenom + " - " + user.groupe)


            elif choice == 6:
                EditUser = MenuEditUser()
                EditUser.run_menu()
        
            elif choice == 7:
                break


class MenuAjoutLivre:
    def run_menu(self):
        db_manager = ManagerLivresSQL()
        livre = Livre(
            id=str(uuid.uuid4()),
            nom="",
            auteur="",
            disponibilite=True,
            emprunteur=None
        )
        
        print("=========================================")
        print("     BIBLIOTHEQUE - AJOUTER LIVRE        ")
        print("=========================================")

        livre.nom = input("Veuillez saisir votre nom du livre : ")
        livre.auteur = input("Veuillez saisir l'auteur : ")

        db_manager.ajouter_livre(livre)

        print("Le livre a bien été ajouté à la bibliothèque.")
        db_manager.close()


class MenuEditLivre:
    def run_menu(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='First-In-Slot972',
            database='bibli'
        )
        self.cursor = self.conn.cursor()
        self.manager_livres = ManagerLivresSQL()
        print("=========================================")
        print("    MODIF LIVRE - MENU GESTION           ")
        print("=========================================")

        print("VOICI TOUT LES LIVRES DISPONIBLES ACTUELLEMENT :")
        for livre in self.manager_livres.listLivres:
            print(str(livre.id) + " - " + livre.nom + " - " + livre.auteur)

        livre_id = input("Veuillez saisir l'id du livre à modifier : ")
        modif_realise = False

        for livre in self.manager_livres.listLivres:
            if livre.disponibilite and livre.id == int(livre_id):
                livre.nom = input("Veuillez saisir votre nom du livre : ")
                livre.auteur = input("Veuillez saisir l'auteur : ")
                modif_realise = True
                requete = "UPDATE livres SET nom = %s, auteur = %s WHERE id = %s"
                valeurs = (livre.nom, livre.auteur, livre_id)
                self.cursor.execute(requete, valeurs)
                self.conn.commit()
                print(f"Vous avez bien modifié le livre n°{livre.id}")

                self.cursor.close()
                self.conn.close()
                break

        if not modif_realise:
            print("Vous n'avez pas saisi d'id de livre valide, retour au menu précédent.")

class MenuDeleteLivre:
    def run_menu(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='First-In-Slot972',
            database='bibli'
        )
        self.cursor = self.conn.cursor()
        self.manager_livres = ManagerLivresSQL()
        print("=========================================")
        print("    SUPPR LIVRE - MENU GESTION           ")
        print("=========================================")

        print("LISTE DES LIVRES:")
        for livre in self.manager_livres.listLivres:
            print(str(livre.id) + " - " + livre.nom + " - " + livre.auteur)

        livre_id = input("Veuillez saisir l'id du livre à supprimer : ")
        supprime_realise = False

        for livre in self.manager_livres.listLivres:
            if livre.disponibilite and livre.id == int(livre_id):
                supprime_realise = True
                print(f"Vous avez bien supprimé {livre.nom}")
                requete = "DELETE FROM livres WHERE id = %s"
                valeurs = (livre.id,)
                self.cursor.execute(requete, valeurs)
                self.conn.commit()

                self.cursor.close()
                self.conn.close()
                break

        if not supprime_realise:
            print("Vous n'avez pas saisi d'id de livre valide, retour au menu précédent.")
            

class MenuEditUser:
    def run_menu(self):
        self.conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='First-In-Slot972',
            database='bibli'
        )
        self.cursor = self.conn.cursor()
        self.manager_user = ManagerUtilisateursSQL()
        self.manager_user.listUser = self.manager_user.charger_utilisateurs()
        print("=========================================")
        print("    MODIF UTILISATEUR - MENU GESTION     ")
        print("=========================================")

        print("VOICI TOUT LES UTILISATEURS :")
        for user in self.manager_user.listUser:
            print(str(user.id) + " - " + user.username + " - " + user.mot_de_passe + " - " + user.nom + " - " + user.prenom + " - " + user.groupe)

        user_id = input("Veuillez saisir l'id de l'utilisateur à modifier : ")
        modif_realise = False

        for user in self.manager_user.listUser:
            if user.id == int(user_id):
                user.username = input("Veuillez saisir le nouveau nom d'utilisateur : ")
                user.mot_de_passe = input("Veuillez saisir le nouveau mot de passe : ")
                user.nom = input("Veuillez saisir le nouveau nom : ")
                user.prenom = input("Veuillez saisir le nouveau prénom : ")

                groupe = input("Veuillez saisir le nouveau groupe (Client ou Gestionnaire) : ")
                user.groupe = groupe if groupe in ["Client", "Gestionnaire"] else "Client"
                
                modif_realise = True
                requete = """
                    UPDATE utilisateurs 
                    SET username = %s, mot_de_passe = %s, prenom = %s, nom = %s, groupe = %s 
                    WHERE id = %s
                """
                valeurs = (user.username, user.mot_de_passe, user.prenom, user.nom, user.groupe, user_id)
                self.cursor.execute(requete, valeurs)
                self.conn.commit()
                print("L'utilisateur" + str(user.id)  + "a été modifié avec succès.")

                self.cursor.close()
                self.conn.close()
                break

        if not modif_realise:
            print("Vous n'avez pas saisi d'id valide, retour au menu précédent.")