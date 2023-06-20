from .table_personne import TablePersonne
import datetime as dt


class TableEnseignant(TablePersonne):
    relation = "enseignant"
    schema = [
        ("matricule", "k", "serial", "", ""),
        ("nom", "", "varchar", "", ""),
        ("prenoms", "", "varchar", "", ""),
        ("date_naissance", "", "date", "", ""),
        ("contact", "", "varchar", "", ""),
        ("genre", "", "varchar", "", ""),
        ("adresse", "", "varchar", "", ""),
        ("statut", "", "varchar", "", ""),
    ]
    primary_key = "matricule"

    def __init__(
        self,
        nom=None,
        prenom=None,
        date_naissance=None,
        contact=None,
        genre=None,
        adresse=None,
        statut=None,
    ):
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.statut = statut


def main():
    datenaiss = dt.datetime(2003, 1, 2).date()
    tut = TableEnseignant(
        "Dosseh", "OOO", datenaiss, "70546987", "M", "BP 25 Sok", "Soulard"
    )
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass
