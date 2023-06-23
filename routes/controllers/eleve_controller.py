from .modeles.table_eleve import TableEleve as Eleve
from .modeles.table_classe import TableClasse as Classe
from .modeles.table_tuteur import TableTuteur as Tuteur
from .controller import Controller

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
        tuteur = cls.assign(Tuteur)
        classe = cls.assign(Classe)
        eff = next(element[2] for element in data if element[0] == classe)
        Classe.update("effectif", classe, eff + 1)
        print("Goal")
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
                super().update("nom",nom)
                break
            elif choix == "2":
                prenoms = cls.read("prenom")
                super().update("prenom",prenoms)
                break
            elif choix == "3":
                date = cls.read("date_naissance")
                super().update("date_naissance",date)
                break
            elif choix == "4":
                contact = cls.read("contact", True)
                super().update("contact",contact)
                break
            elif choix == "5":
                genre = cls.read("genre", False, ["M", "F"])
                super().update("genre",genre)
                break
            elif choix == "6":
                adresse = cls.read("adresse")
                super().update("adresse",adresse)
                break
            elif choix == "7":
                tuteur = cls.assign(Tuteur)
                super().update("tuteurs",tuteur)
                break
            elif choix == "8":
                classe = cls.assign(Classe)
                super().update("classe",classe)
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")

    def validate_classe(id_classe):
        pass


if __name__ =="__main__":
    t = EleveController()
