from .table import Table
from .schema_builder import *

class TableClasse(Table):
    """Classe représentant une table de classes dans la base de données."""

    relation = "classe"
    schema = [
        PrimaryKey("id_classe").build(),
        String("nom").not_null().build(),
        Integer("effectif").build(),
    ]
    primary_key = "id_classe"

    def __init__(self, nom=None, effectif=0):
        """Initialise une instance de la classe TableClasse.

        Args:
            nom (str): Nom de la classe.
            effectif (int): Effectif de la classe (par défaut 0).
        """
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif


def main():
    """Fonction principale du module.

    Imprime le schéma de la table TableClasse.
    """
    print(TableClasse.schema)


if __name__ == "__main__":
    main()
    print(dir())
