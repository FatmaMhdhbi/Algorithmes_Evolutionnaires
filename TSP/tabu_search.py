
import random
import math

villes = {
    "A": (0, 0),
    "B": (2, 6),
    "C": (5, 3),
    "D": (7, 8),
    "E": (8, 2),
    "F": (4, 9)
}

nb_iterations = 200
taille_tabou = 7


def distance(v1, v2):
    x1, y1 = villes[v1]
    x2, y2 = villes[v2]

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def distance_totale(trajet):
    total = 0

    for i in range(len(trajet)-1):
        total += distance(trajet[i], trajet[i+1])

    total += distance(trajet[-1], trajet[0])

    return total


def voisinage(trajet):
    voisins = []

    for i in range(len(trajet)):
        for j in range(i+1, len(trajet)):

            nouveau = trajet[:]

            nouveau[i], nouveau[j] = nouveau[j], nouveau[i]

            mouvement = tuple(sorted((trajet[i], trajet[j])))

            voisins.append((nouveau, mouvement))

    return voisins


def recherche_tabou():

    solution = list(villes.keys())
    random.shuffle(solution)

    meilleure_solution = solution[:]

    liste_tabou = []

    for iteration in range(nb_iterations):

        voisins = voisinage(solution)

        meilleur_voisin = None
        meilleur_mouvement = None
        meilleure_distance = float("inf")

        for voisin, mouvement in voisins:

            distance_actuelle = distance_totale(voisin)

            if (mouvement not in liste_tabou or
                distance_actuelle < distance_totale(meilleure_solution)):

                if distance_actuelle < meilleure_distance:

                    meilleur_voisin = voisin
                    meilleur_mouvement = mouvement
                    meilleure_distance = distance_actuelle

        if meilleur_voisin is None:
            break

        solution = meilleur_voisin

        liste_tabou.append(meilleur_mouvement)

        if len(liste_tabou) > taille_tabou:
            liste_tabou.pop(0)

        if distance_totale(solution) < distance_totale(meilleure_solution):

            meilleure_solution = solution[:]

        if iteration % 20 == 0:

            print("Iteration:", iteration,
                  "Distance:", round(distance_totale(solution), 2))

    return meilleure_solution


# Programme principal

meilleur = recherche_tabou()

print("\nMeilleur trajet:")

for ville in meilleur:
    print(ville, end=" -> ")

print(meilleur[0])

print("Distance totale:",
      round(distance_totale(meilleur), 2))
