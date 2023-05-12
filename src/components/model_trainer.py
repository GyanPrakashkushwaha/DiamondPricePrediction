from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
import sys

from src.utils import ( save_object,
                       evaluate_models
)
from src.components.data_classes import ModelTrainerConfig


class TrainModel:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr, test_arr):
        try:
            logging.info('model training initiated')

            X_train,X_test,y_train,y_test = (
                train_arr[:,[0,1,2,3,4,5,7,8,9]],
                test_arr[:,[0,1,2,3,4,5,7,8,9]],
                train_arr[:,7],
                test_arr[:,7]
            )

            models = {
                'Random Forest': RandomForestRegressor(),
                'Decision Tree':DecisionTreeRegressor(),
                'Gradient Boosting' : GradientBoostingRegressor(),
                'Linear Regression' : LinearRegression(),
                'K-Neighbors Regressor': KNeighborsRegressor(),
                'XGBRegressor' : XGBRegressor(),
                'AdaBoost Regressor' : AdaBoostRegressor()
            }

            model_report = evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)


            """to get best model from dictionary"""
            best_model_score = max(model_report.values())


            """to get best model name from dictionary"""
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            logging.info(f'{best_model} Best found model on both training and testing dataset and its accuracy is {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.ModelObjFilePath,
                obj=best_model
            )


            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_true=y_test,y_pred=predicted)

            return(
                r2_square,
                best_model,
                print(f'best model is {best_model_name} and its accuracy is {best_model_score}')
            )

        except Exception as e:
            raise CustomException(e,sys)
        

        