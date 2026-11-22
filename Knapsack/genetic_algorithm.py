
import random

# Donnees du probleme

poids = [2, 3, 4, 5, 9, 7, 6, 1]
valeurs = [3, 4, 5, 8, 10, 7, 9, 2]

capacite = 15

taille_population = 50
nb_generations = 200
pc = 0.8
pm = 0.1


# Creation d'un individu

def creer_individu():
    individu = [0] * len(poids)

    positions = list(range(len(poids)))
    random.shuffle(positions)

    poids_total = 0

    for i in positions:
        if poids_total + poids[i] <= capacite:
            individu[i] = 1
            poids_total += poids[i]

    return individu


# Calcul du poids total

def poids_total(individu):
    total = 0

    for i in range(len(individu)):
        if individu[i] == 1:
            total += poids[i]

    return total


# Calcul de la valeur totale

def fitness(individu):
    total = 0

    for i in range(len(individu)):
        if individu[i] == 1:
            total += valeurs[i]

    if poids_total(individu) > capacite:
        return 0

    return total


# Reparation d'un individu

def reparer(individu):
    while poids_total(individu) > capacite:

        objets = [i for i in range(len(individu))
                  if individu[i] == 1]

        i = random.choice(objets)
        individu[i] = 0

    return individu


# Selection par tournoi

def selection(population):
    candidats = random.sample(population, 3)
    return max(candidats, key=fitness)


# Croisement en un point

def croisement(p1, p2):

    if random.random() < pc:

        point = random.randint(1, len(p1)-1)

        enfant = p1[:point] + p2[point:]

    else:
        enfant = p1[:]

    return reparer(enfant)


# Mutation

def mutation(individu):

    for i in range(len(individu)):

        if random.random() < pm:
            individu[i] = 1 - individu[i]

    return reparer(individu)


# Algorithme genetique

def algorithme_genetique():

    population = [creer_individu()
                  for i in range(taille_population)]

    for generation in range(nb_generations):

        population.sort(key=fitness, reverse=True)

        meilleur = population[0]

        if generation % 20 == 0:
            print("Generation:", generation,
                  "Valeur:", fitness(meilleur))

        nouvelle_population = population[:2]

        while len(nouvelle_population) < taille_population:

            p1 = selection(population)
            p2 = selection(population)

            enfant = croisement(p1, p2)
            enfant = mutation(enfant)

            nouvelle_population.append(enfant)

        population = nouvelle_population

    return max(population, key=fitness)


# Programme principal

solution = algorithme_genetique()

print("\nMeilleure solution:", solution)
print("Poids total:", poids_total(solution))
print("Valeur totale:", fitness(solution))
