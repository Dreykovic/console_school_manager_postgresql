from table import Table
import datetime as dt


class TablePersonne(Table):
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
