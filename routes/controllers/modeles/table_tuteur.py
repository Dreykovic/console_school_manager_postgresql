from table_personne import *


class TableTuteur(TablePersonne):
    relation = "tuteur"
    schema = TablePersonne.schema
    schema.append(not_null(string("profession")))

    def __init__(
        self,
        nom=None,
        prenom=None,
        date_naissance=None,
        contact=None,
        genre=None,
        adresse=None,
        profession=None,
    ):
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.profession = profession


def main():
    print(TableTuteur.schema)


if __name__ == "__main__":
    main()
    print("5555")
    pass
