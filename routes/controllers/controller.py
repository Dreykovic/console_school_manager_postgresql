from modeles.table_classe import TableClasse as Classe
from validators import *
from datetime import datetime


class Controller:
    model = ""

    # def __init__(self, model):    # Constructor of the class
    #     self.model = model
    def ajouter(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Le controlleur doit implémenter la méthode")

    def editer(self):
        raise NotImplementedError("Le controlleur doit implémenter la méthode")

    @classmethod
    def ask_id(cls):
        matricule = input(f"Id de {cls.model.relation}:       ")
        while not validate_number(matricule):
            print("Saisie invalide. Veuillez saisir un text valide.")
            matricule = input(f"Id de {cls.model.relation}:       ")
        matricule = int(matricule)
        return matricule

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
    def afficher(cls):
        data = cls.model.select_all()
        table_name = cls.model.relation.capitalize()

        if len(data) == 0:
            print(f"Rien de '{table_name}' enregistré")
            return

        columns = cls.model.get_columns()  # Obtient les noms des colonnes de la table
        print(columns)
        column_widths = [12] * len(
            columns
        )  # Largeur fixe de chaque colonne (20 caractères)

        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(
            f"{'Liste des ' + table_name + 's':^{sum(column_widths) + 3 * len(columns) + 1}}"
        )
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        # Affichage des en-têtes des colonnes
        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))

        # Affichage des séparateurs horizontaux
        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)

        # Affichage des lignes de données
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

        # columns = ["matricule","nom", "prenom", "profession", "contact"]
        # # Obtient les noms des colonnes de la table
        columns = colonnes
        column_widths = [12] * len(
            columns
        )  # Largeur fixe de chaque colonne (20 caractères)

        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(
            f"{'Liste des ' + table_name + 's':^{sum(column_widths) + 3 * len(columns) + 1}}"
        )
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        # Affichage des en-têtes des colonnes
        header_format = " | ".join(
            ["{{:<{}}}".format(width) for width in column_widths]
        )
        print(header_format.format(*columns))

        # Affichage des séparateurs horizontaux
        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)

        # Affichage des lignes de données
        for elt in data:
            row_format = " | ".join(
                ["{{:<{}}}".format(width) for width in column_widths]
            )
            print(row_format.format(*elt))
        # return  [t[0] for t in data]
        return data
