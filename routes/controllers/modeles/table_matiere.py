from table import Table


class TableMatiere(Table):
    INFO_ATTR = "libelle"
    relation = "matiere"
    schema = [("id_matiere", "k", "serial", "", ""), ("libelle", "", "varchar", "", "")]
    primary_key = "id_matiere"

    def __init__(
        self,
        libelle=None,
    ):
        self.id_matiere = 0
        self.libelle = libelle

    @classmethod
    def update_libelle(cls, matricule, libelle):
        req = ""
        row = []
        try:
            req = f"UPDATE  {cls.relation} SET libelle = '{libelle}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id("libelle", matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du libelle de  {row[0]}:\n{req}\n :"
            )
            print(err)
            return 0
        else:
            cls.lk.commit()
            print('UPDATE SUCCESSFULLY')
            return 1


def main():
    tut = TableMatiere("Dosseh")
    tut.create()
    TableMatiere.updateLibelle(1, "Koba")


if __name__ == "__main__":
    main()
    print("5555")
    pass
