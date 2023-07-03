from .table_classe import TableClasse
from .table_eleve import TableEleve
from .table_enseignant import TableEnseignant
from .table_matiere import TableMatiere
from .table_programme import TableProgramme
from .table_tuteur import TableTuteur
"""
Ce module contient les définitions des tables de la base de données.

Tables disponibles :
- TableClasse : Table représentant les classes.
- TableEleve : Table représentant les élèves.
- TableEnseignant : Table représentant les enseignants.
- TableMatiere : Table représentant les matières.
- TableProgramme : Table représentant les programmes.
- TableTuteur : Table représentant les tuteurs.

Les tables sont définies dans des fichiers séparés et importées ici pour faciliter leur utilisation.

Le dictionnaire "tables" contient les schémas des tables de la base de données. Les clés sont les noms des tables et les valeurs sont les schémas correspondants.

Exemple d'utilisation :

from database import tables

# Accéder au schéma de la table Classe
classe_schema = tables['classe']

# Créer une instance de la table Classe
classe = TableClasse(nom='Classe A', effectif=25)

# Insérer des données dans la table Classe
classe.insert()

Note : Assurez-vous d'avoir correctement importé les fichiers des tables correspondantes pour que le dictionnaire "tables" soit correctement rempli.

"""


tables = {
    TableClasse.relation: TableClasse.schema,
    TableTuteur.relation: TableTuteur.schema,
    TableEleve.relation: TableEleve.schema,
    TableEnseignant.relation: TableEnseignant.schema,
    TableMatiere.relation: TableMatiere.schema,
    TableProgramme.relation: TableProgramme.schema
}
"""
Un dictionnaire contenant les schémas des tables de la base de données.
Les clés sont les noms des tables et les valeurs sont les schémas correspondants.
"""





