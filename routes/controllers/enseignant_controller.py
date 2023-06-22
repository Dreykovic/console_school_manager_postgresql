from modeles.table_enseignant import TableEnseignant as Enseignant
from personne_controller import PersonneController


class EnseignantController(PersonneController):
    model = Enseignant

    def __init__(
        self,
    ):
        self.afficher()
        pass

    @classmethod
    def ajouter(cls):
        # cls.model.matricule = cls.write_number('matricule')
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
    def editer(cls):
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
                cls.editer_statut()
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                printer()
                choix = input("Choisissez une option (1-7)  :       ")

    @classmethod
    def editer_statut(cls):
        value = cls.write_text("statut")
        Enseignant.update_statut(cls.write_number("matricule"), value)


t = EnseignantController()
