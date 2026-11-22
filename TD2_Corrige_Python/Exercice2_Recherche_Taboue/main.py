
# Exercice 2 : Recherche Taboue
# Probleme de transport

COUTS = [
    [5, 3, 4],  # D1 -> M1, M2, M3
    [6, 7, 2]   # D2 -> M1, M2, M3
]

STOCKS = [8, 9]
DEMANDES = [4, 5, 8]


def cout_total(solution):
    """Calculer le cout total du transport."""
    total = 0

    for i in range(2):
        for j in range(3):
            total += solution[i][j] * COUTS[i][j]

    return total


def solution_valide(solution):
    """Verifier les contraintes du probleme."""

    # Verification des quantites positives
    for ligne in solution:
        for quantite in ligne:
            if quantite < 0:
                return False

    # Verification des stocks
    for i in range(2):
        if sum(solution[i]) != STOCKS[i]:
            return False

    # Verification des demandes
    for j in range(3):
        if solution[0][j] + solution[1][j] != DEMANDES[j]:
            return False

    return True


def generer_voisins(solution):
    """Generer les solutions voisines."""

    voisins = []

    for a in range(3):
        for b in range(3):

            if a == b:
                continue

            if solution[0][a] > 0 and solution[1][b] > 0:

                voisin = [ligne[:] for ligne in solution]

                voisin[0][a] -= 1
                voisin[1][a] += 1

                voisin[1][b] -= 1
                voisin[0][b] += 1

                if solution_valide(voisin):
                    mouvement = (a, b)
                    voisins.append((voisin, mouvement))

    return voisins


def recherche_taboue(solution_initiale, iterations=30, duree_tabu=4):

    solution_courante = [ligne[:] for ligne in solution_initiale]
    meilleure_solution = [ligne[:] for ligne in solution_initiale]

    liste_taboue = {}

    for iteration in range(iterations):

        candidats = []

        for voisin, mouvement in generer_voisins(solution_courante):

            valeur = cout_total(voisin)

            est_tabou = liste_taboue.get(mouvement, -1) > iteration

            # Critere d'aspiration
            if not est_tabou or valeur < cout_total(meilleure_solution):
                candidats.append((valeur, voisin, mouvement))

        if not candidats:
            break

        # Choisir le meilleur voisin
        candidats.sort(key=lambda x: x[0])

        valeur, solution_courante, mouvement = candidats[0]

        # Ajouter le mouvement inverse dans la liste taboue
        mouvement_inverse = (mouvement[1], mouvement[0])
        liste_taboue[mouvement_inverse] = iteration + duree_tabu

        # Mise a jour de la meilleure solution
        if valeur < cout_total(meilleure_solution):
            meilleure_solution = [ligne[:] for ligne in solution_courante]

    return meilleure_solution


# Programme principal
if __name__ == "__main__":

    solution_initiale = [
        [4, 4, 0],
        [0, 1, 8]
    ]

    print("===== SOLUTION INITIALE =====")

    for ligne in solution_initiale:
        print(ligne)

    print("Cout initial :", cout_total(solution_initiale))

    meilleure = recherche_taboue(solution_initiale)

    print("\n===== MEILLEURE SOLUTION =====")

    for i, ligne in enumerate(meilleure):
        print(f"D{i + 1} :", ligne)

    print("Cout total :", cout_total(meilleure))
    print("Solution valide :", solution_valide(meilleure))
