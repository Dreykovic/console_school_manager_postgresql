def vue(table):
    action = ""
    while action is not "5":
        print("==========================================================")
        print(f"                      {table.capitalize}                     ")
        print("==========================================================")
        print(f"1. Afficher les {table}s")
        print(f"2. Ajouter un {table}")
        print(f"3. Supprimer un {table}")
        print(f"4. Éditer un {table}")
        print(f"5. Menu principale")
        print(f"[ctrl+c]. Quitter")

        choix = input("Choisissez une option (1-5) : ")
        action = ""
        if table == "élève":
            action = route_eleve(choix)
            break
        elif table == "enseignant":
            action = route_enseignant(choix)
            break
        elif table == "classe":
            action = route_classe(choix)
            break
        elif table == "tuteur":
            action = route_tuteur()
            break
        elif table == "programme":
            action = route_programme(choix)
            break
        elif table == "matiere":
            action = route_matiere(choix)
            break
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.\n ")
