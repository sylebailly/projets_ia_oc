# Segmentation sémantique d'images urbaines - Deep Learning

## Objectif

Développer un modèle de segmentation sémantique capable d'identifier automatiquement les éléments présents dans une scène urbaine.

L'application cible concerne la compréhension d'environnement pour des systèmes de conduite autonome.


## Données

Le projet utilise le dataset Cityscapes contenant des images urbaines annotées pixel par pixel.

Les données comprennent :

- images RGB,
- masques de segmentation multi-classes.


## Pipeline de traitement

Le pipeline comprend :

- préparation des images,
- génération des masques,
- normalisation,
- augmentation des données,
- génération personnalisée des batches.


## Architectures testées

Les modèles étudiés :

- U-Net,
- LinkNet.


Avec différentes stratégies :

- entraînement classique,
- Transfer Learning,
- backbones ResNet50 et VGG16.


## Entraînement

Optimisations utilisées :

- Dice Loss,
- Early Stopping,
- Data Augmentation,
- suivi des performances entraînement / validation.


## Évaluation

Les modèles sont évalués avec :

- IoU Score,
- Dice Coefficient,
- Accuracy.


## Technologies

Python  
TensorFlow / Keras  
Segmentation Models  
OpenCV  
Albumentations  
NumPy  
Matplotlib