from .table import Table
from .schema_builder import *


class TableMatiere(Table):
    relation = "matiere"
    schema = [
        PrimaryKey('id_matiere').build(),
        String('libelle').not_null().unique().build()
    ]

    primary_key = "id_matiere"

    def __init__(
        self,
        libelle=None,
    ):
        self.id_matiere = 0
        self.libelle = libelle



