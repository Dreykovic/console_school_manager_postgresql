from modeles.table_classe import TableClasse as Classe
from validators import *


def printer():
    print("1. 2nde A4")
    print("2. Znde D")
    print("3. 2nde C4")
    print("4. 1ere A4")
    print("5. 1ere D")
    print("6. 1ere C4")
    print("7. Tle A4")
    print("8. Tle D")
    print("9. Tle C4\n \n")


def ask_id():
    id_cls = input("Id de la classe :       ")
    while not validate_number(id_cls):
        print("Saisie invalide. Veuillez saisir un text valide.")
        id_cls = input("Id de la classe :       ")
    id_cls = int(id_cls)
    return id_cls


def ajouter():
    printer()
    choix = input("Choisissez une option (1-9) : pour le nom de la classe       ")
    while True:
        if choix == "1":
            nom = "2nde A4"
            break
        elif choix == "2":
            nom = "2nde D"
            break
        elif choix == "3":
            nom = "2nde C4"
            break
        elif choix == "4":
            nom = "1ere A4"
            break
        elif choix == "5":
            nom = "1ere D"
            break
        elif choix == "6":
            nom = "1ere C4"
            break
        elif choix == "7":
            nom = "Tle A4"
            break
        elif choix == "8":
            nom = "Tle D"
            break
        elif choix == "9":
            nom = "Tle C4"
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            printer()
            choix = input(
                "Choisissez une option (1-9) pour le nom de la classe :       "
            )
    effectif = input("Effectif de la classe :       ")
    while not validate_number(effectif):
        print("Saisie invalide. Veuillez saisir un text valide.")
        effectif = input("Effectif de la classe :       ")
    effectif = int(effectif)
    uneclasse = Classe(nom, effectif)
    uneclasse.create()


def supprimer():
    Classe.delete(ask_id())


def editer():
    print("1. Editer le nom de la classe ")
    print("2. Editer l'effectif de la classe\n \n")
    choix = input("Choisissez une option (1-2)  :       ")
    while True:
        if choix == "1":
            editerNom()
            break
        elif choix == "2":
            editerEffectif()
            break

        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            printer()
            choix = input("Choisissez une option (1-2)  :       ")


def editerNom():
    printer()
    choix = input(
        "Choisissez une option (1-9) : pour le nouveau nom de la classe       "
    )
    while True:
        if choix == "1":
            nom = "2nde A4"
            break
        elif choix == "2":
            nom = "2nde D"
            break
        elif choix == "3":
            nom = "2nde C4"
            break
        elif choix == "4":
            nom = "1ere A4"
            break
        elif choix == "5":
            nom = "1ere D"
            break
        elif choix == "6":
            nom = "1ere C4"
            break
        elif choix == "7":
            nom = "Tle A4"
            break
        elif choix == "8":
            nom = "Tle D"
            break
        elif choix == "9":
            nom = "Tle C4"
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            printer()
            choix = input(
                "Choisissez une option (1-9) pour le nouveau nom de la classe :       "
            )

    Classe.updateNom(ask_id(), nom)


def editerEffectif():
    effectif = input("Nouvel effectif de la classe :       ")
    while not validate_number(effectif):
        print("Saisie invalide. Veuillez saisir un text valide.")
        effectif = input("Nouvel effectif de la classe :       ")
    effectif = int(effectif)
    Classe.updateEffectif(ask_id(), effectif)


def supprimer():
    Classe.delete(ask_id())

def afficher():
    classes = Classe.select_all()
    table_name = 'classe'.capitalize()

    if len(classes) == 0:
        print(f"Rien de '{table_name}' enregistré")
        return

    columns = Classe.get_columns()  # Obtient les noms des colonnes de la table
    column_widths = [10] * len(columns)  # Largeur fixe de chaque colonne (20 caractères)

    print("=" * (sum(column_widths) + 3 * len(columns) + 1))
    print(f"{'Liste des ' + table_name + 's':^{sum(column_widths) + 3 * len(columns) + 1}}")
    print("=" * (sum(column_widths) + 3 * len(columns) + 1))

    # Affichage des en-têtes des colonnes
    header_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
    print(header_format.format(*columns))

    # Affichage des séparateurs horizontaux
    separator = "-" * (sum(column_widths) + 3 * len(columns) + 1)
    print(separator)

    # Affichage des lignes de données
    for classe in classes:
        row_format = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        print(row_format.format(*classe))

    print(separator)

# ajouter()
afficher()













