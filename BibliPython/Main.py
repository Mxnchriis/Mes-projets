from MenuAccueil import MenuAccueil
from ManagerUtilisateursSQL import ManagerUtilisateursSQL
from ManagerLivresSQL import ManagerLivresSQL

class Main:
    @staticmethod
    def main():
        # manager_livres = ManagerLivresSQL()
        # manager_utilisateurs = ManagerUtilisateursSQL()

        # manager_livres.charger_livres()
        # manager_utilisateurs.charger_utilisateurs()

        accueil = MenuAccueil()
        accueil.run_menu()
        
        # manager_utilisateurs.sauvegarder_utilisateur()
        # manager_livres.sauvegarder_livres()

        # manager_livres.close()
        # manager_utilisateurs.close()


if __name__ == "__main__":
    Main.main()
