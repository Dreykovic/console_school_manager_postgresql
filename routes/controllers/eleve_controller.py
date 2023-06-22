from modeles.table_eleve import TableEleve as Eleve
from modeles.table_classe import TableClasse as Classe
from modeles.table_tuteur import TableTuteur as Tuteur
from controller import Controller

class EleveController(Controller):
    model = Eleve

    def __init__(
        self,
    ):
        self.create()

    @classmethod
    def create(cls):
        nom = cls.read("nom")
        prenoms = cls.read("prenoms")
        date_naissance = cls.read("date_naissance")
        contact = cls.read("contact", True)
        genre = cls.read("genre", False, ["M", "F"])
        adresse = cls.read("adresse")
        tuteur = cls.assigner_tuteur()
        classe = cls.assigner_classe()

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

        Classe.update("effectif", classe, eff + 1)
        return classe

    @classmethod
    def assigner_tuteur(cls):
        data = cls.show(Tuteur)
        ids = [t[0] for t in data]
        tuteur = cls.write_number("id tuteur ")
        while tuteur not in ids:
            print(f"l'id {tuteur} ne correspond a aucun tuteur. veuillez réessayer")
            tuteur = cls.write_number("id tuteur ")
        return tuteur


t = EleveController()
