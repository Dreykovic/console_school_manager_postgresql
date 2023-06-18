from table import Table
class TableMatiere(Table):
    table = 'matiere'
    schema = [("id_matiere", "k", "serial", "", ""),
              ("libelle", "", "varchar", "", "")]
    primary_key = 'id_matiere'
    def __init__(self,  libelle=None,):
        self.id_matiere = 0
        self.libelle = libelle
        

    @classmethod
    def updateLibelle(cls, matricule, libelle):

        try:
            req = f"UPDATE  {cls.table} SET libelle = '{libelle}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('libelle', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du libelle de  {row[0]}:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1


def main():

    tut = TableMatiere("Dosseh")
    tut.create()
    TableMatiere.updateLibelle(1, "Koba")


if __name__ == '__main__':
    main()
    print('5555')
    pass




