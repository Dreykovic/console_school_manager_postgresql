from .table_personne import *


class TableEnseignant(TablePersonne):
    """Classe représentant une table d'enseignants dans la base de données."""

    relation = "enseignant"
    schema = [
        PrimaryKey('matricule').build(),
        String('nom').not_null().build(),
        String('prenoms').not_null().build(),
        Date('date_naissance').not_null().build(),
        String('contact').not_null().build(),
        String('genre').not_null().build(),
        String('adresse').not_null().build(),
        String('statut').not_null().build(),
    ]

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
        """Initialise une instance de la classe TableEnseignant.

        Args:
            nom (str): Nom de l'enseignant.
            prenom (str): Prénoms de l'enseignant.
            date_naissance (str): Date de naissance de l'enseignant.
            contact (str): Contact de l'enseignant.
            genre (str): Genre de l'enseignant.
            adresse (str): Adresse de l'enseignant.
            statut (str): Statut de l'enseignant.
        """
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.statut = statut
