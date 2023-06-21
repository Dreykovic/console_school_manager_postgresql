from linker import Linker
from database import Database


class Migration(object):
    schema = [
        {
            "column_name": "id_classe",
            "constraint": "pk",
            "type": "serial",
            "reference_col": "",
            "reference_table": "",
            "null": 0,
            "unique": 1,
        },
        {
            "column_name": "nom",
            "constraint": "",
            "type": "varchar",
            "reference_col": "",
            "reference_table": "",
            "null": 0,
            "unique": 1,
        },
        {
            "column_name": "effectif",
            "constraint": "rk",
            "type": "integer",
            "reference_col": "go",
            "reference_table": "class",
            "null": 0,
            "unique": 1,
        },
    ]

    @staticmethod
    def create_tables(schema):
        req = ""
        primary_key_def = ""
        foreign_keys_definitions = ()
        foreign = ""
        relation = "test"

        req = f"CREATE TABLE {relation} ("
        for col in schema:
            req = (
                req
                + col["column_name"]
                + " "
                + col["type"]
                + (" NOT NULL" if not col["null"] else "")
                + (" UNIQUE ," if col["unique"] else ", ")
            )

            primary_key_def += (
                f"CONSTRAINT {col['column_name']}_pk PRIMARY KEY({col['column_name']}), "
                if col["constraint"] == "pk"
                else ""
            )
            foreign += (
                f"CONSTRAINT {col['column_name']}_fk FOREIGN KEY ({col['column_name']}) REFERENCES {col['reference_table']} ({col['reference_col']}), "
                if col["constraint"] == "rk"
                else ""
            )

            foreign_keys_definitions += (foreign,)
        req += primary_key_def
        req += "".join(foreign_def for foreign_def in foreign_keys_definitions)
        req = req[:-2] + ")"
        


def main():
    Migration.create_tables(Database.tables)


if __name__ == "__main__":
    main()
    pass
