# Exercice 2 : Placement de jetons

## Description
Dans cet exercice, on utilise un algorithme génétique pour placer 10 jetons dans une grille de taille 5 × 5.

L'objectif est de respecter les contraintes suivantes :
- Chaque ligne doit contenir un nombre pair de jetons.
- Chaque colonne doit contenir un nombre pair de jetons.
- Le nombre total de jetons doit être égal à 10.

## Représentation d'un individu
Chaque individu est représenté par un chromosome binaire de 25 bits.

- 1 : présence d'un jeton.
- 0 : absence d'un jeton.

## Fonction Fitness
La fonction Fitness compte le nombre de lignes et de colonnes qui contiennent un nombre pair de jetons.

La valeur maximale est 10 (5 lignes + 5 colonnes).

## Opérations génétiques
- **Sélection :** sélection par tournoi.
- **Croisement :** croisement en un point.
- **Mutation :** échange de deux positions.
- **Réparation :** ajuste le nombre de jetons pour garder exactement 10 jetons.
- **Élitisme :** conservation des meilleurs individus.

## Exécution
Pour lancer le programme :

```bash
python main.py
```

## Fichier
- `main.py` : contient l'implémentation de l'algorithme génétique.
