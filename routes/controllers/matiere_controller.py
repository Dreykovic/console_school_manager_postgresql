from modeles.table_matiere import TableMatiere as Matiere
from controller import Controller

class MatiereController(Controller):
    model = Matiere

    def __init__(
        self,
    ):
        self.ajouter()
        pass

    @classmethod
    def ajouter(cls):
        libelle = cls.write_text("libelle")
        matiere = Matiere(
            libelle
        )
        matiere.create()
    @classmethod
    def editer(cls):
        value = cls.write_text("libelle")
        Matiere.update_libelle(cls.write_number("matricule"), value)





t = MatiereController()
