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


def foreign_key(col):
    col["constraint"] = "rk"
    return col


def references(col, table, ref_key):
    col["reference_table"] = table
    col["reference_col"] = ref_key
    return col


def unique(col):
    col["unique"] = 1
    return col


def not_null(col):
    col["null"] = 0
    return col


# @staticmethod
# def primary_key(name):
#     return {
#         "column_name": name,
#         "constraint": "pk",
#         "type": "serial",
#         "reference_col": "",
#         "reference_table": "",
#         "null": 0,
#         "unique": 1,
#     }

# @staticmethod
# def string(name):
#     return {
#         "column_name": name,
#         "constraint": "",
#         "type": "varchar",
#         "reference_col": "",
#         "reference_table": "",
#         "null": 1,
#         "unique": 0,
#     }

# @staticmethod
# def integer(name):
#     return {
#         "column_name": name,
#         "constraint": "",
#         "type": "integer",
#         "reference_col": "",
#         "reference_table": "",
#         "null": 1,
#         "unique": 0,
#     }

# @staticmethod
# def date(name):
#     return {
#         "column_name": name,
#         "constraint": "",
#         "type": "varchar",
#         "reference_col": "",
#         "reference_table": "",
#         "null": 1,
#         "unique": 0,
#     }

# @staticmethod
# def string(name):
#     return {
#         "column_name": name,
#         "constraint": "",
#         "type": "varchar",
#         "reference_col": "",
#         "reference_table": "",
#         "null": 1,
#         "unique": 0,
#     }

# @staticmethod
# def foreign_key(col):
#     col["constraint"] = "rk"
#     return col

# @staticmethod
# def references(col, table, ref_key):
#     col["reference_table"] = table
#     col["reference_col"] = ref_key
#     return col

# @staticmethod
# def unique(col):
#     col["unique"] = 1
#     return col

# @staticmethod
# def not_null(col):
#     col["null"] = 0
#     return col
