import sqlite3
from Utilisateur import Utilisateur
from ManagerUtilisateursSQL import ManagerUtilisateursSQL
from MenuClient import MenuClient
from MenuGestion import MenuGestionnaire


class MenuConnexion:
    def run_menu(self):
        db_manager = ManagerUtilisateursSQL()
        
        print("=========================================")
        print("        BIBLIOTHEQUE - CONNEXION         ")
        print("=========================================")

        username = input("Veuillez saisir votre nom d'utilisateur : ")
        mot_de_passe = input("Veuillez saisir votre mot de passe : ")

        # username = "Chef"
        # mot_de_passe = "MDP"

        connected = False
        for utilisateur in db_manager.charger_utilisateurs():
            if utilisateur.username == username and utilisateur.mot_de_passe == mot_de_passe:
                print(f"Vous êtes bien connecté en tant que {utilisateur.prenom} {utilisateur.nom}")
                connected = True
                if utilisateur.groupe == "Client":
                    client_menu = MenuClient()
                    client_menu.run_menu(utilisateur)
                else:
                    gestionnaire_menu = MenuGestionnaire()
                    gestionnaire_menu.run_menu(utilisateur)
                break

        if not connected:
            print("Nom d'utilisateur ou mot de passe erroné, retour au menu principal.")

        db_manager.close()

