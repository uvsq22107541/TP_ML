______________________________________________________________
***** Random Forest V/S Gradient Boosting *****
______________________________________________________________

Les deux algorithmes sont utilisés pour résoudre des problèmes de classification ou de régression dans le cadre de l'apprentissage supervisé.

Sont des algorithmes d'ensemble i.e. des techniques qui combinent plusieurs algorithmes de base de Machine Learning tels que les arbres de décisions pour améliorer les résultats de la prédiction et ainsi, produire un modèle plus robuste et plus précis. 

______________________________________________________________
***** Différence entre Random Forest et Gradient Boosting *****
______________________________________________________________

La principale différence entre Random Forest et Gradient Boosting est la façon dont les modèles sont combinés pour former une prédiction finale. 

  ***** 1. Random Forest *****
  Random Forest est un type de méthode d'ensemble parallèle, i.e. plusieurs arbres de décision sont construits de manière indépendante et la prédiction finale est faite en moyennant ou en votant sur les prédictions de tous les arbres.

  ***** 2. Gradient Boosting *****
  Gradient Boosting est un type de méthode d'ensemble séquentiel, i.e. les arbres sont construits séquentiellement, où chaque nouvel arbre est construit pour corriger les erreurs des prédictions précédentes. 

_____________________________________________________________
***** Etapes pour construire un modèle de prédiction *****
_____________________________________________________________

1. Préparation des données : collection, nettoyage et préparation des données pour l'analyse.
2. Séparation des données : séparation des données en un ensemble d'entraînement (pour entraîner le modèle) et un ensemble de test (pour évaluer le modèle).
3. Choix de l'algorithme / méthode de ML à utiliser : random forest ou gradient boosting.
4. Entraînement du modèle : ajustement des paramètres du modèle sur l'ensemble d'entraînement pour qu'il puisse prédire avec précision la variable cible.
5. Évaluation du modèle : évaluation de la précision du modèle en utilisant l'ensemble de test.
6. Utilisation du modèle pour prédire de nouvelles données: une fois la précision du modèle satisfaisante, l'utiliser pour prédire sur de nouvelles données.


Chaque méthode a des paramètres spécifiques (les hyperparamètres) qui doivent être ajustés pour obtenir les meilleures performances prédictives possibles.

_____________________________________________________________
**** Hyperparamètres *****
_____________________________________________________________

Il y a plusieurs hyperparamètres qui peuvent être ajustés pour optimiser les performances du modèle. Voici quelques exemples d'hyperparamètres couramment utilisés dans les implémentations de Random Forest et Gradient Boosting :


1. Nombre d'arbres de décision : c'est le nombre total d'arbres de décision que le modèle utilisera pour faire des prédictions. Un nombre plus élevé d'arbres peut aider à améliorer les performances, mais peut également augmenter le temps d'entraînement et de prédiction.
2. Profondeur des arbres : c'est la profondeur maximale des arbres de décision utilisés par le modèle. Une profondeur plus grande peut permettre au modèle de capturer des relations plus complexes, mais peut également conduire à un surapprentissage.
3. Min_samples_split : c'est le nombre minimum d'échantillons requis pour diviser un nœud de l'arbre de décision. Une valeur plus grande peut aider à prévenir le surapprentissage en évitant de créer des feuilles avec très peu d'exemples, mais peut également réduire la capacité du modèle à capturer des relations complexes dans les données.
4. Min_samples_leaf : c'est le nombre minimum d'échantillons requis pour former une feuille de l'arbre de décision. Une valeur plus grande peut également aider à prévenir le surapprentissage, mais peut réduire la capacité du modèle à s'ajuster aux données.
5. Learning rate : (pour Gradient Boosting) c'est un paramètre qui contrôle la taille des mises à jour effectuées sur les poids à chaque étape de l'entraînement. Un taux d'apprentissage plus faible signifie que les mises à jour sont plus petites, ce qui peut aider à éviter le surapprentissage, mais peut également ralentir le processus d'entraînement.

Il existe également d'autres hyperparamètres qui peuvent être ajustés, selon l'implémentation de Gradient Boosting utilisée.

________________________________________________________
***** Choix des valeurs des Hyperparamètres ***** 
________________________________________________________

Le choix des valeurs des Hyperparamètres se base sur la validation croisée (cross-validation en anglais) : une technique d'évaluation de la performance d'un modèle de machine learning ou d'une méthode statistique. Elle permet de mesurer la capacité de généralisation d'un modèle en évaluant sa performance sur des données qui n'ont pas été utilisées pour l'entraîner.

Le principe de la validation croisée consiste à diviser le jeu de données en plusieurs sous-ensembles appelés "plis" ou "folds". Le modèle est alors entraîné sur une partie des données (par exemple, sur 4 des 5 folds) et évalué sur la partie restante (par exemple, sur le 5ème fold). Ce processus est répété plusieurs fois en variant à chaque fois les folds utilisés pour l'entraînement et pour l'évaluation, de manière à ce que chaque fold soit utilisé une fois pour l'évaluation.

_______________________________________________________
***** Métriques d'évaluation *****
_______________________________________________________

ll existe plusieurs métriques d'évaluation pour la régression, en voici quelques-unes :

1. MSE (Mean Squared Error) : C'est la moyenne des erreurs au carré entre les prédictions et les vraies valeurs. Elle donne une idée de la qualité de la prédiction en terme de distance entre les valeurs réelles et les valeurs prédites.
2. RMSE (Root Mean Squared Error) : C'est la racine carrée de la MSE, elle est utilisée pour avoir une estimation de l'écart type de l'erreur.
3. MAE (Mean Absolute Error) : C'est la moyenne des valeurs absolues des erreurs entre les prédictions et les vraies valeurs. Elle permet de mesurer l'exactitude de la prédiction sans prendre en compte les écarts de signe.
4. R2 (Coefficient de détermination) : Il représente la proportion de la variance de la variable dépendante qui est expliquée par la ou les variables indépendantes. Plus le R2 est élevé, plus le modèle est performant.

_______________________________________________________
**** Performances *****
_______________________________________________________

Gradient Boosting peut souvent donner de meilleures performances de prédiction que Random Forest, mais il est également plus sensible aux données aberrantes et plus sujet à un surapprentissage s'il n'est pas correctement régularisé.
