from table import Table


class TableClasse(Table):
    relation = "classe"
    schema = [
        ("id_classe", "k", "serial", "", ""),
        ("nom", "", "varchar", "", ""),
        ("effectif", "", "integer", "", ""),
    ]
    schema = [{
        'column_name': 'id_classe',
        'constraint': 'pk',
        'type': 'serial',
        'reference_col': '',
        'reference_table': ''
    }, {
        'column_name': 'nom',
        'constraint': '',
        'type': 'varchar',
        'reference_col': '',
        'reference_table': ''
    }, {
        'column_name': 'effectif',
        'constraint': '',
        'type': 'integer',
        'reference_col': '',
        'reference_table': ''
    }]
    primary_key = "id_classe"

    def __init__(self, nom=None, effectif=0):
        self.id_classe = 0
        self.nom = nom
        self.effectif = effectif


def main():
    tut = TableClasse("Dosseh")
    tut.create()


if __name__ == "__main__":
    main()
    print("5555")
    pass
