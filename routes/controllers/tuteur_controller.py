from modeles.table_tuteur import TableTuteur as Tuteur
from personne_controller import PersonneController


class TuteurController(PersonneController):
    model = Tuteur

    def __init__(
        self,
    ):
        self.create()

    @classmethod
    def create(cls):
        nom = cls.write_text("nom")
        prenoms = cls.write_text("prenoms")
        date_naissance = cls.write_date("date de naissance")
        contact = cls.write_phone_number("contact")
        genre = cls.write_gender()
        adresse = cls.write_text("adresse")
        profession = cls.write_text("profession")
        tuteur = Tuteur(
            nom, prenoms, date_naissance, contact, genre, adresse, profession
        )
        tuteur.create()

    @classmethod
    def update(cls):
        print("1. Editer le nom du tuteur ")
        print("2. Editer le prenom du tuteur")
        print("3. Editer la date de naissance du tuteur ")
        print("4. Editer le contact du tuteur")
        print("5. Editer le genre du tuteur")
        print("6. Editer l'adresse du tuteur")
        print("7. Editer la profession du tuteur\n \n")
        choix = input("Choisissez une option (1-7)  :       ")
        while True:
            if choix == "1":
                super().update("nom", cls.MSG_INVALID_TEXT)
                break
            elif choix == "2":
                super().update("prenoms", cls.MSG_INVALID_TEXT)
                break
            elif choix == "3":
                super().update("date_naissance", cls.MSG_INVALID_DATE)
                break
            elif choix == "4":
                super().update("contact", cls.MSG_INVALID_NUMBER, None, "contact")
                break
            elif choix == "5":
                super().update("genre", cls.MSG_INVALID_OPTION, ["M", "F"])
                break
            elif choix == "6":
                super().update("adresse", cls.MSG_INVALID_TEXT)
                break
            elif choix == "7":
                super().update("profession", cls.MSG_INVALID_TEXT)
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")


if __name__ == "__main__":
    t = TuteurController()
