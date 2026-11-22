
import random

poids = [2, 3, 4, 5, 9, 7, 6, 1]
valeurs = [3, 4, 5, 8, 10, 7, 9, 2]

capacite = 15

nb_iterations = 200
taille_tabou = 7


def poids_total(solution):
    total = 0

    for i in range(len(solution)):
        if solution[i] == 1:
            total += poids[i]

    return total


def fitness(solution):
    total = 0

    for i in range(len(solution)):
        if solution[i] == 1:
            total += valeurs[i]

    if poids_total(solution) > capacite:
        return 0

    return total


def creer_solution():

    solution = [0] * len(poids)

    positions = list(range(len(poids)))
    random.shuffle(positions)

    total = 0

    for i in positions:
        if total + poids[i] <= capacite:
            solution[i] = 1
            total += poids[i]

    return solution


def voisinage(solution):

    voisins = []

    for i in range(len(solution)):

        voisin = solution[:]

        voisin[i] = 1 - voisin[i]

        if poids_total(voisin) <= capacite:
            voisins.append((voisin, i))

    return voisins


def recherche_tabou():

    solution = creer_solution()
    meilleure_solution = solution[:]

    liste_tabou = []

    for iteration in range(nb_iterations):

        voisins = voisinage(solution)

        meilleur_voisin = None
        meilleur_mouvement = None

        meilleure_valeur = -1

        for voisin, mouvement in voisins:

            valeur = fitness(voisin)

            if (mouvement not in liste_tabou or
                valeur > fitness(meilleure_solution)):

                if valeur > meilleure_valeur:

                    meilleur_voisin = voisin
                    meilleur_mouvement = mouvement
                    meilleure_valeur = valeur

        if meilleur_voisin is None:
            break

        solution = meilleur_voisin

        liste_tabou.append(meilleur_mouvement)

        if len(liste_tabou) > taille_tabou:
            liste_tabou.pop(0)

        if fitness(solution) > fitness(meilleure_solution):
            meilleure_solution = solution[:]

        if iteration % 20 == 0:
            print("Iteration:", iteration,
                  "Valeur:", fitness(solution))

    return meilleure_solution


# Programme principal

solution = recherche_tabou()

print("\nMeilleure solution:", solution)
print("Poids total:", poids_total(solution))
print("Valeur totale:", fitness(solution))
