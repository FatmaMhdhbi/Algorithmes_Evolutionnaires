# TSP - Traveling Salesman Problem

## Description
Le problème du voyageur de commerce consiste à trouver le meilleur chemin permettant de visiter toutes les villes une seule fois et de revenir à la ville de départ.

L'objectif est de minimiser la distance totale parcourue.

## Représentation d'un individu
Chaque individu est représenté par une permutation des villes.

Exemple :
`A → C → B → D → E → F → A`

Chaque ville apparaît une seule fois dans le parcours.

## Algorithmes utilisés

### 1. Algorithme Génétique
- Population initiale de solutions.
- Sélection par tournoi.
- Croisement de type Order Crossover (OX).
- Mutation par échange de deux villes.
- Élitisme pour conserver les meilleures solutions.

### 2. Recherche Tabou
- Génération des voisins par échange de deux villes.
- Utilisation d'une liste tabou pour éviter de répéter les mêmes mouvements.
- Critère d'aspiration pour accepter une meilleure solution.

### 3. Recuit Simulé
- Génération d'une solution voisine par échange de deux villes.
- Acceptation des meilleures solutions.
- Acceptation possible d'une solution moins bonne selon la température.
- Diminution progressive de la température.

## Fonction objectif
La distance totale est calculée avec la distance euclidienne entre les villes.

L'objectif est de minimiser cette distance.

## Exécution

Pour lancer chaque algorithme :

```bash
python genetic_algorithm.py
```

```bash
python tabu_search.py
```

```bash
python simulated_annealing.py
```

## Fichiers
- `genetic_algorithm.py` : implémentation de l'algorithme génétique.
- `tabu_search.py` : implémentation de la recherche tabou.
- `simulated_annealing.py` : implémentation du recuit simulé.
