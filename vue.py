def vue(table):
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

    if table == "élève":
        route_eleve(choix)
    elif table == "enseignant":
        route_enseignant(choix)
    elif table == "classe":
        route_classe(choix)
    elif table == "tuteur":
        route_tuteur()
    elif table == "programme":
        route_programme(choix)
    elif table == "matiere":
        route_matiere(choix)
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
        
import routes

print(dir())

