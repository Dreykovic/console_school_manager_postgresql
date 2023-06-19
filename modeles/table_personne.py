from .table import Table
import datetime as dt


class TablePersonne(Table):

    def __init__(self,  nom=None, prenom=None, date_naissance=None, contact=None, genre=None, adresse=None, ):
        self.matricule = 0
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.contact = contact
        self.genre = genre
        self.adresse = adresse
        self.INFO_ATTR = 'nom, prenoms'
        # print(TablePersonne.schema)

    @classmethod
    def updateNom(cls, matricule, nom):
        try:
            req = f"UPDATE  {cls.relation} SET nom = '{nom}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du nom de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def update_prenoms(cls, matricule, prenoms):
        try:
            req = f"UPDATE  {cls.relation} SET prenoms = '{prenoms}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du prenom de {row[0]} {row[1]}:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def update_date_naissance(cls, matricule, date_naissance):
        try:
            req = f"UPDATE  {cls.relation} SET date_naissance = '{date_naissance}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour de la date de naissance de {row[0]} {row[1]}:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def update_contact(cls, matricule, contact):
        try:
            req = f"UPDATE  {cls.relation} SET contact = '{contact}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du contact de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    def update_genre(cls, matricule, genre):
        try:
            req = f"UPDATE  {cls.relation} SET genre = '{genre}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du genre de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def update_adresse(cls, matricule, adresse):
        try:
            req = f"UPDATE  {cls.relation} SET adresse = '{adresse}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.select_attr_where_id(self.INFO_ATTR, matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour de l'adresse de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1
