from linker import Linker


class Table(object):
    table = ''
    schema = []
    primary_key = ""

    lk = Linker()

    def create(self):
        data = tuple()
        try:
            for attr in self.__dict__:
                if attr == self.primary_key:
                    try:
                        self.__dict__[attr] = self.key() + 1
                    except TypeError:
                        self.__dict__[attr] = 1
                print(attr)
                print(self.__dict__[attr])
                data += (self.__dict__[attr],)
            self.insert(data)
        except NameError as err:
            print(f"Une erreur est surmenu lors de la création  :\n :")
            print(err)

    @classmethod
    def insert(cls, data):
        req = ''
        try:
            columns = '('
            for col in cls.schema:
                columns += ' ' + col[0] + ','
            columns = columns[:-1]+" )"
            column_number = len(cls.schema)
            values = '('
            values += ' %s, '*column_number
            values = values[:-2]+")"

            req = f"INSERT INTO {cls.table} {columns} VALUES {values};"
            cls.lk.executerReq(req, data)
        except Exception as err:
            print(f"Une erreur est surmenu lors de l'insertion :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1

    @classmethod
    def key(cls):
        req = ''
        try:
            for col in cls.schema:
                if col[1] == 'k':
                    pkey = col[0]
            req = f"SELECT max({pkey}) From {cls.table};"
            # print(req)
            cls.lk.executerReq(req)
            key = cls.lk.resultatReq()[0][0]
        except Exception as err:
            print(f"Id fetch problem :\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return key

    @classmethod
    def selectAttrWhereId(cls, attributes, matricule):
        try:
            sql = f"SELECT {attributes} FROM {cls.table} WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(sql)
            row = cls.lk.resultatReq()
        except Exception as err:
            print(f"Select problem :\n{req}\n :")
            print(err)
            return 0
        else:
            return row[0]

    @classmethod
    def delete(cls, matricule):
        try:
            req = f"DELETE FROM {cls.table} WHERE {cls.primary_key} = '{matricule}';"
            cls.lk.executerReq(req)
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la suppressiond:\n{req}\n :")
            print(err)
            return 0
        else:
            cls.lk.commit()
            return 1


def main():
    Table.key()

    # Table.insert(("2nde C4", 50))
if __name__ == '__main__':
    # main()
    pass
