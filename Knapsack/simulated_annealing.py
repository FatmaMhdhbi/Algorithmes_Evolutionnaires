
import random
import math

poids = [2, 3, 4, 5, 9, 7, 6, 1]
valeurs = [3, 4, 5, 8, 10, 7, 9, 2]

capacite = 15

temperature = 1000
temperature_min = 0.01
alpha = 0.995


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


def voisin(solution):

    nouveau = solution[:]

    i = random.randint(0, len(solution)-1)

    nouveau[i] = 1 - nouveau[i]

    return nouveau


def recuit_simule():

    solution = creer_solution()
    meilleure_solution = solution[:]

    t = temperature
    iteration = 0

    while t > temperature_min:

        nouvelle_solution = voisin(solution)

        if poids_total(nouvelle_solution) <= capacite:

            delta = fitness(nouvelle_solution) - fitness(solution)

            if delta > 0:
                solution = nouvelle_solution

            else:
                probabilite = math.exp(delta / t)

                if random.random() < probabilite:
                    solution = nouvelle_solution

        if fitness(solution) > fitness(meilleure_solution):
            meilleure_solution = solution[:]

        if iteration % 500 == 0:
            print("Iteration:", iteration,
                  "Valeur:", fitness(solution),
                  "Temperature:", round(t, 2))

        t = t * alpha
        iteration += 1

    return meilleure_solution


# Programme principal

solution = recuit_simule()

print("\nMeilleure solution:", solution)
print("Poids total:", poids_total(solution))
print("Valeur totale:", fitness(solution))
