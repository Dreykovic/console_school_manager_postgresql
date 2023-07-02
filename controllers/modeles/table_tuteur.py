from .table_personne import *


class TableTuteur(TablePersonne):
    """Classe représentant la table 'tuteur' dans la base de données."""

    relation = "tuteur"
    schema = [
        PrimaryKey("matricule").build(),
        String("nom").not_null().build(),
        String("prenoms").not_null().build(),
        Date("date_naissance").not_null().build(),
        String("contact").not_null().build(),
        String("genre").not_null().build(),
        String("adresse").not_null().build(),
        String("profession").not_null().build(),
    ]

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
        """Initialise une instance de la classe TableTuteur.

        Args:
            nom (str): Nom du tuteur.
            prenom (str): Prénoms du tuteur.
            date_naissance (str): Date de naissance du tuteur.
            contact (str): Contact du tuteur.
            genre (str): Genre du tuteur.
            adresse (str): Adresse du tuteur.
            profession (str): Profession du tuteur.
        """
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.profession = profession
