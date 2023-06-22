from modeles.table_tuteur import TableTuteur as Tuteur
from controller import Controller


class TuteurController(Controller):
    model = Tuteur

    def __init__(
        self,
    ):
        self.update()

    @classmethod
    def create(cls):
        nom = cls.read("nom")
        prenoms = cls.read("prenoms")
        date_naissance = cls.read("date_naissance")
        contact = cls.read("contact", True)
        genre = cls.read("genre", False, ["M", "F"])
        adresse = cls.read("adresse")
        profession = cls.read("profession")
        tuteur = Tuteur(
            nom, prenoms, date_naissance, contact, genre, adresse, profession
        )
        tuteur.create()

    @classmethod
    def update(cls):
        print("1. Editer le nom de l'enseignant ")
        print("2. Editer le prenom de l'enseignant")
        print("3. Editer la date de naissance de l'enseignant ")
        print("4. Editer le contact de l'enseignant")
        print("5. Editer le genre de l'enseignant")
        print("6. Editer l'adresse de l'enseignant")
        print("7. Editer le statut de l'enseignant\n \n")
        choix = input("Choisissez une option (1-7)  :       ")
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
                profession = cls.read("profession")
                super().update(profession)
                break

            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")


if __name__ == "__main__":
    t = TuteurController()
