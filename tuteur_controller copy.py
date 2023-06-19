from modeles.table_classe import TableClasse as Classe
from controller.validators import *


def printer():
    print(f"M")
    print(f"F")

    
def ask_id():
    matricule = input("Id du tuteur :       ")
    while not validate_number(matricule):
        print("Saisie invalide. Veuillez saisir un text valide.")
        matricule = input("Id du tuteur :       ")
    matricule = int(matricule)
    return matricule

def ajouter():
    printer()
    choix = input(
        "Choisissez une option (1-9) : pour le nom de la classe       ")
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
                "Choisissez une option (1-9) pour le nom de la classe :       ")
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
    print(f"1. Editer le nom de la classe ")
    print(f"2. Editer l'effectif de la classe\n \n")
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
        "Choisissez une option (1-9) : pour le nouveau nom de la classe       ")
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
                "Choisissez une option (1-9) pour le nouveau nom de la classe :       ")

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
    classes = Classe.selectAttr('nom, effectif')
    if len(classes) == 0:
        print("Aucune classe enregistré.e")
        return

    print("======================================")
    print("            Liste des classes         ")
    print("======================================")
    print("            {:<10} | {:<10}             ".format(
          "Nom", "Éffectif",))
    print("--------------------------------------")
    for classe in classes:
        nom, effectif = classe
        print("            {:<10} | {:<10}             ".format(
            nom, effectif))
    print("--------------------------------------")

ajouter()
afficher()