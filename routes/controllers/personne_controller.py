from controller import Controller
import sys


class PersonneController(Controller):
    
    @classmethod
    def editer(cls, attribut, *args):
        data = cls.show(cls.model)
        matricule = cls.write_number("matricule")
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
        message = f"Etes vous sur de vouloir mettre à jour les donnée de {cls.model.relation}  :"

        choix = cls.action_confirm(message, matricule, data)
        while True:
            if choix == "1":
                cls.model.update(attribut, matricule, value)
                break
            elif choix == "2":
                return 0
            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Oui")
                print("2. Non")
                choix = input("Choisissez une option (1-2) :       ")
















    # @classmethod
    # def editer(cls, attribut, *args):
    #     data = cls.show(cls.model)
    #     matricule = cls.write_number("matricule")
    #     if attribut in ["nom", "prenoms", "adresse"]:
    #         value = cls.write_text(f"nouveau {attribut}")
    #     elif attribut == "profession":
    #         value = cls.write_text(attribut)
    #     elif attribut == "genre":
    #         value = Controller.write_gender("correct")
    #     elif attribut == "contact":
    #         value = cls.write_phone_number(f"nouveau {attribut}")
    #     elif attribut == "date_naissance":
    #         attr = [
    #             "Matricule",
    #             "Nom",
    #             "Prenoms",
    #             "Adresse",
    #             "Contact",
    #             "Date de naissance",
    #         ]
    #         data = cls.show(cls.model)
    #         value = cls.write_date(" nouvelle date de naissance")
    #     else:
    #         return 0
    #     message = f"Etes vous sur de vouloir mettre à jour les donnée de {cls.model.relation}  :"

    #     choix = cls.action_confirm(message, matricule, data)
    #     while True:
    #         if choix == "1":
    #             cls.model.update(attribut, matricule, value)
    #             break
    #         elif choix == "2":
    #             return 0
    #         else:
    #             print(cls.MSG_INVALID_OPTION)
    #             print("1. Oui")
    #             print("2. Non")
    #             choix = input("Choisissez une option (1-2) :       ")
