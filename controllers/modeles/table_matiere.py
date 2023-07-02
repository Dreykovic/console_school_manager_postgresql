from .table import Table
from .schema_builder import *


class TableMatiere(Table):
    """Classe représentant une table de matières dans la base de données."""

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
        """Initialise une instance de la classe TableMatiere.

        Args:
            libelle (str): Libellé de la matière.
        """
        self.id_matiere = 0
        self.libelle = libelle
