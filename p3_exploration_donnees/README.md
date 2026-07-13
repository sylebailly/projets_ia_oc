# Exploration Open Food Facts - Analyse exploratoire de données

## Objectif

Explorer et analyser la base Open Food Facts afin d'étudier les relations entre les caractéristiques nutritionnelles des produits alimentaires et le Nutri-Score.

L'objectif est de produire un jeu de données nettoyé et de mettre en évidence les principaux facteurs nutritionnels associés au Nutri-Score.


## Données

Le projet utilise le jeu de données Open Food Facts contenant plusieurs centaines de milliers de produits alimentaires.

Les informations exploitées comprennent notamment :

- informations nutritionnelles pour 100 g,
- Nutri-Score,
- nom des produits,
- pays de commercialisation.


## Préparation des données

Les principales étapes réalisées sont :

- sélection des produits commercialisés en France,
- suppression des variables comportant trop de valeurs manquantes,
- suppression des doublons,
- normalisation des noms de produits,
- détection des valeurs aberrantes,
- traitement des valeurs atypiques,
- imputation des valeurs manquantes avec KNN Imputer.


## Analyse exploratoire

Les analyses réalisées comprennent :

- étude des distributions,
- analyse des corrélations,
- visualisation des variables nutritionnelles,
- comparaison des distributions selon le Nutri-Score,
- analyse multivariée.


## Analyse statistique

Le projet met en œuvre plusieurs méthodes statistiques :

- analyse de variance (ANOVA),
- analyse en composantes principales (ACP),
- interprétation des composantes principales.


## Résultats

L'analyse met notamment en évidence :

- une forte relation entre certains nutriments (énergie, lipides, acides gras saturés) et le Nutri-Score,
- des corrélations importantes entre plusieurs variables nutritionnelles,
- une représentation synthétique des produits alimentaires grâce à l'ACP.


## Technologies

Python  
Pandas  
NumPy  
Scikit-learn  
Statsmodels  
Matplotlib  
Seaborn  
Jupyter Notebook