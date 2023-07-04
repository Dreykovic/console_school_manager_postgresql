"""
Module contenant la classe Table pour interagir avec une table dans une base de données.
"""

from .linker import Linker
import sys

class Table(object):
    """
    Classe Table pour interagir avec une table dans une base de données.
    """

    relation = ""
    """
    Nom de la relation (table) dans la base de données.
    """

    schema = []
    """
    Schéma de la table, décrivant les colonnes et leurs types.
    """

    primary_key = ""
    """
    Clé primaire de la table.
    """

    lk = Linker()

    @classmethod
    def get_columns(cls):
        """
        Récupère les noms des colonnes de la table.

        Returns:
            list: Liste des noms de colonnes.
        """
        return [t["column_name"] for t in cls.schema]

    @classmethod
    def get_colunm_type(cls, column):
        """
        Récupère le type de données d'une colonne spécifiée.

        Args:
            column (str): Nom de la colonne.

        Returns:
            str: Type de données de la colonne.
        """
        for elmet in cls.schema:
            if elmet["column_name"] == column:
                return elmet["type"]

    def create(self):
        """
        Crée un nouvel enregistrement dans la table avec les valeurs des attributs de l'objet.

        Raises:
            NameError: Si une erreur survient lors de la création de l'enregistrement.
        """
        data = tuple()
        try:
            for attr in self.__dict__:
                if attr == self.primary_key:
                    try:
                        self.__dict__[attr] = self.key() + 1
                    except TypeError:
                        self.__dict__[attr] = 1
                if attr == "INFO_ATTR":
                    continue
                data += (self.__dict__[attr],)
            self.insert(data)
        except NameError as err:
            print("❌ »»»» Une erreur est survenue lors de la création  :\n :")
            sys.exit(0)

    @classmethod
    def insert(cls, data):
        """
        Insère un nouvel enregistrement dans la table avec les données fournies.

        Args:
            data (tuple): Données à insérer dans les colonnes correspondantes de la table.

        Returns:
            int: 1 si l'insertion a réussi, sinon 0.

        Raises:
            Exception: Si une erreur survient lors de l'insertion.
        """
        req = ""
        try:
            columns = "("
            for col in cls.schema:
                columns += " " + col["column_name"] + ","
            columns = columns[:-1] + " )"
            column_number = len(cls.schema)
            values = "("
            values += " %s, " * column_number
            values = values[:-2] + ")"

            req = f"INSERT INTO {cls.relation} {columns} VALUES {values};"
            cls.lk.executerReq(req, data)
        except Exception as err:
            print(f"❌ »»»» Une erreur est survenue lors de l'insertion :\n{req}\n :")
            sys.exit(0)
        else:
            cls.lk.commit()
            print("INSERT SUCCESSFULY !!!✔️")
            return 1

    @classmethod
    def key(cls):
        """
        Récupère la clé maximale (valeur) de la colonne de clé primaire de la table.

        Returns:
            int: Valeur de la clé maximale.

        Raises:
            Exception: Si une erreur survient lors de la récupération de la clé.
        """
        req = ""
        try:
            req = f"SELECT max({cls.primary_key}) From {cls.relation};"
            cls.lk.executerReq(req)
            key = cls.lk.resultatReq()[0][0]
        except Exception as err:
            print(f"❌ »»»» Id fetch problem :\n{req}\n :")
            sys.exit(0)
        else:
            return key

    @classmethod
    def select_attr_where_id(cls, attributes, matricule):
        """
        Sélectionne les valeurs des attributs spécifiés pour un enregistrement avec une clé primaire donnée.

        Args:
            attributes (str): Attributs à sélectionner (séparés par des virgules).
            matricule (str): Clé primaire de l'enregistrement.

        Returns:
            list or int: Liste des valeurs des attributs sélectionnés, ou 0 si aucune correspondance n'a été trouvée.

        Raises:
            Exception: Si une erreur survient lors de la sélection.
        """
        req = ""
        try:
            sql = f"SELECT {attributes} FROM {cls.relation} WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"❌ »»»» Select problem :\n{req}\n :")
            sys.exit(0)
        else:
            if len(row) == 0:
                print("!!! ❌ »»»»   Désolé, aucune correspondance")
                return 0
            else:
                return row[0]

    @classmethod
    def select_attr(cls, attributes):
        """
        Sélectionne les valeurs des attributs spécifiés pour tous les enregistrements de la table.

        Args:
            attributes (str): Attributs à sélectionner (séparés par des virgules).

        Returns:
            list: Liste des valeurs des attributs sélectionnés.

        Raises:
            Exception: Si une erreur survient lors de la sélection.
        """
        req = ""
        try:
            sql = f"SELECT {attributes} FROM {cls.relation};"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"❌ »»»»  Select problem :\n{req}\n :")
            sys.exit(0)
        else:
            return row

    @classmethod
    def select_all(cls):
        """
        Sélectionne tous les enregistrements de la table.

        Returns:
            list: Liste des enregistrements sélectionnés.

        Raises:
            Exception: Si une erreur survient lors de la sélection.
        """
        req = ""
        try:
            sql = f"SELECT * FROM {cls.relation};"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"❌ »»»»  Select problem :\n{req}\n :")
            sys.exit(0)
        else:
            return row

    @classmethod
    def delete(cls, matricule):
        """
        Supprime un enregistrement de la table avec la clé primaire spécifiée.

        Args:
            matricule (str): Clé primaire de l'enregistrement à supprimer.

        Returns:
            int: 1 si la suppression a réussi, sinon 0.

        Raises:
            Exception: Si une erreur survient lors de la suppression.
        """
        req = ""
        try:
            req = f"DELETE FROM {cls.relation} WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
        except Exception as err:
            print(f"❌ »»»»  Une erreur est survenue lors de la suppressiond:\n{req}\n :")
            sys.exit(0)
        else:
            cls.lk.commit()
            print("DELETED !!!✔️ ")
            return 1

    @classmethod
    def update(cls, attribut, matricule, value):
        """
        Met à jour la valeur d'un attribut pour un enregistrement avec une clé primaire donnée.

        Args:
            attribut (str): Attribut à mettre à jour.
            matricule (str): Clé primaire de l'enregistrement.
            value (str): Nouvelle valeur de l'attribut.

        Returns:
            int: 1 si la mise à jour a réussi, sinon 0.

        Raises:
            Exception: Si une erreur survient lors de la mise à jour.
        """
        row = ""
        req = ""
        try:
            req = f"UPDATE  {cls.relation} SET {attribut} = '{value}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
        except Exception as err:
            print(
                f"❌ »»»» Une erreur est survenue lors de la mise à jour de {attribut} : ID:{matricule}:\n{req}\n :"
            )
            sys.exit(0)
        else:
            cls.lk.commit()
            print("UPDATED SUCCESSFULLY !!!✔️ ")
            return 1
