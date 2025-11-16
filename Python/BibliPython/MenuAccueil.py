from MenuInscription import MenuInscription
from MenuConnexion import MenuConnexion

class MenuAccueil:
    def run_menu(self):
        choice = 0
        while choice == 0:
            print("=========================================")
            print("        BIBLIOTHÈQUE - ACCUEIL           ")
            print("=========================================")
            print("1 - Se connecter")
            print("2 - Créer un compte")
            print("3 - Quitter")

            try:
                choice = int(input())
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                choice = 0
                continue

            if choice not in [1, 2, 3]:
                choice = 0

            if choice == 1:
                connexion = MenuConnexion()
                connexion.run_menu()
                choice = 0
            elif choice == 2:
                inscription = MenuInscription()
                inscription.run_menu()
                choice = 0
            elif choice == 3:
                break
