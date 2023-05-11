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
            
        
        except Exception as e:
            raise CustomException(e,sys)
        

        