from controllers import *
def route_classe(choix):
    if choix == "1":
        show()
    elif choix == "2":
        ajouter_eleve()
    elif choix == "3":
        supprimer_eleve()
    elif choix == "4":
        editer_eleve()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")

print(dir())
