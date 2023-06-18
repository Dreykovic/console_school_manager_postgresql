class TableEleve(object):
    table = 'eleve'
    schema = [("matricule", "k", "serial", "", ""),
              ("nom", "", "varchar", "", ""),
              ("prenoms", "", "varchar", "", ""),
              ("date_naissance", "", "date", "", ""),
              ("contact", "", "varchar", "", ""),
              ("genre", "", "varchar", "", ""),
              ("adresse", "", "varchar", "", ""),
              ("tuteur", "rf", "integer", "matricule", "tuteur"),
              ("classe", "rf", "varchar", "nom", "classe")]
