import uuid
from Utilisateur import Utilisateur
from ManagerUtilisateursSQL import ManagerUtilisateursSQL

class MenuInscription:
    def run_menu(self):
        manager_utilisateurs = ManagerUtilisateursSQL()
        utilisateur = Utilisateur(
            id=str(uuid.uuid4()),
            username="",
            mot_de_passe="",
            prenom="",
            nom="",
            groupe=""
        )

        print("=========================================")
        print("     BIBLIOTHÈQUE - CRÉER COMPTE         ")
        print("=========================================")

        utilisateur.username = input("Veuillez saisir votre nom d'utilisateur : ")
        utilisateur.mot_de_passe = input("Veuillez saisir votre mot de passe : ")
        utilisateur.nom = input("Veuillez saisir votre nom : ")
        utilisateur.prenom = input("Veuillez saisir votre prénom : ")

        groupe = input("Veuillez saisir votre groupe (Client ou Gestionnaire) : ")
        utilisateur.groupe = groupe if groupe in ["Client", "Gestionnaire"] else "Client"

        manager_utilisateurs.sauvegarder_utilisateur(utilisateur)
        print("Utilisateur a bien été créé.")
