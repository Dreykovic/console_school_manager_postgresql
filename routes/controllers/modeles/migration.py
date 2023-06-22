from .linker import Linker
from .database import tables


def create_tables(relation, schema):
    req = ""
    primary_key_def = ""
    foreign = ""
    count = 1
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
            f"CONSTRAINT {relation}_pk_{col['column_name']} PRIMARY KEY({col['column_name']}), "
            if col["constraint"] == "pk"
            else ""
        )
        foreign += (
            f"CONSTRAINT {relation}_fk_{col['column_name']}_{count} FOREIGN KEY ({col['column_name']}) REFERENCES {col['reference_table']} ({col['reference_col']}), "
            if col["constraint"] == "rk"
            else ""
        )
        count += 1

    req += primary_key_def
    req += foreign
    req = req[:-2] + ")"
    lk = Linker()
    lk.executerReq(req)
    lk.commit()
    lk.close()
    print(
        f"»»»»» Relation {relation.capitalize()} created successfully !!! ✔️   «««««\n\n"
    )


def main():
    for relation in tables:
        create_tables(relation, tables[relation])
        # print(relation)
        # print(tables[relation])   ûîðæþç789~~~###ðæ±þß


if __name__ == "__main__":
    main()
    pass
