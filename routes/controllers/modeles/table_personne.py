from table import Table
import datetime as dt
from schema_builder import *


class TablePersonne(Table):
    schema = [
        primary_key("matricule"),
        not_null(string("nom")),
        not_null(string("prenom")),
        not_null(date("date_naissance")),
        not_null(string("contact")),
        not_null(string("genre")),
        not_null(string("adresse")),
        not_null(string("prenom")),
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
