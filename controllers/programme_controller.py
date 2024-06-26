import os
import sys
sys.path.append(f'{os.getcwd}/modeles' )
from modeles.table_enseignant import TableEnseignant as Enseignant
from modeles.table_classe import TableClasse as Classe
from modeles.table_matiere import TableMatiere as Matiere
from modeles.table_programme import TableProgramme as Programme
from controllers.controller import Controller


class ProgrammeController(Controller):
    model = Programme

    def __init__(
        self,
    ):
        self.update()

    @classmethod
    def create(cls):
        matiere = cls.assign(Matiere)[0]
        print("CHOISIR COEFICIENT")
        coef = cls.read("coeficient", False, ["1", "2", "3", "4", "5"])
        classe = cls.assign(Classe)[0]
        prof = cls.assign(Enseignant)[0]
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
                matiere = cls.assign(Matiere)[0]
                super().update("matiere", matiere)
                break
            elif choix == "3":
                classe = cls.assign(Classe)[0]
                super().update("classe", classe)
                break
            elif choix == "4":
                prof = cls.assign(Enseignant)[0]
                super().update("prof", prof)
                break

            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-4)  :       ")


if __name__ == "__main__":
    pr = ProgrammeController()
