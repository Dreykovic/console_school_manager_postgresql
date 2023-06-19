from modeles.table_tuteur import TableTuteur as Tuteur
from controller import Controller


class TuteurController(Controller):
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
        date_naissance = self.write_date("date_naissance")
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
                editerEffectif()
                break
            elif choix == "4":
                editerEffectif()
                break
            elif choix == "5":
                editerEffectif()
                break
            elif choix == "6":
                editerEffectif()
                break
            elif choix == "7":
                editerEffectif()
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")

    def editer_nom(self):
        value = self.write_text("nom")
        Tuteur.update_nom(self.write_number("matricule"), value)
    
    def editer_prenom(self):
        value = self.write_text("prenom")
        Tuteur.update_prenoms(self.write_number("matricule"), value)


t = TuteurController()
