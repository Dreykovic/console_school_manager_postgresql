from .table import Table
from .schema_builder import *


class TableProgramme(Table):
    relation = "programme"
    schema = [
        PrimaryKey("id_programme").build(),
        Integer("coeficient").not_null().build(),
        Integer("matiere").foreign_key().references("matiere", "id_matiere").build(),
        Integer("prof").foreign_key().references("enseignant", "matricule").build(),
        Integer("classe").foreign_key().references("classe", "id_classe").build(),
    ]
    primary_key = "id_programme"

    def __init__(self,coeficient, matiere, prof, classe):
        self.id_programme = 0
        self.coeficient = coeficient
        self.matiere = matiere
        self.prof = prof
        self.classe = classe
