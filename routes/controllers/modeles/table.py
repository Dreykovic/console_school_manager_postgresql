from linker import Linker


class Table(object):
    relation = ""
    schema = []
    primary_key = ""
    lk = Linker()

    @staticmethod
    def primary_key(name):
        return {
            "column_name": name,
            "constraint": "pk",
            "type": "serial",
            "reference_col": "",
            "reference_table": "",
            "null": 0,
            "unique": 1,
        }

    @staticmethod
    def string(name):
        return {
            "column_name": name,
            "constraint": "",
            "type": "varchar",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }

    @staticmethod
    def integer(name):
        return {
            "column_name": name,
            "constraint": "",
            "type": "integer",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }

    @staticmethod
    def date(name):
        return {
            "column_name": name,
            "constraint": "",
            "type": "varchar",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }

    @staticmethod
    def string(name):
        return {
            "column_name": name,
            "constraint": "",
            "type": "varchar",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }

    @staticmethod
    def foreign_key(col):
        col["constraint"] = "rk"
        return col

    @staticmethod
    def references(col, table, ref_key):
        col["reference_table"] = table
        col["reference_col"] = ref_key
        return col

    @staticmethod
    def unique(col):
        col["unique"] = 1
        return col

    @staticmethod
    def not_null(col):
        col["null"] = 0
        return col

    @classmethod
    def get_columns(cls):
        return [t["column_name"] for t in cls.schema]

    @classmethod
    def get_colunm_type(cls, column):
        for elmet in cls.schema:
            if elmet["column_name"] == column:
                return elmet["type"]

    def create(self):
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
                print(data)
            self.insert(data)
        except NameError as err:
            print("Une erreur est surmenu lors de la création  :\n :")

    @classmethod
    def insert(cls, data):
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
            print(data)
            cls.lk.executerReq(req, data)
        except Exception as err:
            print(f"Une erreur est surmenu lors de l'insertion :\n{req}\n :")
            return 0
        else:
            cls.lk.commit()
            print("INSERT SUCCESSFULY !!")
            return 1

    @classmethod
    def key(cls):
        req = ""
        try:
            req = f"SELECT max({cls.primary_key}) From {cls.relation};"
            # print(req)
            cls.lk.executerReq(req)
            print(req)
            key = cls.lk.resultatReq()[0][0]
        except Exception as err:
            print(f"Id fetch problem :\n{req}\n :")
            return 0
        else:
            print(key)
            return key

    @classmethod
    def select_attr_where_id(cls, attributes, matricule):
        req = ""
        try:
            sql = f"SELECT {attributes} FROM {cls.relation} WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"Select problem :\n{req}\n :")
            return 0
        else:
            if len(row) == 0:
                print("!!!   Désolé, aucune correspondance")
                return 0
            else:
                return row[0]

    @classmethod
    def select_attr(cls, attributes):
        req = ""
        try:
            sql = f"SELECT {attributes} FROM {cls.relation};"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"Select problem :\n{req}\n :")
            return 0
        else:
            return row

    @classmethod
    def select_all(cls):
        req = ""
        try:
            sql = f"SELECT * FROM {cls.relation};"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"Select problem :\n{req}\n :")
            return 0
        else:
            return row

    @classmethod
    def delete(cls, matricule):
        req = ""
        try:
            req = f"DELETE FROM {cls.relation} WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
        except Exception as err:
            print(f"Une erreur est surmenu lors de la suppressiond:\n{req}\n :")
            return 0
        else:
            cls.lk.commit()
            print("DELETED !!!")
            return 1

    @classmethod
    def update(cls, attribut, matricule, value):
        row = ""
        try:
            req = f"UPDATE  {cls.relation} SET {attribut} = '{value}' WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
            print(req)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la mise à jour de {attribut} : ID:{matricule}:\n{req}\n :"
            )
            return 0
        else:
            cls.lk.commit()
            print("UPDATED SUCCESSFULLY !!!")
            return 1


def main():
    Table.key()



if __name__ == "__main__":
    pass
