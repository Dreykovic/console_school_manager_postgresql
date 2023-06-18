
while True:
    print("===================================")
    print("            Enseignants            ")
    print("===================================")
    print("1. Afficher les enseignats")
    print("2. Ajouter un enseignant")
    print("3. Supprimer un enseignant")
    print("4. Éditer un enseignant")
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
    elif choix == "6":
        print("Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
