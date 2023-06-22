from modeles.table_enseignant import TableEnseignant as Enseignant
from modeles.table_classe import TableClasse as Classe
from modeles.table_matiere import TableMatiere as Matiere
from modeles.table_programme import TableProgramme as Programme
from controller import Controller


class ProgrammeController(Controller):
    model = Programme

    def __init__(
        self,
    ):
        self.create()

    @classmethod
    def create(cls):
        coef = cls.read("coeficient", False, ["1", "2", "3", "4", "5"])
        tuteur = cls.assigner_tuteur()
        classe = cls.assigner_classe()

        eleve = Eleve(
            tuteur, classe, nom, prenoms, date_naissance, contact, genre, adresse
        )
        eleve.create()



    @classmethod
    def assigner(cls, reference):
        data = cls.show(Matiere)
        ids = [t[0] for t in data]
        identifiant = cls.write_number(f"id {reference.relation} ")
        while identifiant not in ids:
            print(f"l'id {identifiant} ne correspond a aucune {reference.relation}")
            identifiant = cls.write_number(f"id {reference.relation} ")
        return identifiant



t = EleveController()
