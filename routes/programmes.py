


def route_programme(Choix):
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
