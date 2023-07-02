import sys
import psycopg2
from . import env


class Linker(object):
    """Linker permet de faire un lien entre python et une SGBDR notamment PostgreSQL"""

    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname=env.database,
                user=env.username,
                password=env.passwd,
                port=env.port,
                host=env.host,
            )
        except Exception as err:
            print(
                f"La connexion avec la base de données a échoué :\nErreur détectée :\n{err}"
            )
            self.echec = 1
        else:
            self.cur = self.conn.cursor()
            self.echec = 0

    def executerReq(self, req, param=None):
        try:
            self.cur.execute(req, param)
        except Exception as err:
            print(f"Requête SQL incorrecte :\n{req}\nErreur détectée :")
            print(err)
            return 0
        else:
            return 1

    def resultatReq(self):
        return self.cur.fetchall()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()


# def main():
#     f = Linker()
#     f.createTables(Database.tables)

    # f.createTables({TableTuteur.table:TableTuteur.schema})


if __name__ == "__main__":
    # main()
    pass
