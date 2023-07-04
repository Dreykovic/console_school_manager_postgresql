__all__ = ["PrimaryKey", "String", "Integer", "Date"]

class SchemaBuilder:
    """Classe de construction du schéma de colonne pour une table."""

    col = dict()

    def unique(self):
        """Spécifie que la colonne doit contenir des valeurs uniques."""
        self.col["unique"] = 1
        return self

    def not_null(self):
        """Spécifie que la colonne ne peut pas contenir de valeurs nulles."""
        self.col["null"] = 0
        return self

    def foreign_key(self):
        """Spécifie que la colonne est une clé étrangère."""
        self.col["constraint"] = "rk"
        return self

    def references(self, table, ref_key):
        """Spécifie la table et la clé de référence pour la colonne.

        Args:
            table (str): Nom de la table de référence.
            ref_key (str): Clé de référence dans la table de référence.
        """
        self.col["reference_table"] = table
        self.col["reference_col"] = ref_key
        return self

    def build(self):
        """Construit et retourne le dictionnaire de la colonne."""
        return self.col


class String(SchemaBuilder):
    """Classe de construction du schéma d'une colonne de type chaîne de caractères."""

    def __init__(self, name):
        """Initialise une instance de la classe String.

        Args:
            name (str): Nom de la colonne.
        """
        self.col = {
            "column_name": name,
            "constraint": "",
            "type": "varchar",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }


class PrimaryKey(SchemaBuilder):
    """Classe de construction du schéma d'une colonne de clé primaire."""

    def __init__(self, name):
        """Initialise une instance de la classe PrimaryKey.

        Args:
            name (str): Nom de la colonne.
        """
        self.col = {
            "column_name": name,
            "constraint": "pk",
            "type": "serial",
            "reference_col": "",
            "reference_table": "",
            "null": 0,
            "unique": 1,
        }


class Integer(SchemaBuilder):
    """Classe de construction du schéma d'une colonne de type entier."""

    def __init__(self, name):
        """Initialise une instance de la classe Integer.

        Args:
            name (str): Nom de la colonne.
        """
        self.col = {
            "column_name": name,
            "constraint": "",
            "type": "integer",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }


class Date(SchemaBuilder):
    """Classe de construction du schéma d'une colonne de type date."""

    def __init__(self, name):
        """Initialise une instance de la classe Date.

        Args:
            name (str): Nom de la colonne.
        """
        self.col = {
            "column_name": name,
            "constraint": "",
            "type": "date",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }
