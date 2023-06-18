from relations.linker import Linker
from database import Database


class Migration(object):
    @staticmethod
    def createTables(base):
        lk = Linker()
        try:
            # queries = list()
            for table in base:
                try:
                    req = f"CREATE TABLE {table} ("
                    pk = ''
                    reference_string = ''
                    pkey_string = ''
                    for prop in base[table]:
                        column = prop[0]
                        constrainte = prop[1]
                        column_type = prop[2]
                        ref_column = prop[3]
                        ref_table = prop[4]
                        if constrainte == 'k':
                            pk = column
                        if constrainte == "rf":
                            reference_string += f"CONSTRAINT {ref_column}_fk_{ref_table} FOREIGN KEY({column}) REFERENCES {ref_table}({ref_column}), "
                        req += f"{column} {column_type}, "
                    if pk != '':
                        pkey_string += f"CONSTRAINT {pk}_pk_{table} PRIMARY KEY({pk}), "
                        # print(pkey_string)
                        # print(column)
                    req += pkey_string + reference_string
                    req = req[:-2]+")"
                    # queries.append(req)
                    # print(req)
                    lk.executerReq(req)
                except Exception as err:
                    print(
                        f"Une erreur est surmenu lors de la création de la tables {table}:\n{req}\n :")
                    print(err)
                    return 0
                else:
                    lk.commit()
                    print(
                        f"        #---------Relalation {table} has been created !!\n \n")

            # return queries
        except Exception as err:
            print(
                f"Une erreur est surmenu lors de la création des tables :\n{req}\n :")
            print(err)
            return 0
        else:
            lk.close()
            print('        #---------Relations created successfully !!')
            return 1


def main():
    Migration.createTables(Database.tables)

    # ,{TableNiveauSerie.table: TableNiveauSerie.schema}
    #     TableClasse.table: TableClasse.schema,
    #     TableTuteur.table: TableTuteur.schema,
    #     TableEleve.table: TableEleve.schema,
    #     TableEnseignant.table: TableEnseignant.schema,
    #     TableMatiere.table: TableMatiere.schema,
    #     TableProgramme.table: TableProgramme.schema
if __name__ == '__main__':
    main()
    pass
