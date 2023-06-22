from modeles.table_classe import TableClasse
from modeles.table_eleve import TableEleve
from modeles.table_enseignant import TableEnseignant
from modeles.table_matiere import TableMatiere
from modeles.table_programme import TableProgramme
from modeles.table_tuteur import TableTuteur
from datetime import datetime as dt
from modeles.migration import *
from modeles.database import tables

for relation in tables:
    create_tables(relation, tables[relation])


TableClasse("2nde A4").create()
TableClasse("2nde D").create()
TableClasse("2nde C4").create()
TableClasse("1ere D").create()
TableClasse("1ere A4").create()
TableClasse("1ere C4").create()
TableTuteur(
    "ATALAKPOU",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableTuteur(
    "FUjustsi",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableTuteur(
    "ATALAKPOU",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableTuteur(
    "ATALAKPOU",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableEnseignant(
    "ATALAKPOU",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableEnseignant(
    "ATALAKPOU",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableEnseignant(
    "ATALAKPOU",
    "Ferdinand",
    dt(2001, 1, 1).date(),
    "90546875",
    "H",
    "AKAMADE",
    "AAstronaute",
)
TableEleve(
    2, 2, "ATALAKPOU", "Ferdinand", dt(2001, 1, 1).date(), "90546875", "H", "AKAMADE"
)
TableEleve(
    2, 1, "ATALAKPOU", "Ferdinand", dt(2001, 1, 1).date(), "90546875", "H", "AKAMADE"
)
TableEleve(
    2, 2, "ATALAKPOU", "Ferdinand", dt(2001, 1, 1).date(), "90546875", "H", "AKAMADE"
)
TableMatiere("MAth")
TableMatiere("PC")
TableMatiere("HG")
