from modeles.table_eleve import TableEleve as Eleve
from modeles.table_classe import TableClasse as Classe
from modeles.table_tuteur import TableTuteur as Tuteur
from personne_controller import PersonneController


class EleveController(PersonneController):
    model = Eleve

    def __init__(
        self,
    ):
        self.update()

    @classmethod
    def create(cls):
        tuteur = cls.assigner_tuteur()
        classe = cls.assigner_classe()
        nom = cls.write_text("nom")
        prenoms = cls.write_text("prenoms")
        date_naissance = cls.write_date("date de naissance")
        contact = cls.write_phone_number("contact")
        genre = cls.write_gender()
        adresse = cls.write_text("adresse")

        eleve = Eleve(
            tuteur, classe, nom, prenoms, date_naissance, contact, genre, adresse
        )
        eleve.create()

    @classmethod
    def update(cls):
        print("1. Editer le nom de l'eleve ")
        print("2. Editer le prenom de l'eleve")
        print("3. Editer la date de naissance de l'eleve ")
        print("4. Editer le contact de l'eleve")
        print("5. Editer le genre de l'eleve")
        print("6. Editer l'adresse de l'eleve")
        print("7. Editer la profession de l'eleve\n \n")
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
                super().update("tuteur", cls.MSG_INVALID_TEXT)
                break
            elif choix == "7":
                super().update("classe", cls.MSG_INVALID_TEXT)
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")



    def validate_classe(id_classe):
        pass

    @classmethod
    def assigner_classe(cls):
        data = cls.show(Classe)
        ids = [t[0] for t in data]
        classe = cls.write_number("id classe ")
        while classe not in ids:
            print(f"l'id {classe} ne correspond a aucune classe")
            classe = cls.write_number("id classe ")
        for element in data:
            if element[0] == classe:
                eff = element[2]
    
        print("0000000000000000000000000000000000000000000000000000")
        Classe.update("effectif",classe, eff+1)
        return classe

    @classmethod
    def assigner_tuteur(cls):
        data = cls.show(
            Tuteur
        )
        ids = [t[0] for t in data]
        tuteur = cls.write_number("id tuteur ")
        while tuteur not in ids:
            print(f"l'id {tuteur} ne correspond a aucun tuteur. veuillez réessayer")
            tuteur = cls.write_number("id tuteur ")
        return tuteur


t = EleveController()
