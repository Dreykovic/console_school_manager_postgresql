# from table import Table
import datetime as dt
from table_personne import TablePersonne


class TableTuteur(TablePersonne):
    table = 'tuteur'
    schema = [("matricule", "k", "serial", "", ""),
              ("nom", "", "varchar", "", ""),
              ("prenoms", "", "varchar", "", ""),
              ("date_naissance", "", "date", "", ""),
              ("contact", "", "varchar", "", ""),
              ("genre", "", "varchar", "", ""),
              ("adresse", "", "varchar", "", ""),
              ("profession", "", "varchar", "", "")]
    primary_key = 'matricule'

    def __init__(self,  nom=None, prenom=None, date_naissance=None, contact=None, genre=None, adresse=None, profession=None):
        TablePersonne.__init__(
            self,  nom, prenom, date_naissance, contact, genre, adresse)
        self.profession = profession

    @classmethod
    def updateProfession(cls, matricule, profession):

        try:
            req = f"UPDATE  {cls.table} SET profession = '{profession}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, prenoms', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour de la profession de  {row[0]} {row[1]}:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1


def main():

    datenaiss = dt.datetime(2003, 1, 2).date()
    tut = TableTuteur("Dosseh", "OOO", datenaiss, "70546987",
                      "M", "BP 25 Sok", "Soulard")
    tut.create()
    tut.updateProfession(2, "Koba")


if __name__ == '__main__':
    main()
    print('5555')
    pass















