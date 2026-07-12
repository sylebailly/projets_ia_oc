# Analyse automatique de retours clients et labellisation d'images - Machine Learning

## Objectif

Développer une solution d'analyse automatique de données issues de plateformes de restauration afin d'identifier les sujets d'insatisfaction clients et d'explorer la possibilité de labelliser automatiquement des images.

Le projet combine :
- traitement automatique du langage (NLP),
- collecte de données via API,
- traitement d'images par vision par ordinateur.


## Données

Le projet utilise le dataset Yelp contenant :

- avis clients,
- informations sur les restaurants,
- photos associées aux établissements.

Les données textuelles sont utilisées pour détecter les thèmes récurrents dans les avis.
Les images sont utilisées pour étudier une approche de classification non supervisée.


## Pipeline NLP

Le traitement des avis clients comprend :

- analyse exploratoire des données,
- nettoyage et normalisation des textes,
- suppression des caractères spécifiques et stop words,
- lemmatisation,
- vectorisation TF / TF-IDF,
- modélisation des sujets.


## Modélisation des sujets

L'approche utilisée repose sur :

- Latent Dirichlet Allocation (LDA),
- recherche du nombre optimal de topics,
- analyse des mots représentatifs,
- visualisation des résultats.

Le modèle permet d'identifier automatiquement les principaux sujets d'insatisfaction présents dans les avis.


## Collecte de données

Une collecte complémentaire est réalisée via l'API Yelp afin de :

- récupérer de nouveaux restaurants,
- extraire leurs avis,
- tester l'intégration de nouvelles données dans le pipeline.


## Pipeline image

Une approche de vision par ordinateur est développée pour explorer la labellisation automatique des photos.

Le pipeline comprend :

- prétraitement des images avec OpenCV,
- extraction de caractéristiques visuelles avec SIFT,
- création de représentations Bag of Visual Words,
- réduction de dimension avec PCA / t-SNE,
- clustering des images.


## Évaluation

Les résultats sont évalués avec :

- matrice de confusion,
- Adjusted Rand Index (ARI),
- classification report.


## Technologies

Python  
Pandas  
NumPy  
Scikit-learn  
NLTK  
OpenCV  
SIFT  
Matplotlib  
Seaborn  
Yelp API