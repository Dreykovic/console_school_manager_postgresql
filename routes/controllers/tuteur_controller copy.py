from modeles.table_tuteur import TableTuteur as Tuteur
from personne_controller import PersonneController

class TuteurController(PersonneController):
    model = Tuteur

    def __init__(
        self,
    ):
        self.editer()
        pass

    @classmethod
    def ajouter(self):
        # cls.model.matricule = cls.write_number('matricule')
        nom = self.write_text("nom")
        prenoms = self.write_text("prenoms")
        date_naissance = self.write_date("date de naissance")
        contact = self.write_phone_number("contact")
        genre = Controller.write_gender()
        adresse = self.write_text("adresse")
        profession = self.write_text("profession")
        tuteur = Tuteur(
            nom, prenoms, date_naissance, contact, genre, adresse, profession
        )
        tuteur.create()

    def editer(self):
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
                self.editer_nom()
                break
            elif choix == "2":
                self.editer_prenom()
                break
            elif choix == "3":
                self.editer_date_naissance()
                break
            elif choix == "4":
                self.editer_contact()
                break
            elif choix == "5":
                self.editer_genre()
                break
            elif choix == "6":
                self.editer_adresse()
                break
            elif choix == "7":
                self.editer_profession()
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")


    def editer_profession(self):
        value = self.write_text("profession")
        Tuteur.update_profession(self.write_number("matricule"), value)


t = TuteurController()
