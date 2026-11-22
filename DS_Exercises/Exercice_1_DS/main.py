
import random

# Labyrinthe : 0 = case libre, 1 = mur

labyrinthe = [
    [0,1,0,0,1,0,0,0,0,0],
    [0,1,0,0,1,0,1,1,1,1],
    [0,0,0,0,1,0,1,0,1,0],
    [1,1,1,0,1,0,1,0,1,0],
    [0,0,0,0,0,0,1,0,1,0],
    [0,0,1,1,1,0,1,0,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,0,1,0,1,0,0,1,0],
    [0,1,0,1,0,1,0,1,1,1],
    [0,1,0,1,0,1,0,0,0,0]
]

depart = (0, 0)
sortie = (9, 9)

# 0: Haut, 1: Bas, 2: Gauche, 3: Droite

directions = {
    0: (-1, 0),
    1: (1, 0),
    2: (0, -1),
    3: (0, 1)
}

# Parametres de l'algorithme genetique

TAILLE_POP = 100
TAILLE_CHROMOSOME = 30
GENERATIONS = 1000
PC = 0.8
PM = 0.05


# Evaluation d'un individu

def fitness(individu):

    position = depart
    visites = [depart]

    for gene in individu:

        dx, dy = directions[gene]

        x = position[0] + dx
        y = position[1] + dy

        # Verifier les limites
        if x < 0 or x >= 10 or y < 0 or y >= 10:
            break

        # Verifier les murs
        if labyrinthe[x][y] == 1:
            break

        # Verifier les cases deja visitees
        if (x, y) in visites:
            break

        position = (x, y)
        visites.append(position)

        # Verifier si le robot atteint la sortie
        if position == sortie:
            return 1000 - len(visites), True, visites

    # Calculer la distance jusqu'a la sortie
    distance = abs(position[0] - sortie[0]) + abs(position[1] - sortie[1])

    score = -10 * distance + len(visites)

    return score, False, visites


# Creation d'un individu

def creer_individu():

    return [random.randint(0, 3)
            for i in range(TAILLE_CHROMOSOME)]


# Creation de la population initiale

def creer_population():

    population = []

    for i in range(TAILLE_POP):
        population.append(creer_individu())

    return population


# Selection par tournoi

def selection(population):

    candidats = random.sample(population, 3)

    meilleur = max(candidats, key=lambda x: fitness(x)[0])

    return meilleur


# Croisement en un point

def croisement(parent1, parent2):

    if random.random() < PC:

        point = random.randint(1, TAILLE_CHROMOSOME - 1)

        enfant = parent1[:point] + parent2[point:]

    else:
        enfant = parent1[:]

    return enfant


# Mutation

def mutation(individu):

    for i in range(TAILLE_CHROMOSOME):

        if random.random() < PM:
            individu[i] = random.randint(0, 3)

    return individu


# Algorithme genetique

def algorithme_genetique():

    population = creer_population()

    for generation in range(GENERATIONS):

        population.sort(
            key=lambda x: fitness(x)[0],
            reverse=True
        )

        meilleur = population[0]

        score, atteint, visites = fitness(meilleur)

        if generation % 50 == 0:
            print("Generation:", generation,
                  " Fitness:", score)

        if atteint:
            print("\nSortie trouvee !")
            print("Generation:", generation)
            return meilleur

        nouvelle_population = population[:2]

        while len(nouvelle_population) < TAILLE_POP:

            parent1 = selection(population)
            parent2 = selection(population)

            enfant = croisement(parent1, parent2)

            enfant = mutation(enfant)

            nouvelle_population.append(enfant)

        population = nouvelle_population

    population.sort(
        key=lambda x: fitness(x)[0],
        reverse=True
    )

    return population[0]


# Affichage du resultat

def afficher_resultat(individu):

    score, atteint, visites = fitness(individu)

    print("\nScore:", score)
    print("Sortie atteinte:", atteint)
    print("Nombre de cases visitees:", len(visites))

    for i in range(10):

        for j in range(10):

            if (i, j) == depart:
                print("S", end=" ")

            elif (i, j) == sortie:
                print("E", end=" ")

            elif labyrinthe[i][j] == 1:
                print("#", end=" ")

            elif (i, j) in visites:
                print("*", end=" ")

            else:
                print(".", end=" ")

        print()


# Execution du programme

meilleur = algorithme_genetique()

afficher_resultat(meilleur)
