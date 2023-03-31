# -*- coding: utf-8 -*-
"""GradientBoosting.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_0xjXg6vYOkgdyxu9r9yZy-IfzimLQ2w
"""

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Chargement des données
data = pd.read_csv('fetal_health.csv')

# Séparation des données en train et test
X_train, X_test, y_train, y_test = train_test_split(data.drop('fetal_health', axis=1), data['fetal_health'], test_size=0.2, random_state=42)

# Définition du modèle
gb = GradientBoostingRegressor()

# Définition de la grille de recherche des hyperparamètres
param_grid = {'n_estimators': [50, 100, 200],
              'learning_rate': [0.01, 0.1, 0.5, 1],
              'max_depth': [5, 10, 20, None],
              'min_samples_split': [2, 5, 10],
              'min_samples_leaf': [1, 2, 4]}

# Recherche des meilleurs hyperparamètres avec la validation croisée
grid_gb = GridSearchCV(gb, param_grid=param_grid, cv=5, n_jobs=-1, verbose=2) # verbose : une ligne sera affichée à chaque itération pour surveiller l'entraînement d'un modèle et comprendre comment il apprend à partir des données

grid_gb.fit(X_train, y_train)

# Affichage des meilleurs hyperparamètres et de la performance sur le jeu de test
print("Meilleurs hyperparamètres : ", grid_gb.best_params_)

# Evaluation avec les métriques de régression 
y_pred = grid_gb.predict(X_test)
print("Performance sur le jeu de test (MSE) : ", mean_squared_error(y_test, y_pred, squared=False))
print("Performance sur le jeu de test (RMSE) : ", mean_squared_error(y_test, y_pred, squared=True)) #Racine carre (MSE)
print("Performance sur le jeu de test (R2) : ", r2_score(y_test, y_pred)) #le coefficient de détermination R2