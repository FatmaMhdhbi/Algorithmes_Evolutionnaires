
import random

capacites = [20, 15, 35, 40, 15, 15, 10]
intervalles = [80, 90, 65, 70]

possibilites = [
    ["1100", "0110", "0011"],
    ["1100", "0110", "0011"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"],
    ["1000", "0100", "0010", "0001"]
]

taille_population = 100
nb_generations = 300
pc = 0.8
pm = 0.1


def creer_individu():
    individu = []
    for i in range(7):
        gene = random.choice(possibilites[i])
        individu.append(gene)
    return individu


def calculer_reserves(individu):
    reserves = []

    for j in range(4):
        puissance_maintenance = 0

        for i in range(7):
            if individu[i][j] == "1":
                puissance_maintenance += capacites[i]

        reserve = 150 - puissance_maintenance - intervalles[j]
        reserves.append(reserve)

    return reserves


def fitness(individu):
    reserves = calculer_reserves(individu)

    if min(reserves) < 0:
        return 0

    return min(reserves)


def selection(population):
    candidats = random.sample(population, 3)
    return max(candidats, key=fitness)


def croisement(p1, p2):
    if random.random() < pc:
        point = random.randint(1, 6)

        enfant1 = p1[:point] + p2[point:]
        enfant2 = p2[:point] + p1[point:]

        return enfant1, enfant2

    return p1[:], p2[:]


def mutation(individu):
    if random.random() < pm:
        position = random.randint(0, 6)
        individu[position] = random.choice(possibilites[position])

    return individu


def algorithme_genetique():
    population = [creer_individu() for i in range(taille_population)]

    for generation in range(nb_generations):
        population.sort(key=fitness, reverse=True)

        nouvelle_population = population[:2]

        while len(nouvelle_population) < taille_population:
            p1 = selection(population)
            p2 = selection(population)

            enfant1, enfant2 = croisement(p1, p2)

            enfant1 = mutation(enfant1)
            enfant2 = mutation(enfant2)

            nouvelle_population.append(enfant1)

            if len(nouvelle_population) < taille_population:
                nouvelle_population.append(enfant2)

        population = nouvelle_population

    meilleur = max(population, key=fitness)
    return meilleur


solution = algorithme_genetique()

print("Meilleure solution :")

for i in range(7):
    print("Unite", i + 1, ":", solution[i])

print("\nReserves par intervalle :")

reserves = calculer_reserves(solution)

for i in range(4):
    print("Intervalle", i + 1, ":", reserves[i], "MW")

print("\nFitness :", fitness(solution), "MW")
