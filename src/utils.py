import os 
import sys 
import numpy as np 
import pandas as pd
import dill 
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok= True) #Add exist_okay= True

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]

            grid = GridSearchCV(model, param, cv= 3)
            grid.fit(X_train, y_train) #Fitting to get the best params. 

            model.set_params(**grid.best_params_)
            model.fit(X_train, y_train) #Train the model using best params received from GridSearchCV

            #model.fit(X_train, y_train) #Train the model #Commented because hyperparameter tuning is added

            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)

            train_r2_score = r2_score(y_train, y_pred_train)
            test_r2_score = r2_score(y_test, y_pred_test)

            report[list(models.keys())[i]] = test_r2_score
        
        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
