from modeles.table_matiere import TableMatiere as Matiere
from controller import Controller


class MatiereController(Controller):
    model = Matiere

    def __init__(
        self,
    ):
        self.create()
        pass

    @classmethod
    def create(cls):
        libelle = cls.read("libelle")
        matiere = Matiere(libelle)
        matiere.create()

    @classmethod
    def update(cls):
        value = cls.read("libelle")
        super().update("libelle",value)


if __name__ == "__main__":
    t = MatiereController()
