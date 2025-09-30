class Utilisateur:
    def connection(self):
        print("Connection en tant qu'utilisateur")

class Administrateur(Utilisateur):
    def connection(self):
        print(f"Connexion en tant qu'Administrateur")
        print("Admin : Création du panneau de contrôle")
        print("Admin : Envoi d'une alerte à tous les utilisateurs")

class UtilisateurStandard(Utilisateur):
    def connection(self):
        print(f"Connexion en tant qu'Utilisateur standard")
        print("Utilisateur standard : Chargement de la boîte de réception")
        print("Utilisateur standard : Affichage des messages")

def utilisateur_factory(type_utilisateur):
    if type_utilisateur == "admin":
        return Administrateur()
    elif type_utilisateur == "utilisateur":
        return UtilisateurStandard()
    else:
        raise ValueError("Type d'utilisateur inconnu")
    
def main():
    print("Bienvenue dans l'application de messagerie")

    type_utilisateur = input("Type d'utilisateur (admin/utilisateur) : ").strip().lower()
    utilisateur_factory(type_utilisateur).connection()

if __name__ == "__main__":
    main()

