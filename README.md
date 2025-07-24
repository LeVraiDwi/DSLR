# DSLR
42 project about: Datascience X Logistic Regression

## Histograms
    histograms.py affiche les hitograme des different cours. Qui montre le score des eleves en fonction de leur maison. Ici le but est de repondre a la question:
    Which Hogwarts course has a homogeneous score distribution between all four houses?
### Aprroche graphique
    Pour ca on cherche sur qu'elle graphique les score des maison semble le plus similaire
### Approche arithmetique
    Pour determiner qu' elle cours a la ditribution de score la plus homogene entre les maison. On cherche a determiner qu'elle classe a la derivation standart (std in utils.py) entre les score moyen des maison. Plus le score est bas plus le cours est homogegne.

## Scatter_plot
    scatter_plot.py permet de trouver le couple de variable qui sont le  plus correler.
### Approche graphique
    On cherche ici un couple de variable dont le graphique de point formeras le plus possible un droite.
### Approche arithmetique
    Pour trouver qu' elle variable sont les plus correller on peut calculer la matrix de correlation des cours:
```    
                                Arithmancy  Astronomy  ...  Care of Magical Creatures    Charms    Flying
Arithmancy                       1.000000   0.044430  ...                   0.038896  0.104625  0.163970
Astronomy                        0.044430   1.000000  ...                   0.024163  0.526608  0.512377
Herbology                        0.031995   0.018229  ...                   0.060914  0.747755  0.278585
Defense Against the Dark Arts    0.044430   1.000000  ...                   0.024163  0.526608  0.512377
Divination                       0.005860   0.477947  ...                   0.021221  0.390945  0.401089
Muggle Studies                   0.050263   0.591140  ...                   0.049220  0.853373  0.198084
Ancient Runes                    0.082528   0.207361  ...                   0.014294  0.349610  0.566074
History of Magic                 0.068600   0.394914  ...                   0.050820  0.538433  0.897115
Transfiguration                  0.007317   0.435840  ...                   0.054967  0.547589  0.872422
Potions                          0.296657   0.554737  ...                   0.013340  0.255250  0.558627
Care of Magical Creatures        0.038896   0.024163  ...                   1.000000  0.063826  0.038899
Charms                           0.104625   0.526608  ...                   0.063826  1.000000  0.354373
Flying                           0.163970   0.512377  ...                   0.038899  0.354373  1.000000
```
    Pour calculer cette matrix on calcul la correlation des cours 2 a 2. 
    correlation: corr = (cov / (std1 * std2))
    avec cov la covariance telle que: cov = sum((ValCour1 - meanCour1) * (ValCour2 - meanCour2))
    et std1 et std2 la derivation standart respective du Cour2 et du Cours2 
    on normalize en divisant les par le nombre de d'eleve corrNorme = corr/n.
    
    On Cherche ensuite dans la matrix le couple de cours qui a la corellation absolue la plus elever sont prendre en compte les pair egale ex:(Astronomy, Astronomy) qui feront toujours 1. et qui forme la diagonale au mileux du tableau.

## Pair_Plot
    pair_plot.py affiche des graphique qui vont permettre de determiner qu'elle variable utiliser pour faire notre regresion lineaire logique. On cherche des graphiques ou les differentes ecole sont le plus separer possible afin de pouvoir les trier par la suite.