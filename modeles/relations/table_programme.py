class TableProgramme(object):
    table = 'programme'
    schema = [("matiere", "rf", "integer",
               "id_matiere", "matiere"),
              ("prof", "rf", "integer",
               "matricule", "enseignant"),
              ("classe", "rf", "varchar", "nom", "classe")]
