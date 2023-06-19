import modeles
from validators import *


def ajouter():
    nom = input("Choisir : ")
    while not validate_text(nom):
        nom = input("Nom de l'élève : ")
    effectif = input("Prénom de l'élève : ")
    while not validate_number(effectif):
        effectif = input("Prénom de l'élève : ")
    eleve = {"nom": nom, "prénom": prenom}
    eleves.append(eleve)
    print(f"Élève {prenom} {nom} ajouté avec succès.")
def printer():
    print(f"1. 2nde A4")
    print(f"2. Znde D")
    print(f"3. 2nde C4")
    print(f"4. 1ere A4")
    print(f"5. 1ere D")
    print(f"6. 1ere C4")
    print(f"7. Tle A4")
    print(f"8. Tle D")
    print(f"9. Tle C4")

def ajouter():
    printer()    
    choix = input("Choisissez une option (1-9) : pour le nom de la classe")
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
        elif choix == "4":
            nom = "Tle A4"
            break
        elif choix == "5":
            nom = "Tle D"
            break
        elif choix == "6":
            nom = "Tle C4"
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
            printer()
            choix = input("Choisissez une option (1-9) pour le nom de la classe : ")
    effectif = input("Effectif de la classe : ")
    while not validate_number(effectif):
        effectif = input("Prénom de l'élève : ")


def supprimer_eleve():
    if len(eleves) == 0:
        print("Aucun élève à supprimer.")
        return

    print("Liste des élèves :")
    for i, eleve in enumerate(eleves):
        print(f"{i+1}. {eleve['prénom']} {eleve['nom']}")

    choix = int(input("Choisissez le numéro de l'élève à supprimer : "))
    if choix < 1 or choix > len(eleves):
        print("Choix invalide.")
        return

    eleve_supprime = eleves.pop(choix - 1)
    print(
        f"Élève {eleve_supprime['prénom']} {eleve_supprime['nom']} supprimé avec succès.")


def editer_eleve():
    if len(eleves) == 0:
        print("Aucun élève à éditer.")
        return

    print("Liste des élèves :")
    for i, eleve in enumerate(eleves):
        print(f"{i+1}. {eleve['prénom']} {eleve['nom']}")

    choix = int(input("Choisissez le numéro de l'élève à éditer : "))
    if choix < 1 or choix > len(eleves):
        print("Choix invalide.")
        return

    eleve = eleves[choix - 1]
    print(f"Édition de l'élève {eleve['prénom']} {eleve['nom']}")
    nouveau_nom = input("Nouveau nom : ")
    nouveau_prenom = input("Nouveau prénom : ")
    eleve["nom"] = nouveau_nom
    eleve["prénom"] = nouveau_prenom
    print("Élève modifié avec succès.")


eleves = []


def afficher_eleves():
    if not eleves:
        print("Aucun élève enregistré.")
        return

    print("===================================")
    print("           Liste des élèves         ")
    print("===================================")
    print("{:<10} {:<10} {:<15} {:<20} {:<10}".format(
        "Prénom", "Nom", "Contact", "Adresse", "Genre"))
    print("-----------------------------------")
    for eleve in eleves:
        prenom, nom, contact, adresse, genre = eleve
        print("{:<10} {:<10} {:<15} {:<20} {:<10}".format(
            prenom, nom, contact, adresse, genre))
    print("-----------------------------------")


def ajouter_eleve():
    nom = input("Nom de l'élève : ")
    prenom = input("Prénom de l'élève : ")
    contact = input("Contact de l'élève : ")
    adresse = input("Adresse de l'élève : ")
    genre = input("Genre de l'élève : ")
    eleve = (prenom, nom, contact, adresse, genre)
    eleves.append(eleve)
    print(f"Élève {prenom} {nom} ajouté avec succès.")

# Autres fonctions pour supprimer, éditer les élèves...


while True:
    print("===================================")
    print("          Gestion de l'école        ")
    print("===================================")
    print("1. Afficher les élèves")
    print("2. Ajouter un élève")
    print("3. Supprimer un élève")
    print("4. Éditer un élève")
    print("5. Quitter")

    choix = input("Choisissez une option (1-5) : ")

    if choix == "1":
        afficher_eleves()
    elif choix == "2":
        ajouter_eleve()
    elif choix == "3":
        supprimer_eleve()
    elif choix == "4":
        editer_eleve()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
