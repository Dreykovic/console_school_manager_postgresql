from table import Table

# from linker import linker


class TableClasse(Table):
    relation = "classe"
    schema = [
        Table.primary_key("id_classe"),
        Table.not_null(Table.string("nom")),
        Table.not_null(Table.integer("effectif")),
    ]

    primary_key = "id_classe"

    def __init__(self, nom=None, effectif=0):
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif


def main():
    print(TableClasse.schema)
    a=[t['column_name'] for t in TableClasse.schema]
    print(00000)
    print(a)


if __name__ == "__main__":
    main()
    print("5555")
    pass

