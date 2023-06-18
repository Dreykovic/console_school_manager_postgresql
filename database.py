from modeles.table_classe import TableClasse
from modeles.table_eleve import TableEleve
from modeles.table_enseignant import TableEnseignant
from modeles.table_matiere import TableMatiere
from modeles.table_niveau_serie import TableNiveauSerie
from modeles.table_programme import TableProgramme
from modeles.table_tuteur import TableTuteur


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
