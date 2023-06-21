from table_personne import TablePersonne
import datetime as dt


class TableEnseignant(TablePersonne):
    relation = "enseignant"
    schema = TablePersonne.schema
    schema.append(not_null(string("statut")))

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
    tut = TableEnseignant(
        "Dosseh", "OOO", datenaiss, "70546987", "M", "BP 25 Sok", "Soulard"
    )
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass
