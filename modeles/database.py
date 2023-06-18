from relations.table_classe import TableClasse
from relations.table_eleve import TableEleve
from relations.table_enseignant import TableEnseignant
from relations.table_matiere import TableMatiere
from relations.table_niveau_serie import TableNiveauSerie
from relations.table_programme import TableProgramme
from relations.table_tuteur import TableTuteur


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



