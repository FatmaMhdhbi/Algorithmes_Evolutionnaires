# Knapsack Problem

## Description
Le problème du sac à dos consiste à choisir un ensemble d'objets à placer dans un sac ayant une capacité limitée.

Chaque objet possède un poids et une valeur.

L'objectif est de maximiser la valeur totale des objets sans dépasser la capacité du sac.

## Représentation d'un individu
Chaque individu est représenté par un chromosome binaire.

- 1 : l'objet est sélectionné.
- 0 : l'objet n'est pas sélectionné.

Exemple :
`[1, 0, 1, 1, 0, 0, 1, 0]`

## Fonction Fitness
La fonction Fitness calcule la valeur totale des objets sélectionnés.

Si le poids total dépasse la capacité du sac, la solution n'est pas valide et sa Fitness est égale à 0.

## Algorithmes utilisés

### 1. Algorithme Génétique
- Création d'une population initiale.
- Sélection par tournoi.
- Croisement en un point.
- Mutation binaire.
- Réparation des solutions qui dépassent la capacité.
- Élitisme pour conserver les meilleurs individus.

### 2. Recherche Tabou
- Génération des voisins en modifiant un objet.
- Utilisation d'une liste tabou pour éviter les mouvements récents.
- Critère d'aspiration pour accepter une meilleure solution.

### 3. Recuit Simulé
- Génération d'une solution voisine.
- Acceptation des meilleures solutions.
- Possibilité d'accepter une solution moins bonne selon la température.
- Refroidissement progressif.

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
