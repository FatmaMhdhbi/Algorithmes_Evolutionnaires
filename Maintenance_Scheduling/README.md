# Maintenance Scheduling - Centrales Electriques

## Description
Le problème consiste à organiser les périodes de maintenance de 7 centrales électriques pendant une année divisée en 4 intervalles.

L'objectif est de maximiser la réserve de puissance disponible pendant chaque intervalle.

## Données du problème
- Nombre de centrales : 7
- Nombre d'intervalles : 4
- Capacités des centrales : 20, 15, 35, 40, 15, 15 et 10 MW
- Demande en puissance : 80, 90, 65 et 70 MW

## Représentation d'un individu
Chaque centrale est représentée par un gène de 4 bits.

- 1 : la centrale est en maintenance.
- 0 : la centrale fonctionne normalement.

Un individu contient donc 7 gènes de 4 bits.

## Fonction Fitness
La réserve est calculée par :

Réserve = Capacité totale - Puissance en maintenance - Demande

La Fitness correspond à la plus petite réserve parmi les 4 intervalles.

Si une réserve est négative, la Fitness est égale à 0.

L'objectif est de maximiser cette Fitness.

## Opérations génétiques
- **Sélection :** sélection par tournoi.
- **Croisement :** croisement en un point entre les blocs de 4 bits.
- **Mutation :** remplacement d'un gène par une possibilité autorisée.
- **Élitisme :** conservation des deux meilleurs individus.

## Exécution

```bash
python main.py
```

## Fichiers
- `main.py` : implémentation de l'algorithme génétique.
