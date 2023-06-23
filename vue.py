from call import *
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
            action = call_eleve(choix)
            break
        elif table == "enseignant":
            action = call_enseignant(choix)
            break
        elif table == "classe":
            action = call_classe(choix)
            break
        elif table == "tuteur":
            action = call_tuteur(choix)
            break
        elif table == "programme":
            action = call_programme(choix)
            break
        elif table == "matiere":
            action = call_matiere(choix)
            break
        else:
            print("\nChoix invalide. Veuillez sélectionner une option valide.\n ")
