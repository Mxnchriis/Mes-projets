class Pizza:
    def __init__(self, name):
        self.name = name

    def parler(self):
        pass  # Méthode à surcharger

class PizzaMagherita(Pizza):
    def parler(self):
        return f"{self.name} dit Miaou!"

class PizzaPepperoni(Pizza):
    def parler(self):
        return f"{self.name} dit Woof!"

def Pizza_factory(type_Pizza, name):
    if type_Pizza == "PizzaPepperoni":
        return PizzaPepperoni(name)
    elif type_Pizza == "PizzaMagherita":
        return PizzaMagherita(name)
    else:
        raise ValueError("Type de Pizza inconnu")


def main():
    PizzaPepperoni = Pizza_factory("PizzaPepperoni")
    PizzaMagherita = Pizza_factory("PizzaMagherita")
    poisson = Pizza_factory("poisson", "Bubbles")

    print(PizzaPepperoni.parler())
    print(PizzaMagherita.parler())
    print(poisson.parler())


if __name__ == "__main__":
    main()