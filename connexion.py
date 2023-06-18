#!/bin/python3
import psycopg2
import env

class Connexion:
    database = env.database
    username = env.username
    passwd = env.passwd
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                dbname=Connexion.database, user=Connexion.username)
        except Exception as err:
            print(
                'La connexion avec la base de données a échoué :\n''Erreur détectée :\n%s' % err)
            self.echec = 1
        else:
            self.cur = self.conn.cursor()
            # création du curseur
            self.echec = 0

    def executerReq(self, req, param=None):
        try:
            self.cur.execute(req, param)
        except Exception as err:
            print("Requête SQL incorrecte :\n{}\nErreur détectée :".format(req))
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


if __name__ == "__main__":
    pass
    bd = Connexion()
    bd.executerReq("SELECT * FROM personne;")
    res = bd.resultatReq()
    for elmt in res:
        print(elmt)
    bd.close()





