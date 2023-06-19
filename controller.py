from modeles.table_classe import TableClasse as Classe
from controller.validators import *


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
    def afficher(cls):
        classes = cls.model.select_all()
        table_name = cls.model.relation.capitalize()

        if len(classes) == 0:
            print(f"Rien de '{table_name}' enregistré")
            return

        columns = cls.model.get_columns()  # Obtient les noms des colonnes de la table
        column_widths = [20] * len(columns)  # Largeur fixe de chaque colonne (20 caractères)

        print("=" * (sum(column_widths) + 3 * len(columns) + 1))
        print(f"{'Liste des ' + table_name + 's':^{sum(column_widths) + 3 * len(columns) + 1}}")
        print("=" * (sum(column_widths) + 3 * len(columns) + 1))

        # Affichage des en-têtes des colonnes
        header_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        print(header_format.format(*columns))

        # Affichage des séparateurs horizontaux
        separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
        print(separator)

        # Affichage des lignes de données
        for classe in classes:
            row_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
            print(row_format.format(*classe))


ajouter()
afficher()
