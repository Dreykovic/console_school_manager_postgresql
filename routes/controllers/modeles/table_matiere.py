from .table import Table


class TableMatiere(Table):
    INFO_ATTR = "libelle"
    relation = "matiere"
    schema = [("id_matiere", "k", "serial", "", ""), ("libelle", "", "varchar", "", "")]
    primary_key = "id_matiere"

    def __init__(
        self,
        libelle=None,
    ):
        self.id_matiere = 0
        self.libelle = libelle



def main():
    tut = TableMatiere("Dosseh")
    tut.create()
    TableMatiere.updateLibelle(1, "Koba")


if __name__ == "__main__":
    main()
    print("5555")
    pass
