from table_personne import TablePersonne
import datetime as dt


class TableEleve(TablePersonne):
    relation = "eleve"
    schema = [
        ("matricule", "k", "serial", "", ""),
        ("nom", "", "varchar", "", ""),
        ("prenoms", "", "varchar", "", ""),
        ("date_naissance", "", "date", "", ""),
        ("contact", "", "varchar", "", ""),
        ("genre", "", "varchar", "", ""),
        ("adresse", "", "varchar", "", ""),
        ("tuteur", "rf", "integer", "matricule", "tuteur"),
        ("classe", "rf", "integer", "id_classe", "classe"),
    ]

    def __init__(
        self,
        tuteur,
        classe,
        nom=None,
        prenom=None,
        date_naissance=None,
        contact=None,
        genre=None,
        adresse=None,
    ):
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.tuteur = tuteur
        self.classe = classe


def main():
    datenaiss = dt.datetime(2003, 1, 2).date()
    tut = TableEleve(1, 1, "Dosseh", "OOO", datenaiss, "70546987", "M", "BP 25 Sok")
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass
