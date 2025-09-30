class Animal:
    def __init__(self, name):
        self.name = name

    def parler(self):
        pass  # Méthode à surcharger


class Chien(Animal):
    def parler(self):
        return f"{self.name} dit Woof!"


class Chat(Animal):
    def parler(self):
        return f"{self.name} dit Miaou!"


class Poisson(Animal):
    def parler(self):
        return f"{self.name} dit Bloup!"


def animal_factory(type_animal, name):
    if type_animal == "chien":
        return Chien(name)
    elif type_animal == "chat":
        return Chat(name)
    elif type_animal == "poisson":
        return Poisson(name)
    else:
        raise ValueError("Type d'animal inconnu")


def main():
    chien = animal_factory("chien", "Rex")
    chat = animal_factory("chat", "Mimi")
    poisson = animal_factory("poisson", "Bubbles")

    print(chien.parler())
    print(chat.parler())
    print(poisson.parler())


if __name__ == "__main__":
    main()