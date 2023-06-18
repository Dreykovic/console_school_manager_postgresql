class TableEnseignant(object):
    table = 'enseignant'
    schema = [("matricule", "k", "serial", "", ""),
              ("nom", "", "varchar", "", ""),
              ("prenoms", "", "varchar", "", ""),
              ("date_naissance", "", "date", "", ""),
              ("contact", "", "varchar", "", ""),
              ("genre", "", "varchar", "", ""),
              ("adresse", "", "varchar", "", ""),
              ("statut", "", "varchar", "", "")]
