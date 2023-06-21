from table import Table
from schema_builder import *


class TableMatiere(Table):
    relation = "matiere"
    schema = [
        primary_key("id_matiere"),
        unique(not_null(string("libelle"))),
    ]

    primary_key = "id_matiere"

    def __init__(
        self,
        libelle=None,
    ):
        self.id_matiere = 0
        self.libelle = libelle


def main():
    print(TableMatiere.schema)


if __name__ == "__main__":
    main()
    print("5555")
    pass

