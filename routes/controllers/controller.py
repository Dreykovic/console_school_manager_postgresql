from modeles.table_classe import TableClasse as Classe
from validators import *
from datetime import datetime
import sys


class Controller:
    model = ""

    # def __init__(self, model):    # Constructor of the class
    #     self.model = model
    def ajouter(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Le controlleur doit implémenter la méthode")

    def editer(self):
        raise NotImplementedError("Le controlleur doit implémenter la méthode")

    # @classmethod
    # def ask_id(cls):
    #     matricule = input(f"Id de {cls.model.relation}:       ")
    #     while not validate_number(matricule):
    #         print("Saisie invalide. Veuillez saisir un text valide.")
    #         matricule = input(f"Id de {cls.model.relation}:       ")
    #     matricule = int(matricule)
    #     return matricule

    @classmethod
    def supprimer(cls):
        cls.model.delete(cls.ask_id())

    @classmethod
    def write_text(cls, name):
        text = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_text(text):
            print("Saisie invalide. Veuillez saisir un text valide.")
            text = input(f"Ecrire {name} de {cls.model.relation} :       ")
        return text

    @classmethod
    def write_number(cls, name):
        number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_number(number):
            print("Saisie invalide. Veuillez saisir un number valide.")
            number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        return int(number)

    @classmethod
    def write_date(cls, name):
        date = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_date(date):
            print("Saisie invalide. Veuillez saisir un date valide.")
            date = input(f"Ecrire {name} de {cls.model.relation} :       ")
        data = date.split("-")
        annee = int(data[0])
        mois = int(data[1])
        jour = int(data[2])
        return datetime(annee, mois, jour).date()

    @staticmethod
    def write_gender():
        print("1. Homme")
        print("2. Femme")
        choix = input("Choisissez une option (1-2) : pour le genre       ")
        while True:
            if choix == "1":
                gender = "M"
                break
            elif choix == "2":
                gender = "F"
                break
            else:
                print("Choix invalide. Veuillez sélectionner une option valide.")
                print("Homme")
                print("Femme")
                choix = input("Choisissez une option (1-9) pour le genre :       ")
        return gender

    @classmethod
    def write_phone_number(cls, name):
        phone_number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        while not validate_phone_number(phone_number):
            print("Saisie invalide. Veuillez saisir un phone_number valide.")
            phone_number = input(f"Ecrire {name} de {cls.model.relation} :       ")
        return int(phone_number)

    @classmethod
    def show_all(cls):
        data = cls.model.select_all()
        table_name = cls.model.relation.capitalize()

        if len(data) == 0:
            print(f"Rien de '{table_name}' enregistré")
            return

        columns = cls.model.get_columns()
        print(columns)
        column_widths = [12] * len(columns)

        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(
            f"{'Liste des ' + table_name + 's':^{sum(column_widths) + 3 * len(columns) + 1}}"
        )
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))

        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)

        for elt in data:
            row_format = " | ".join(
                ["{{:<{}}}".format(width) for width in column_widths]
            )
            print(row_format.format(*elt))

    @staticmethod
    def show_attr_of(model, colonnes):
        attributs = ", ".join(colonnes)
        data = model.select_attr(attributs)
        table_name = model.relation.capitalize()
        print(data)
        if len(data) == 0:
            print(f"Rien de '{table_name}' enregistré")
            return

        columns = colonnes
        column_widths = [12] * len(columns)

        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(
            f"{'Liste des ' + table_name + 's':^{sum(column_widths) + 3 * len(columns) + 1}}"
        )
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))

        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)

        for elt in data:
            row_format = " | ".join(
                ["{{:<{}}}".format(width) for width in column_widths]
            )
            print(row_format.format(*elt))
        return data

    @staticmethod
    def show_attr_where_id(model, colonnes, matricule, alldata):
        ids = [t[0] for t in alldata]
        while matricule not in ids:
            print(f"l'id  ne correspond a aucun {model.relation}, Veuillez réessayer")
            return 0
        data = tuple(filter(lambda x: x[0] == matricule, [t for t in alldata]))[0]
        table_name = model.relation.capitalize()

        columns = colonnes
        column_widths = [12] * len(columns)

        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(f"{table_name:^{sum(column_widths) + 3 * len(columns) + 1}}")
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))

        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)

        row_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        print(row_format.format(*data))
        return 1


if __name__ == "__main__":
    print(dir())
