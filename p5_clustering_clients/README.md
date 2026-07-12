# Segmentation clients e-commerce - Machine Learning non supervisé

## Objectif

Identifier différents profils clients à partir de données transactionnelles afin de mieux comprendre les comportements d'achat et faciliter la mise en place d'actions marketing ciblées.


## Données

Analyse du dataset e-commerce Olist comprenant plusieurs sources :

- commandes,
- clients,
- paiements,
- produits,
- vendeurs,
- avis clients.


## Préparation des données

Construction d'un dataset client consolidé à partir de plusieurs tables :

- nettoyage des données,
- gestion des valeurs manquantes,
- suppression des doublons,
- analyse des valeurs aberrantes,
- agrégation des données transactionnelles.


## Feature engineering

Création d'indicateurs comportementaux clients :

- Recency : ancienneté du dernier achat,
- Frequency : fréquence d'achat,
- Monetary : montant total dépensé.

Les variables sont complétées par :

- satisfaction client,
- délais de livraison,
- habitudes d'achat.


## Segmentation

Mise en œuvre de méthodes de clustering :

- K-Means,
- DBSCAN.


Le nombre de clusters est étudié à l'aide de :

- Silhouette Score,
- analyse comparative des paramètres.


## Analyse des segments

Les groupes obtenus sont étudiés grâce à :

- statistiques par cluster,
- visualisations des profils,
- réduction dimensionnelle t-SNE.


## Suivi du modèle

Une approche de suivi temporel est proposée :

- recalcul périodique des segments,
- comparaison des regroupements,
- mesure de stabilité avec Adjusted Rand Index.


## Technologies

Python  
Pandas  
NumPy  
Scikit-learn  
Matplotlib  
Seaborn  
K-Means  
DBSCAN  
PCA  
t-SNE