__all__ = ["PrimaryKey", "String", "Integer", "Date"]


class SchemaBuilder:
    col = dict()

    def unique(self):
        self.col["unique"] = 1
        return self

    def not_null(self):
        self.col["null"] = 0
        return self

    def foreign_key(self):
        self.col["constraint"] = "rk"
        return self

    def references(self, table, ref_key):
        self.col["reference_table"] = table
        self.col["reference_col"] = ref_key
        return self

    def build(self):
        return self.col


class String(SchemaBuilder):
    col = {
        "column_name": "",
        "constraint": "",
        "type": "varchar",
        "reference_col": "",
        "reference_table": "",
        "null": 1,
        "unique": 0,
    }

    def __init__(self, name):
        self.col["column_name"] = name




class PrimaryKey(SchemaBuilder):
    col = {
        "column_name": "",
        "constraint": "pk",
        "type": "serial",
        "reference_col": "",
        "reference_table": "",
        "null": 0,
        "unique": 1,
    }

    def __init__(self, name):
        self.col["column_name"] = name


class Integer(SchemaBuilder):
    col = {
        "column_name": "",
        "constraint": "",
        "type": "integer",
        "reference_col": "",
        "reference_table": "",
        "null": 1,
        "unique": 0,
    }

    def __init__(self, name):
        self.col["column_name"] = name





class Date(SchemaBuilder):
    col = {
        "column_name": "",
        "constraint": "",
        "type": "date",
        "reference_col": "",
        "reference_table": "",
        "null": 1,
        "unique": 0,
    }

    def __init__(self, name):
        self.col["column_name"] = name
