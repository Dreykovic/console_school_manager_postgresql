class Glob(object):
    """docstring for Glob"""

    database = "gestion_note"
    username = "audrey"
    passwd = "1234"
    host = "127.0.0.1"
    port = 5432

    base = {"niveau_seri": [("niveau", "", "varchar", "", ""),
                            ("serie", "", "varchar", "", "")],
            "classe": [("nom", "k", "varchar", "", ""),
                       ("effectif", "", "integer", "", "")],
            "tuteur": [("matricule", "k", "serial", "", ""),
                       ("nom", "", "varchar", "", ""),
                       ("prenoms", "", "varchar", "", ""),
                       ("date_naissance", "", "date", "", ""),
                       ("contact", "", "varchar", "", ""),
                       ("genre", "", "varchar", "", ""),
                       ("adresse", "", "varchar", "", ""),
                       ("profession", "", "varchar", "", "")],
            "eleve": [("matricule", "k", "serial", "", ""),
                      ("nom", "", "varchar", "", ""),
                      ("prenoms", "", "varchar", "", ""),
                      ("date_naissance", "", "date", "", ""),
                      ("contact", "", "varchar", "", ""),
                      ("genre", "", "varchar", "", ""),
                      ("adresse", "", "varchar", "", ""),
                      ("tuteur", "rf", "integer", "matricule", "tuteur"),
                      ("classe", "rf", "varchar", "nom", "classe")],
            "enseignant": [("matricule", "k", "serial", "", ""),
                           ("nom", "", "varchar", "", ""),
                           ("prenoms", "", "varchar", "", ""),
                           ("date_naissance", "", "date", "", ""),
                           ("contact", "", "varchar", "", ""),
                           ("genre", "", "varchar", "", ""),
                           ("adresse", "", "varchar", "", ""),
                           ("statut", "", "varchar", "", "")],
            "matiere": [("id_matiere", "k", "serial", "", ""),
                        ("libelle", "", "varchar", "", "")],
            "programme": [("matiere", "rf", "integer",
                           "id_matiere", "matiere"),
                          ("prof", "rf", "integer",
                           "matricule", "enseignant"),
                          ("classe", "rf", "varchar", "nom", "classe")]

            }


print(Glob.base)
