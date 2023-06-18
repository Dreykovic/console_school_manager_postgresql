
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
