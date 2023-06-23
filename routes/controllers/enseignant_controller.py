from modeles.table_enseignant import TableEnseignant as Enseignant
from controller import Controller


class EnseignantController(Controller):
    model = Enseignant

    def __init__(
        self,
    ):
        self.afficher()
        pass

    @classmethod
    def create(cls):
        nom = cls.read("nom")
        prenoms = cls.read("prenoms")
        date_naissance = cls.read("date_naissance")
        contact = cls.read("contact", True)
        genre = cls.read("genre", False, ["M", "F"])
        adresse = cls.read("adresse")
        statut = cls.read("statut")
        prof = Enseignant(nom, prenoms, date_naissance, contact, genre, adresse, statut)
        prof.create()

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
                statut = cls.read("statut")
                super().update("statut",statut)
                break

            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")


if __name__ == "__main__":
    t = EnseignantController()
