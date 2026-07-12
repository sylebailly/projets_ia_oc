# Système de recommandation d'articles - Machine Learning

## Objectif

Développer un moteur de recommandation capable de proposer des articles pertinents en fonction du profil utilisateur et de son historique d'interaction.


## Approche

Le système combine deux méthodes complémentaires :

### Content-Based Filtering

Recommandation basée sur les caractéristiques des articles :

- représentation vectorielle,
- embeddings,
- calcul de similarité cosinus.


### Collaborative Filtering

Recommandation basée sur les interactions utilisateurs :

- construction d'une matrice utilisateur/article,
- factorisation matricielle SVD.


## Préparation des données

Traitements réalisés :

- nettoyage des interactions,
- analyse des comportements utilisateurs,
- calcul de scores d'intérêt,
- création des jeux d'entraînement.


## Pipeline ML

Le pipeline comprend :

- préparation des données,
- entraînement du modèle,
- sauvegarde des artefacts,
- chargement pour l'inférence.


## Déploiement

Le modèle est exposé via une API serverless :

- Azure Functions,
- stockage des modèles dans Azure Blob Storage,
- génération de recommandations en temps réel.


## Gestion des cas utilisateurs

Le système prend en compte :

- nouveaux utilisateurs,
- utilisateurs récents,
- utilisateurs avec historique complet.


## Technologies

Python  
Pandas  
NumPy  
Scikit-surprise  
Embeddings  
Similarité cosinus  
Azure Functions  
Azure Blob Storage