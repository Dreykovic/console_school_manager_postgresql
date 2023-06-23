from .table import Table
from .schema_builder import *

# from linker import linker


class TableClasse(Table):
    relation = "classe"
    schema = [
        PrimaryKey("id_classe").build(),
        String("nom").not_null().build(),
        Integer("effectif").build(),
    ]

    primary_key = "id_classe"

    def __init__(self, nom=None, effectif=0):
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif


def main():
    print(TableClasse.schema)
    


if __name__ == "__main__":
    main()
    print(dir())
    pass




