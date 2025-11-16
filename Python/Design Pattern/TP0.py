# Dans un premier temps, on peut constater que le code est mal structuré, il serait préférable de faire des fonctions pour chaque tâche.

# En cas d'ajout d'un 3ème type d'utilisateur, il faudrait rajouter une condition else if, ce qui n'est pas très propre.

print("Bienvenue dans l'application de messagerie")

type_utilisateur = input("Type d'utilisateur (admin/utilisateur) : ")

if type_utilisateur == "admin":
    print("Connexion en tant qu'administrateur")
    print("Création du panneau de contrôle")
    print("Envoi d'une alerte à tous les utilisateurs")
elif type_utilisateur == "utilisateur":
    print("Connexion en tant qu'utilisateur standard")
    print("Chargement de la boîte de réception")
    print("Affichage des messages")
else:
    print("Type d'utilisateur inconnu")

