#!/bin/python3
from connexion import Connexion
import datetime as dt


class Linker:
    def __init__(self, connexion, table):
        self.bd = connexion
        self.table = table
        self.__infoTable = self.get_info_table()

    def get_info_table(self):
        self.bd.executerReq("""SELECT column_name
                            FROM information_schema.columns
                            WHERE table_name = %s
                            ORDER BY column_name ASC;""",
                            (self.table,))
        rows = self.bd.resultatReq()
        infoTable = tuple()
        for item in rows:
            infoTable += (item[0],)
        return infoTable

    def insert(self, data):
        id = False
        if (self.table == 'tuteur'):
            sql = "SELECT recup_id_tuteur " + str(data)+";"
            self.bd.executerReq(sql)
            id = self.bd.resultatReq()
        else:
            valeur = "( "
            schemas = "( "
            for info in self.__infoTable:
                if (info == "matricule" or info == "id_matiere"):
                    pass
                else:
                    schemas += info+", "
                    valeur += "%s, "
            schemas = schemas.strip(", ")
            valeur = valeur.strip(", ")
            schemas += ")"
            valeur += ")"
            sql = "INSERT INTO " + self.table + schemas + "VALUES " + valeur + " ;"
            self.bd.executerReq(sql, data)
        self.bd.commit()
        return id

    def select(self):
        schemas = " "
        for info in self.__infoTable:
            schemas += info+", "
        schemas = schemas.strip(", ")
        sql = "SELECT " + schemas + " FROM " + self.table + " ;"
        self.bd.executerReq(sql)
        rows = self.bd.resultatReq()
        return rows


if __name__ == "__main__":
    bd = Connexion()
    test = Linker(bd, table="matiere")
    test.insert(("math",))
    datenaiss = dt.datetime(2003, 1, 2).date()
    data = ('Sokodé',  '90542147', datenaiss, 'masculin', 'OZO', 'Audrey')
    test2 = Linker(bd, table="personne")
    test2.insert(data)
    bd.commit()
    bd.close()
    print('succes')




