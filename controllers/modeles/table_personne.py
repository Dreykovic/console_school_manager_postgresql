from .table import Table
from .schema_builder import *


class TablePersonne(Table):
    """Classe représentant une table de personnes dans la base de données."""

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
        """Initialise une instance de la classe TablePersonne.

        Args:
            nom (str): Nom de la personne.
            prenom (str): Prénom de la personne.
            date_naissance (str): Date de naissance de la personne.
            contact (str): Contact de la personne.
            genre (str): Genre de la personne.
            adresse (str): Adresse de la personne.
        """
        self.matricule = 0
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.contact = contact
        self.genre = genre
        self.adresse = adresse
