from .controllers import *

def call_classe(choix):
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

def call_eleve(choix):
    if choix == "1":
        EleveController.show()
    elif choix == "2":
        EleveController.create()
    elif choix == "3":
        EleveController.destroy()
    elif choix == "4":
        EleveController.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix

def call_matiere(choix):
    if choix == "1":
        MatiereController.show()
    elif choix == "2":
        MatiereController.create()
    elif choix == "3":
        MatiereController.destroy()
    elif choix == "4":
        MatiereController.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix

def call_programme(choix):
    if choix == "1":
        ProgrammeController.show()
    elif choix == "2":
        ProgrammeController.create()
    elif choix == "3":
        ProgrammeController.destroy()
    elif choix == "4":
        ProgrammeController.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix


def call_enseignant(choix):
    if choix == "1":
        EnseignantController.show()
    elif choix == "2":
        EnseignantController.create()
    elif choix == "3":
        EnseignantController.destroy()
    elif choix == "4":
        EnseignantController.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix


def call_tuteur(choix):
    if choix == "1":
        Tuteur.show()
    elif choix == "2":
        Tuteur.create()
    elif choix == "3":
        Tuteur.destroy()
    elif choix == "4":
        Tuteur.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix