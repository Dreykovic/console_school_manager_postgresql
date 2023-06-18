
while True:
    print("===================================")
    print("              Matières             ")
    print("===================================")
    print("1. Afficher les Matières")
    print("2. Ajouter un Matières")
    print("3. Supprimer un Matières")
    print("4. Éditer un Matières")
    print("5. Menu principal")
    print("6. Quitter")

    choix = input("Choisissez une option (1-6) : ")

    if choix == "1":
        afficher_eleves()
    elif choix == "2":
        ajouter_eleve()
    elif choix == "3":
        supprimer_eleve()
    elif choix == "4":
        editer_eleve()
    elif choix == "4":
        editer_eleve()
    elif choix == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
