from .modeles.table_classe import TableClasse as Classe
from .controller import Controller


class ClasseController(Controller):
    model = Classe
    avalible_names = [
        "2nde A4",
        "2nde D",
        "2nde C4",
        "1ere A4",
        "1ere D",
        "1ere C4",
        "Tle A4",
        "Tle D",
        "Tle C4",
    ]

    def __init__(self):
        self.show(Classe)

    @classmethod
    def create(cls):
        nom = cls.read("nom", False, cls.avalible_names)
        uneclasse = Classe(nom)
        uneclasse.create()

    @classmethod
    def update(cls):
        print("1. Editer le nom de la classe ")
        print("2. Editer l'effectif de la classe\n \n")
        choix = input("Choisissez une option (1-2)  :       ")
        while True:
            if choix == "1":
                nom = cls.read("nom")
                super().update("nom", nom)
                break
            elif choix == "2":
                eff = cls.read("effectif")
                super().update("effectif", eff)
                break

            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Editer le nom de la classe ")
                print("2. Editer l'effectif de la classe\n \n")
                choix = input("Choisissez une option (1-2)  :       ")


if __name__ == "__main__":
    clazss = ClasseController()
