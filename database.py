from table_classe import TableClasse
from table_eleve import TableEleve
from table_enseignant import TableEnseignant
from table_matiere import TableMatiere
from table_niveau_serie import TableNiveauSerie
from table_programme import TableProgramme
from table_tuteur import TableTuteur


class Database(object):
    """docstring for Glob"""

    tables = {
        TableNiveauSerie.table: TableNiveauSerie.schema,
        TableClasse.table: TableClasse.schema,
        TableTuteur.table: TableTuteur.schema,
        TableEleve.table: TableEleve.schema,
        TableEnseignant.table: TableEnseignant.schema,
        TableMatiere.table: TableMatiere.schema,
        TableProgramme.table: TableProgramme.schema
    }


# print(Glob.base)
