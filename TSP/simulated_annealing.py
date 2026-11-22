
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

temperature = 1000
temperature_min = 0.01
alpha = 0.995


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


def voisin(trajet):

    nouveau = trajet[:]

    i, j = random.sample(range(len(nouveau)), 2)

    nouveau[i], nouveau[j] = nouveau[j], nouveau[i]

    return nouveau


def recuit_simule():

    solution = list(villes.keys())
    random.shuffle(solution)

    meilleure_solution = solution[:]

    t = temperature
    iteration = 0

    while t > temperature_min:

        nouvelle_solution = voisin(solution)

        distance_actuelle = distance_totale(solution)
        nouvelle_distance = distance_totale(nouvelle_solution)

        delta = nouvelle_distance - distance_actuelle

        if delta < 0:
            solution = nouvelle_solution

        else:
            probabilite = math.exp(-delta / t)

            if random.random() < probabilite:
                solution = nouvelle_solution

        if distance_totale(solution) < distance_totale(meilleure_solution):
            meilleure_solution = solution[:]

        if iteration % 500 == 0:
            print("Iteration:", iteration,
                  "Distance:", round(distance_totale(solution), 2),
                  "Temperature:", round(t, 2))

        t = t * alpha
        iteration += 1

    return meilleure_solution


# Programme principal

meilleur = recuit_simule()

print("\nMeilleur trajet:")

for ville in meilleur:
    print(ville, end=" -> ")

print(meilleur[0])

print("Distance totale:",
      round(distance_totale(meilleur), 2))
