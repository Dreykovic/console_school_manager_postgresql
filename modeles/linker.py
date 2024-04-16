"""
Module contenant la classe Linker pour établir une liaison avec une base de données SGBDR, notamment PostgreSQL.
"""
import os
import sys
sys.path.append(f'{os.getcwd}' )
import psycopg2
import settings


class Linker(object):
    """
    Linker permet de faire un lien entre Python et une base de données SGBDR, notamment PostgreSQL.
    """

    def __init__(self, dbname= settings.database ):
        """
        Initialise une nouvelle instance du Linker et établit une connexion à la base de données.
        """
        self.conn =""
        self.cur = ""
        self.dbname = dbname
        try:

            self.conn = psycopg2.connect(
                dbname=dbname,
                user=settings.username,
                password=settings.passwd,
                host=settings.host,
                port=settings.port
            )
        except Exception as err:
            print("La connexion avec la base de données a échoué :\nErreur détectée :\n{err}")
            print(err)
            self.echec = 1
        else:
            self.cur = self.conn.cursor()
            self.echec = 0

    def executerReq(self, req, param=None):
        """
        Exécute une requête SQL sur la base de données.

        Args:
            req (str): La requête SQL à exécuter.
            param (tuple, optional): Les paramètres à passer à la requête (si nécessaire). Par défaut, None.

        Returns:
            int: 1 si la requête a été exécutée avec succès, 0 sinon.
        """
        try:
            self.cur.execute(req, param)
        except Exception as err:
            print(f"Requête SQL incorrecte :\n{req}\nErreur détectée :")
            print(err)
            return 0
        else:
            return 1

    def resultatReq(self):
        """
        Récupère les résultats de la dernière requête exécutée.

        Returns:
            list: Les résultats de la requête.
        """
        return self.cur.fetchall()

    def commit(self):
        """
        Effectue la validation des modifications apportées à la base de données.
        """

        if self.conn:
            self.conn.commit()

    def close(self):
        """
        Ferme la connexion à la base de données.
        """
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
