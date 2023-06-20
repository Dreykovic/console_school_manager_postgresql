from modeles.table_eleve import TableEleve as Eleve
from modeles.table_classe import TableClasse as Classe
from modeles.table_tuteur import TableTuteur as Tuteur
from personne_controller import PersonneController


class EleveController(PersonneController):
    model = Eleve

    def __init__(
        self,
    ):
        self.ajouter()

    @classmethod
    def ajouter(cls):
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
        value = cls.write_text("profession")
        Tuteur.update_profession(cls.write_number("matricule"), value)

    def validate_classe(id_classe):
        pass

    @classmethod
    def assigner_classe(cls):
        data = cls.show_attr_of(Classe, ["id_classe", "nom", "effectif"])
        ids = [t[0] for t in data]
        classe = cls.write_number("id classe ")
        while classe not in ids:
            print(f"l'id {classe} ne correspond a aucune classe")
            classe = cls.write_number("id classe ")
        eff = list(filter(lambda x: x == classe, [t[2] for t in data]))
        eff = eff[0] + 1
        Classe.update_effectif(classe, eff)
        return classe

    @classmethod
    def assigner_tuteur(cls):
        data = cls.show_attr_of(
            Tuteur, ["matricule", "nom", "prenoms", "profession", "contact"]
        )
        ids = [t[0] for t in data]
        tuteur = cls.write_number("id tuteur ")
        while tuteur not in ids:
            print(f"l'id {tuteur} ne correspond a aucun tuteur. veuillez réessayer")
            tuteur = cls.write_number("id tuteur ")
        return tuteur


t = EleveController()





