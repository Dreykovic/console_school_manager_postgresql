from table import Table
from schema_builder import *


class TableProgramme(Table):
    relation = "programme"
    schema = [
        primary_key("id_programme"),
        references(foreign_key(integer("matiere")), "matiere", "id_matiere"),
        references(foreign_key(integer("prof")), "enseignat", "matricule"),
        references(foreign_key(integer("classe")), "classe", "id_classe"),
    ]
    primary_key = "id_programme"

    def __init__(self, matiere, prof, classe):
        self.id_programme = 0
        self.matiere = matiere
        self.prof = prof
        self.classe = classe


def main():
    tut = TableProgramme(1, 1, 1)
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass
