from table_personne import *


class TableEleve(TablePersonne):
    relation = "eleve"

    schema = [
        primary_key("matricule"),
        not_null(string("nom")),
        not_null(string("prenom")),
        not_null(date("date_naissance")),
        not_null(string("contact")),
        not_null(string("genre")),
        not_null(string("adresse")),
        references(foreign_key(integer("tuteur")), "tuteur", "matricule"),
        references(foreign_key(integer("classe")), "classe", "id_classe"),
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
    import datetime as dt

    main()
    print("5555")
    pass
