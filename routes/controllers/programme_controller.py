from modeles.table_enseignant import TableEnseignant as Enseignant
from modeles.table_classe import TableClasse as Classe
from modeles.table_matiere import TableMatiere as Matiere
from modeles.table_programme import TableProgramme as Programme
from controller import Controller


class ProgrammeController(Controller):
    model = Programme

    def __init__(
        self,
    ):
        self.create()

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
        print("1. Editer le nom de l'eleve ")
        print("2. Editer le prenom de l'eleve")
        print("3. Editer la date de naissance de l'eleve ")
        print("4. Editer le contact de l'eleve")
        print("5. Modifier le genre de l'eleve")
        print("6. Editer l'adresse de l'eleve")
        print("7. Changer le tueur de l'eleve")
        print("8. Changer la classe de l'eleve\n \n")
        choix = input("Choisissez une option (1-8)  :       ")
        while True:
            if choix == "1":
                nom = cls.read("nom")
                super().update(nom)
                break
            elif choix == "2":
                prenoms = cls.read("prenom")
                super().update(prenoms)
                break
            elif choix == "3":
                date = cls.read("date_naissance")
                super().update(date)
                break
            elif choix == "4":
                contact = cls.read("contact", True)
                super().update(contact)
                break
            elif choix == "5":
                genre = cls.read("genre", False, ["M", "F"])
                super().update(genre)
                break
            elif choix == "6":
                adresse = cls.read("adresse")
                super().update(adresse)
                break
            elif choix == "7":
                tuteur = cls.read("tuteur")
                super().update(tuteur)
                break
            elif choix == "8":
                classe = cls.read("classe")
                super().update(classe)
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")


t = EleveController()
