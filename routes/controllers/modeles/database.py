from .table_classe import TableClasse
from .table_eleve import TableEleve
from .table_enseignant import TableEnseignant
from .table_matiere import TableMatiere
from .table_niveau_serie import TableNiveauSerie
from .table_programme import TableProgramme
from .table_tuteur import TableTuteur


class Database(object):
    """docstring for Glob"""

    tables = {
        TableNiveauSerie.relation: TableNiveauSerie.schema,
        TableClasse.relation: TableClasse.schema,
        TableTuteur.relation: TableTuteur.schema,
        TableEleve.relation: TableEleve.schema,
        TableEnseignant.relation: TableEnseignant.schema,
        TableMatiere.relation: TableMatiere.schema,
        TableProgramme.relation: TableProgramme.schema
    }


# print(Glob.base)


