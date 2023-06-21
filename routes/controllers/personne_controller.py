from controller import Controller
import sys


class PersonneController(Controller):
    @classmethod
    def editer(cls, attribut):
        data = cls.show(cls.model)
        if attribut in ["nom", "prenoms", "adresse"]:
            value = cls.write_text(f"nouveau {attribut}")
        elif attribut == "profession":
            value = cls.write_text(attribut)
        elif attribut == "genre":
            value = Controller.write_gender("correct")
        elif attribut == "contact":
            value = cls.write_phone_number(f"nouveau {attribut}")
        elif attribut == "date_naissance":
            attr = [
                "Matricule",
                "Nom",
                "Prenoms",
                "Adresse",
                "Contact",
                "Date de naissance",
            ]
            data = cls.show(cls.model)
            value = cls.write_date(" nouvelle date de naissance")
        else:
            return 0

        matricule = cls.write_number("matricule")
        print("")
        print("")
        print(
            f"Etes vous sur de vouloir mettre à jour les donnée de {cls.model.relation}  :"
        )
        while not cls.show_where_id(cls.model, matricule, data):
            matricule = cls.write_number("matricule")
            print(
                f"Etes vous sur de vouloir mettre à jour les donnée de {cls.model.relation}  :"
            )

        print("?")
        print("")
        print("")
        print("1. Oui")
        print("2. Non")
        choix = input("Choisissez une option (1-2) :       ")
        while True:
            if choix == "1":
                cls.model.update(attribut, matricule, value)
                break
            elif choix == "2":
                sys.exit(0)
                return 0
            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Oui")
                print("2. Non")
                choix = input("Choisissez une option (1-2) :       ")
