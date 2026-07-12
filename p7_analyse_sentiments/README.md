# Analyse de sentiments - NLP & Deep Learning

## Objectif

Développer un modèle capable de classifier automatiquement le sentiment exprimé dans des messages textuels.

Le projet consiste à comparer différentes approches allant des modèles classiques de Machine Learning aux architectures Deep Learning modernes.


## Préparation des textes

Le pipeline comprend :

- nettoyage des textes,
- normalisation,
- tokenisation,
- suppression des stop words,
- stemming et lemmatisation.


## Représentation des textes

Différentes représentations vectorielles sont comparées :

- Bag-of-Words,
- Word2Vec,
- GloVe,
- embeddings Transformer.


## Modèles testés

Les approches suivantes sont évaluées :

- Naive Bayes comme baseline,
- réseau dense,
- réseau LSTM,
- modèle Transformer BERT.


## Entraînement

Les modèles Deep Learning utilisent :

- TensorFlow / Keras,
- Dropout,
- Early Stopping,
- suivi des courbes d'apprentissage.


## Évaluation

Comparaison des modèles selon :

- Accuracy,
- F1-score,
- matrice de confusion,
- temps d'entraînement,
- temps d'inférence.


## Déploiement

Préparation d'un pipeline de prédiction :

- encapsulation preprocessing + modèle,
- sérialisation des modèles,
- format d'échange JSON,
- préparation d'un déploiement Azure ML.


## Technologies

Python  
TensorFlow / Keras  
Scikit-learn  
Hugging Face Transformers  
Gensim  
Pandas  
NumPy