from .table import Table
from .schema_builder import *

class TableQuelqueChose(Table):
    """Classe représentant une table de quelque chose dans la base de données."""

    relation = "quelque_chose"
    schema = [
        PrimaryKey("id_quelque_chose").build(),
        String("nom").not_null().build(),
        Integer("attribut").build(),
    ]
    primary_key = "id_quelque_chose"

    def __init__(self, nom=None, attribut=0):
        """Initialise une instance de la classe TableQuelqueChose.

        Args:
            nom (str): Nom de quelque chose.
            attribut (int): Attribut de quelque chose.
        """
        self.id_quelque_chose = 0
        self.nom = nom
        self.attribut = attribut
