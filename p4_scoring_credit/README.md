# Scoring crédit - Machine Learning supervisé

## Objectif

Construire un modèle de scoring permettant d'estimer le risque de défaut de paiement d'un client à partir de données historiques de crédit.

Le modèle doit permettre d'identifier les profils présentant un risque élevé tout en conservant un bon équilibre entre détection des défauts et limitation des faux positifs.


## Données

Le projet utilise le dataset Home Credit Default Risk contenant des informations financières et personnelles issues de plusieurs sources :

- caractéristiques des demandeurs,
- historique de crédits,
- informations de paiement,
- données comportementales.


## Préparation des données

Les étapes réalisées :

- analyse exploratoire des données,
- étude des distributions,
- traitement des valeurs manquantes,
- détection des valeurs aberrantes,
- fusion de plusieurs sources de données,
- encodage des variables catégorielles.


## Feature engineering

Création de variables permettant d'améliorer la capacité prédictive du modèle :

- ratios financiers,
- agrégations historiques,
- indicateurs liés aux comportements de paiement.


## Modélisation

Plusieurs modèles de classification ont été comparés :

- Régression logistique,
- Random Forest,
- SVM.


L'entraînement utilise :

- pipelines Scikit-learn,
- validation croisée stratifiée,
- recherche d'hyperparamètres,
- gestion du déséquilibre des classes.


## Gestion du déséquilibre

Les différentes approches testées :

- SMOTE,
- Random Undersampling,
- pondération des classes.


## Évaluation

Les performances sont analysées avec :

- ROC-AUC,
- courbe ROC,
- matrice de confusion,
- précision,
- rappel,
- F1-score.


## Technologies

Python  
Pandas  
NumPy  
Scikit-learn  
Imbalanced-learn  
Matplotlib  
Seaborn  
Jupyter Notebook