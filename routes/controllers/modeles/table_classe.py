# from .table import Table
from table import Table


class TableClasse(Table):
    INFO_ATTR = "nom, effectif"
    relation = "classe"
    schema = [
        ("id_classe", "k", "serial", "", ""),
        ("nom", "", "varchar", "", ""),
        ("effectif", "", "integer", "", ""),
    ]
    primary_key = "id_classe"

    def __init__(self, nom=None, effectif=0):
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif

    @classmethod
    def update_nom(cls, matricule, nom):
        row = []
        req = ""
        try:
            req = f"UPDATE  {cls.relation} SET nom = '{nom}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(cls.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du libelle de  {row[0]} {row[1]}:\n{req}\n :"
            )
            print(err)
            return 0
        else:
            cls.lk.commit()
            print("Nom de classe mis à jour avec succès !!!")
            return 1

    @classmethod
    def update_effectif(cls, matricule, effectif):
        row = []
        req = ""
        try:
            req = f"UPDATE  {cls.relation} SET effectif = '{effectif}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(cls.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du libelle de  {row[0]} {row[1]}:\n{req}\n :"
            )
            print(err)
            return 0
        else:
            cls.lk.commit()
            print("Effectid de classe mis à jour avec succès !!!")
            return 1


def main():
    tut = TableClasse("Dosseh")
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass


