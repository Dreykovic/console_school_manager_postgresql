from table import Table
import datetime as dt


class TablePersonne(Table):
    schema = [
        ("matricule", "k", "serial", "", ""),
        ("nom", "", "varchar", "", ""),
        ("prenoms", "", "varchar", "", ""),
        ("date_naissance", "", "date", "", ""),
        ("contact", "", "varchar", "", ""),
        ("genre", "", "varchar", "", ""),
        ("adresse", "", "varchar", "", ""),
        ("profession", "", "varchar", "", ""),
        Table.primary_key("matricule"),
        Table.not_null(Table.string('nom')),
        Table.not_null(Table.string('nom')),
        Table.not_null(Table.string('nom')),
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
    ):
        self.matricule = 0
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.contact = contact
        self.genre = genre
        self.adresse = adresse
