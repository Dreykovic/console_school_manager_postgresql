from table import Table
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
        # print(TablePersonne.schema)

    @classmethod
    def updateNom(cls, matricule, nom):
        try:
            req = f"UPDATE  {cls.table} SET nom = '{nom}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, prenoms', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du nom de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def updatePrenoms(cls, matricule, prenoms):
        try:
            req = f"UPDATE  {cls.table} SET prenoms = '{prenoms}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du prenom de {row[0]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def updateDateNaissance(cls, matricule, date_naissance):
        try:
            req = f"UPDATE  {cls.table} SET date_naissance = '{date_naissance}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour de la date de naissance de {row[0]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def updateContact(cls, matricule, contact):
        try:
            req = f"UPDATE  {cls.table} SET contact = '{contact}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, prenoms', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du contact de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    def updateGenre(cls, matricule, genre):
        try:
            req = f"UPDATE  {cls.table} SET genre = '{genre}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, prenoms', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour du genre de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def updateAdresse(cls, matricule, adresse):
        try:
            req = f"UPDATE  {cls.table} SET adresse = '{adresse}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            row = cls.selectAttrWhereId('nom, prenoms', matricule)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour de l'adresse de {row[0]} {row[1]} :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1
