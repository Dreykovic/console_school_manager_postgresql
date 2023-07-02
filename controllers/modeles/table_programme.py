from .table import Table
from .schema_builder import *


class TableProgramme(Table):
    """Classe représentant la table 'programme' dans la base de données."""

    relation = "programme"
    schema = [
        PrimaryKey("id_programme").build(),
        Integer("coeficient").not_null().build(),
        Integer("matiere").foreign_key().references("matiere", "id_matiere").build(),
        Integer("prof").foreign_key().references("enseignant", "matricule").build(),
        Integer("classe").foreign_key().references("classe", "id_classe").build(),
    ]
    primary_key = "id_programme"

    def __init__(self, coeficient, matiere, prof, classe):
        """Initialise une instance de la classe TableProgramme.

        Args:
            coeficient (int): Coefficient du programme.
            matiere (int): Clé étrangère de la matière associée au programme.
            prof (int): Clé étrangère de l'enseignant associé au programme.
            classe (int): Clé étrangère de la classe associée au programme.
        """
        self.id_programme = 0
        self.coeficient = coeficient
        self.matiere = matiere
        self.prof = prof
        self.classe = classe
