from controllers import *

def route_classe(choix):
    if choix == "1":
        ClasseController.show()
    elif choix == "2":
        ClasseController.create()
    elif choix == "3":
        ClasseController.destroy()
    elif choix == "4":
        ClasseController.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix

