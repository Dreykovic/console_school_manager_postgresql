from linker import Linker
from database import tables


def create_tables(relation, schema):
    req = ""
    primary_key_def = ""
    foreign_keys_definitions = ()
    foreign = ""

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
    for relation in tables:
        create_tables(relation, tables[relation])


if __name__ == "__main__":
    main()
    pass
