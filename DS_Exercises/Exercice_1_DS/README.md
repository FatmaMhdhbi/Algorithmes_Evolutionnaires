# Exercice 1 : Robot dans un labyrinthe

## Description
Dans cet exercice, on utilise un algorithme génétique pour trouver un chemin permettant à un robot de sortir d'un labyrinthe.

Le robot commence à la position `(1,1)` et doit atteindre la sortie située à `(10,10)`.

## Représentation d'un individu
Chaque individu représente une suite de mouvements du robot.

- 0 : Haut
- 1 : Bas
- 2 : Gauche
- 3 : Droite

## Fonction Fitness
La fonction Fitness évalue la qualité du chemin parcouru par le robot.

Elle prend en considération la distance entre la position finale du robot et la sortie.

## Opérations génétiques
- **Sélection :** sélection par tournoi.
- **Croisement :** croisement en un point.
- **Mutation :** modification aléatoire d'un mouvement.
- **Élitisme :** conservation des meilleurs individus.

## Exécution
Pour lancer le programme :

```bash
python main.py
```

## Fichier
- `main.py` : contient l'implémentation de l'algorithme génétique.
