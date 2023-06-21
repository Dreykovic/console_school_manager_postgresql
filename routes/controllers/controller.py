from modeles.table_classe import TableClasse as Classe
from validators import *
from datetime import datetime
import sys


class Controller:
    model = object()
    MSG_INVALID_TEXT = "Saisie invalide. Veuillez saisir un text valide."
    MSG_INVALID_NUMBER = "Saisie invalide. Veuillez saisir un number valide."
    MSG_INVALID_DATE = "Saisie invalide. Veuillez saisir une date valide."
    MSG_INVALID_OPTION = "Choix invalide. Veuillez sélectionner une option valide."

    def create(self):
        raise NotImplementedError("Le controlleur doit implémenter la méthode")

    def update(self):
        raise NotImplementedError("Le controlleur doit implémenter la méthode")

    @classmethod
    def destroy(cls):
        message = (
            f"Etes vous sur de vouloir supprimer les donnée de {cls.model.relation}  :"
        )
        data = cls.show(cls.model)
        matricule = cls.write_number("matricule")
        print("")
        print("")
        print(message)
        while not cls.show_where_id(cls.model, matricule, data):
            matricule = cls.write_number("matricule")
            print(message)

        print("?")
        print("")
        print("")
        print("1. Oui")
        print("2. Non")
        choix = input("Choisissez une option (1-2) :       ")
        while True:
            if choix == "1":
                cls.model.delete(matricule)
                break
            elif choix == "2":
                sys.exit(0)
                return 0
            else:
                print(cls.MSG_INVALID_OPTION)
                print("1. Oui")
                print("2. Non")
                choix = input("Choisissez une option (1-2) :       ")

    @classmethod
    def write_text(cls, name):
        text = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_text(text):
            print(cls.MSG_INVALID_TEXT)
            text = input(f"Ecrire {name} de {cls.model.relation} :       ")
        return text

    @classmethod
    def write_number(cls, name):
        number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_number(number):
            print(cls.MSG_INVALID_NUMBER)
            number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        return int(number)

    @classmethod
    def write_date(cls, name):
        date = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_date(date):
            print(cls.MSG_INVALID_DATE)
            date = input(f"Ecrire {name} de {cls.model.relation} :       ")
        data = date.split("-")
        annee = int(data[0])
        mois = int(data[1])
        jour = int(data[2])
        return datetime(annee, mois, jour).date()

    @staticmethod
    def write_gender(correct=""):
        print("1. Homme")
        print("2. Femme")
        choix = input(f"Choisissez une option (1-2) : pour le genre {correct}    ")
        while True:
            if choix == "1":
                gender = "M"
                break
            elif choix == "2":
                gender = "F"
                break
            else:
                print(cls.MSG_INVALID_OPTION)
                print("Homme")
                print("Femme")
                choix = input("Choisissez une option (1-9) pour le genre :       ")
        return gender

    @classmethod
    def write_phone_number(cls, name):
        phone_number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_phone_number(phone_number):
            print(cls.MSG_INVALID_NUMBER)
            phone_number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        return int(phone_number)

    @staticmethod
    def show(model):
        data = model.select_all()
        table_name = model.relation.capitalize()

        if len(data) == 0:
            print(f"Rien de '{table_name}' enregistré")
            return

        columns = model.get_columns()
        column_widths = [14] * len(columns)

        Controller.print_head(columns, column_widths, table_name)

        datetime_string_format = "%b %d %Y"
        uneListe = []
        for elt in data:
            tuplet = tuple()
            for value in elt:
                if type(value) == type(datetime(2000, 1, 1).date()):
                    value = datetime.strftime(value, datetime_string_format)
                tuplet += (value,)
            elt = tuplet
            uneListe.append(elt)
            row_format = " | ".join(
                ["{{:<{}}}".format(width) for width in column_widths]
            )
            print(row_format.format(*elt))
        data = uneListe
        return data

    @staticmethod
    def show_where_id(model, matricule, alldata):
        ids = [t[0] for t in alldata]
        while matricule not in ids:
            print(f"l'id  ne correspond a aucun {model.relation}, Veuillez réessayer")
            return 0
        data = tuple(filter(lambda x: x[0] == matricule, [t for t in alldata]))[0]
        table_name = model.relation.capitalize()

        columns = model.get_columns()
        column_widths = [12] * len(columns)

        Controller.print_head(columns, column_widths, table_name)

        row_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        print(row_format.format(*data))
        return 1

    def print_head(columns, column_widths, table_name):
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(f"{table_name:^{sum(column_widths) + 3 * len(columns) + 1}}")
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))

        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)


if __name__ == "__main__":
    print(dir())
