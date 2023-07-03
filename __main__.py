import pprint
import os
import sys
from vue import vue



def afficher_menu():
    print("===================================")
    print("          Gestion de l'école        ")
    print("===================================")
    pprint.pprint(
        {
            "1": "Manager élèves",
            "2": "Manager enseignants",
            "3": "Manager classes",
            "4": "Manager tuteurs",
            "5": "Manager matières",
            "6": "Manager programmes",
            "7": "Manager notes",
            "8": "Imprimer",
            "9": "Quitter",
        },
        indent=4,
    )


# Fonctions similaires pour les autres entités (classes, enseignants, tuteurs, matières, programmes)...

while True:
    afficher_menu()
    choix = input("Choisissez une option (1-9) : ")

    if choix == "1":
        vue("élève")
    elif choix == "2":
        vue("enseignant")
    elif choix == "3":
        vue("classe")
    elif choix == "4":
        vue("tuteur")
    elif choix == "5":
        vue("matière")
    elif choix == "6":
        vue("programme")
    elif choix == "7":
        print("Fonctionnalité indisponible")
    elif choix == "8":
        print("Fonctionnalité indisponible")
    elif choix == "9":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
