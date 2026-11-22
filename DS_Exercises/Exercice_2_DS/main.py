
import random

n = 5
k = 10

taille_population = 100
nb_generations = 500
pc = 0.8
pm = 0.1


def creer_individu():
    individu = [0] * (n * n)

    positions = random.sample(range(n * n), k)

    for p in positions:
        individu[p] = 1

    return individu


def fitness(individu):
    score = 0

    # Verification des lignes
    for i in range(n):
        somme = 0

        for j in range(n):
            somme += individu[i * n + j]

        if somme % 2 == 0:
            score += 1

    # Verification des colonnes
    for j in range(n):
        somme = 0

        for i in range(n):
            somme += individu[i * n + j]

        if somme % 2 == 0:
            score += 1

    return score


def reparer(individu):
    while sum(individu) > k:
        p = random.choice([i for i in range(n*n) if individu[i] == 1])
        individu[p] = 0

    while sum(individu) < k:
        p = random.choice([i for i in range(n*n) if individu[i] == 0])
        individu[p] = 1

    return individu


def selection(population):
    candidats = random.sample(population, 3)
    return max(candidats, key=fitness)


def croisement(p1, p2):
    if random.random() < pc:
        point = random.randint(1, n*n-1)
        enfant = p1[:point] + p2[point:]
    else:
        enfant = p1[:]

    return reparer(enfant)


def mutation(individu):
    if random.random() < pm:
        pos1 = random.choice([i for i in range(n*n) if individu[i] == 1])
        pos0 = random.choice([i for i in range(n*n) if individu[i] == 0])

        individu[pos1] = 0
        individu[pos0] = 1

    return individu


def algorithme_genetique():
    population = [creer_individu() for i in range(taille_population)]

    for generation in range(nb_generations):

        population.sort(key=fitness, reverse=True)

        meilleur = population[0]

        if fitness(meilleur) == 2*n:
            print("Solution trouvee a la generation", generation)
            return meilleur

        nouvelle_population = population[:2]

        while len(nouvelle_population) < taille_population:

            p1 = selection(population)
            p2 = selection(population)

            enfant = croisement(p1, p2)
            enfant = mutation(enfant)

            nouvelle_population.append(enfant)

        population = nouvelle_population

    return max(population, key=fitness)


def afficher(individu):
    for i in range(n):
        for j in range(n):
            print(individu[i*n+j], end=" ")
        print()

    print("Nombre de jetons:", sum(individu))
    print("Fitness:", fitness(individu))


solution = algorithme_genetique()
afficher(solution)
