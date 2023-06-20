from modeles.table_tuteur import TableTuteur as Tuteur
from personne_controller import PersonneController


class TuteurController(PersonneController):
    model = Tuteur

    def __init__(
        self,
    ):
        self.editer()

    @classmethod
    def ajouter(cls):
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
    def editer(cls):
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
                cls.editer_nom()
                break
            elif choix == "2":
                cls.editer_prenom()
                break
            elif choix == "3":
                cls.editer_date_naissance()
                break
            elif choix == "4":
                cls.editer_contact()
                break
            elif choix == "5":
                cls.editer_genre()
                break
            elif choix == "6":
                cls.editer_adresse()
                break
            elif choix == "7":
                cls.editer_profession()
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")


    @classmethod
    def editer_profession(cls):
        attr = ["matricule", "nom","prenoms","adresse","profession"]
        data = cls.show_attr_of(Tuteur, attr)
        matricule = cls.write_number("matricule")
        print("Etes vous sur de vouloir mettre à jour les donnée du tuteur  :")
        while not cls.show_attr_where_id(Tuteur, attr, matricule, data):
                matricule = cls.write_number("matricule")
        print("?")
        Tuteur.update_profession(matricule, cls.write_text("profession"))

if __name__ == "__main__":
    t = TuteurController()
