
import random
import math

# Les villes
villes = {
    "A": (0, 0),
    "B": (2, 6),
    "C": (5, 3),
    "D": (7, 8),
    "E": (8, 2),
    "F": (4, 9)
}

taille_population = 50
nb_generations = 200
pc = 0.8
pm = 0.1


# Calcul de la distance entre deux villes

def distance(v1, v2):
    x1, y1 = villes[v1]
    x2, y2 = villes[v2]

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


# Calcul de la distance totale du trajet

def distance_totale(individu):
    total = 0

    for i in range(len(individu)-1):
        total += distance(individu[i], individu[i+1])

    total += distance(individu[-1], individu[0])

    return total


# Fonction fitness

def fitness(individu):
    return 1 / distance_totale(individu)


# Creation d'un individu

def creer_individu():
    individu = list(villes.keys())
    random.shuffle(individu)
    return individu


# Creation de la population

def creer_population():
    return [creer_individu() for i in range(taille_population)]


# Selection par tournoi

def selection(population):
    candidats = random.sample(population, 3)
    return max(candidats, key=fitness)


# Croisement (Order Crossover)

def croisement(p1, p2):

    if random.random() < pc:

        debut, fin = sorted(random.sample(range(len(p1)), 2))

        enfant = [None] * len(p1)

        enfant[debut:fin+1] = p1[debut:fin+1]

        position = (fin + 1) % len(p1)

        for ville in p2:
            if ville not in enfant:

                enfant[position] = ville
                position = (position + 1) % len(p1)

        return enfant

    return p1[:]


# Mutation par echange

def mutation(individu):

    if random.random() < pm:

        i, j = random.sample(range(len(individu)), 2)

        individu[i], individu[j] = individu[j], individu[i]

    return individu


# Algorithme genetique

def algorithme_genetique():

    population = creer_population()

    for generation in range(nb_generations):

        population.sort(key=fitness, reverse=True)

        meilleur = population[0]

        if generation % 20 == 0:
            print("Generation:", generation,
                  "Distance:", round(distance_totale(meilleur), 2))

        nouvelle_population = population[:2]

        while len(nouvelle_population) < taille_population:

            p1 = selection(population)
            p2 = selection(population)

            enfant = croisement(p1, p2)

            enfant = mutation(enfant)

            nouvelle_population.append(enfant)

        population = nouvelle_population

    meilleur = max(population, key=fitness)

    return meilleur


# Programme principal

meilleur = algorithme_genetique()

print("\nMeilleur trajet:")

for ville in meilleur:
    print(ville, end=" -> ")

print(meilleur[0])

print("Distance totale:",
      round(distance_totale(meilleur), 2)