class Livre:
    def __init__(self, id, nom, auteur, disponibilite=True, emprunteur=None):
        self.id = id
        self.nom = nom
        self.auteur = auteur
        self.disponibilite = disponibilite
        self.emprunteur = emprunteur
