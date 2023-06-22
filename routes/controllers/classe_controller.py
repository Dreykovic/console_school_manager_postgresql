from modeles.table_classe import TableClasse as Classe
from controller import Controller


class ClasseController(Controller):
    model = Classe

    def __init__(self):
        self.create()
    @staticmethod
    def printer():
        print("1. 2nde A4")
        print("2. Znde D")
        print("3. 2nde C4")
        print("4. 1ere A4")
        print("5. 1ere D")
        print("6. 1ere C4")
        print("7. Tle A4")
        print("8. Tle D")
        print("9. Tle C4\n \n")

    @classmethod
    def create(cls):
        ClasseController.printer()
        choix = input("Choisissez une option (1-9) : pour le nom de la classe       ")
        while True:
            if choix == "1":
                nom = "2nde A4"
                break
            elif choix == "2":
                nom = "2nde D"
                break
            elif choix == "3":
                nom = "2nde C4"
                break
            elif choix == "4":
                nom = "1ere A4"
                break
            elif choix == "5":
                nom = "1ere D"
                break
            elif choix == "6":
                nom = "1ere C4"
                break
            elif choix == "7":
                nom = "Tle A4"
                break
            elif choix == "8":
                nom = "Tle D"
                break
            elif choix == "9":
                nom = "Tle C4"
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                ClasseController.printer()
                choix = input(
                    "Choisissez une option (1-9) pour le nom de la classe :       "
                )
        uneclasse = Classe(nom)
        uneclasse.create()

    @classmethod
    def update(cls):
        print("1. Editer le nom de la classe ")
        print("2. Editer l'effectif de la classe\n \n")
        choix = input("Choisissez une option (1-2)  :       ")
        while True:
            if choix == "1":
                super().update("nom",cls.MSG_INVALID_TEXT)
                break
            elif choix == "2":
                super().update("effectif", cls.MSG_INVALID_NUMBER,)
                break

            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Editer le nom de la classe ")
                print("2. Editer l'effectif de la classe\n \n")
                choix = input("Choisissez une option (1-2)  :       ")


if __name__ == "__main__":
    clazss = ClasseController()
