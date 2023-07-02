from .table_personne import *


class TableEleve(TablePersonne):
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
        TablePersonne.__init__(
            self, nom, prenom, date_naissance, contact, genre, adresse
        )
        self.tuteur = tuteur
        self.classe = classe



