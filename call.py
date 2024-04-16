from modeles import *
from controllers.classe_controller import ClasseController
from controllers.eleve_controller import EleveController
from controllers.enseignant_controller import EnseignantController
from controllers.tuteur_controller import TuteurController
from controllers.programme_controller import ProgrammeController
from controllers.matiere_controller import MatiereController

from modeles.table_eleve import TableEleve as Eleve
from modeles.table_classe import TableClasse as Classe
from modeles.table_tuteur import TableTuteur as Tuteur
from modeles.table_tuteur import TableTuteur as Matiere
from modeles.table_tuteur import TableTuteur as Enseignant
from modeles.table_tuteur import TableTuteur as Programme
def call_classe(choix):
    if choix == "1":
        ClasseController.show(Classe) 
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
        EleveController.show(Eleve)
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
        MatiereController.show(Matiere)
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
        ProgrammeController.show(Programme)
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
        EnseignantController.show(Enseignant)
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
        TuteurController.show(Tuteur)
    elif choix == "2":
        TuteurController.create()
    elif choix == "3":
        TuteurController.destroy()
    elif choix == "4":
        TuteurController.update()
    elif choix == "5":
        print("Au revoir !")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
    return choix