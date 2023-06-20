from .table import Table


class TableProgramme(Table):
    relation = "programme"
    schema = [
        ("id_programme", "k", "integer", "", ""),
        ("matiere", "rf", "integer", "id_matiere", "matiere"),
        ("prof", "rf", "integer", "matricule", "enseignant"),
        ("classe", "rf", "integer", "id_classe", "classe"),
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
