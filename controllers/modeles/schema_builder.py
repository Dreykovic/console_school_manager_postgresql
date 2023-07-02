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
    def __init__(self, name):
        self.col = {
            "column_name": name,
            "constraint": "",
            "type": "varchar",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }


class PrimaryKey(SchemaBuilder):
    def __init__(self, name):
        self.col = {
            "column_name": name,
            "constraint": "pk",
            "type": "serial",
            "reference_col": "",
            "reference_table": "",
            "null": 0,
            "unique": 1,
        }


class Integer(SchemaBuilder):
    def __init__(self, name):
        self.col = {
            "column_name": name,
            "constraint": "",
            "type": "integer",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }


class Date(SchemaBuilder):
    def __init__(self, name):
        self.col = {
            "column_name": name,
            "constraint": "",
            "type": "date",
            "reference_col": "",
            "reference_table": "",
            "null": 1,
            "unique": 0,
        }
