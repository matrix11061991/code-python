def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 9)

def verifier_victoire(plateau, symbole):
    # Vérifier les lignes et les colonnes
    for i in range(4):
        if all(plateau[i][j] == symbole for j in range(4)) or all(plateau[j][i] == symbole for j in range(4)):
            return True

    # Vérifier les diagonales
    if all(plateau[i][i] == symbole for i in range(4)) or all(plateau[i][3 - i] == symbole for i in range(4)):
        return True

    return False

def jouer_tic_tac_toe():
    plateau = [[" " for _ in range(4)] for _ in range(4)]
    tour = 0
    symboles = ["X", "O"]

    while True:
        afficher_plateau(plateau)
        joueur = tour % 2
        symbole = symboles[joueur]

        try:
            ligne = int(input(f"Joueur {joueur + 1}, entrez le numéro de ligne (1-4): ")) - 1
            colonne = int(input(f"Joueur {joueur + 1}, entrez le numéro de colonne (1-4): ")) - 1
        except ValueError:
            print("Veuillez entrer des nombres valides.")
            continue

        if 0 <= ligne < 4 and 0 <= colonne < 4 and plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = symbole
            tour += 1

            if tour >= 5 and verifier_victoire(plateau, symbole):
                afficher_plateau(plateau)
                print(f"Le joueur {joueur + 1} ({symbole}) remporte la partie!")
                break
            elif tour == 16:
                afficher_plateau(plateau)
                print("La partie est un match nul!")
                break
        else:
            print("Coup invalide. Veuillez réessayer.")

if __name__ == "__main__":
    jouer_tic_tac_toe()
