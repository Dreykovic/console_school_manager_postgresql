from table import Table
from schema_builder import *

# from linker import linker


class TableClasse(Table):
    relation = "classe"
    schema = [
        primary_key("id_classe"),
        not_null(string("nom")),
        not_null(integer("effectif")),
    ]

    primary_key = "id_classe"

    def __init__(self, nom=None, effectif=0):
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif


def main():
    print(TableClasse.schema)
    a = [t["type"] for t in TableClasse.schema]
    print(00000)
    print(a)


if __name__ == "__main__":
    main()
    print("5555")
    pass
