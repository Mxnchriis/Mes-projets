class BurgerBuilder:
    def __init__(self, name):
        self.name = name

    def ajouter_pain(self):
        print("J'ajoute du pain !")

    def ajouter_sauce(self):
        print("J'ajoute de la sauce !")

    def ajouter_legumes(self):
        print("J'ajoute des légumes !")

class VeggieBurgerBuilder(BurgerBuilder):
    def ajouter_viande_vegan(self):
        print("J'ajoute de la viande vegan !")

class MeatBurgerBuilder(BurgerBuilder):
    def ajouter_viande(self):
        print("J'ajoute de la viande !")

def BurgerBuilder_factory(type_BurgerBuilder, name):
    if type_BurgerBuilder == "MeatBurgerBuilder":
        burger = MeatBurgerBuilder(name)
        burger.ajouter_pain()
        burger.ajouter_sauce()
        burger.ajouter_legumes()
        burger.ajouter_viande()
        return burger
    elif type_BurgerBuilder == "VeggieBurgerBuilder":
        burger = VeggieBurgerBuilder(name)
        burger.ajouter_pain()
        burger.ajouter_sauce()
        burger.ajouter_legumes()
        burger.ajouter_viande_vegan()
        return burger
    else:
        raise ValueError("Type de BurgerBuilder inconnu")


def main():
    print("Création d'un burger viande :")
    BurgerBuilder_factory("MeatBurgerBuilder", "Burger Viande")
    print("\nCréation d'un burger vegan :")
    BurgerBuilder_factory("VeggieBurgerBuilder", "Burger Vegan")


if __name__ == "__main__":
    main()