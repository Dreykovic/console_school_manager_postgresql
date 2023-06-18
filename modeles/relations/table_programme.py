from table import Table
class TableProgramme(Table):
    table = 'programme'
    schema = [("matiere", "rf", "integer",
               "id_matiere", "matiere"),
              ("prof", "rf", "integer",
               "matricule", "enseignant"),
              ("classe", "rf", "varchar", "nom", "classe")]
