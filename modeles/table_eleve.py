from .table_personne import *


class TableEleve(TablePersonne):
    """Classe représentant une table d'élèves dans la base de données."""

    relation = "eleve"

    schema = [
        PrimaryKey("matricule").build(),
        String("nom").not_null().build(),
        String("prenoms").not_null().build(),
        Date("date_naissance").not_null().build(),
        String("contact").not_null().build(),
        String("genre").not_null().build(),
        String("adresse").not_null().build(),
        Integer("tuteur").foreign_key().references("tuteur", "matricule").build(),
        Integer("classe").foreign_key().references("classe", "id_classe").build(),
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
        """Initialise une instance de la classe TableEleve.

        Args:
            tuteur (int): Matricule du tuteur de l'élève.
            classe (int): ID de la classe de l'élève.
            nom (str): Nom de l'élève.
            prenom (str): Prénoms de l'élève.
            date_naissance (str): Date de naissance de l'élève.
            contact (str): Contact de l'élève.
            genre (str): Genre de l'élève.
            adresse (str): Adresse de l'élève.
        """
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.tuteur = tuteur
        self.classe = classe
