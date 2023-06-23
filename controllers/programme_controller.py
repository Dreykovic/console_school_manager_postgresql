from .modeles.table_enseignant import TableEnseignant as Enseignant
from .modeles.table_classe import TableClasse as Classe
from .modeles.table_matiere import TableMatiere as Matiere
from .modeles.table_programme import TableProgramme as Programme
from .controller import Controller


class ProgrammeController(Controller):
    model = Programme

    def __init__(
        self,
    ):
        self.update()

    @classmethod
    def create(cls):
        coef = cls.read("coeficient", False, ["1", "2", "3", "4", "5"])
        matiere = cls.assign(Matiere)
        classe = cls.assign(Classe)
        prof = cls.assign(Enseignant)
        programme = Programme(coef, matiere, prof, classe)
        programme.create()

    @classmethod
    def update(cls):
        print("1. Editer le coeficient du programme ")
        print("2. Changer la matiere assigner au programme")
        print("3. Changer la classe assignée au programme ")
        print("4. Changer le professeur assigné au proramme")

        choix = input("Choisissez une option (1-4)  :       ")
        while True:
            if choix == "1":
                coef = cls.read("coeficient", False, ["1", "2", "3", "4", "5"])
                super().update("coeficient", coef)
                break
            elif choix == "2":
                matiere = cls.assign(Matiere)
                super().update("matiere", matiere)
                break
            elif choix == "3":
                classe = cls.assign(Classe)
                super().update("classe", classe)
                break
            elif choix == "4":
                prof = cls.assign(Enseignant)
                super().update("prof", prof)
                break

            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-4)  :       ")


if __name__ == "__main__":
    pr = ProgrammeController()
