import sys
from src.utils import load_object
from src.exception import CustomException
import pandas as pd
from src.logger import logging


class PredictionPipeline:
    
    def predict(self,features):
        try:
            model_file_path = 'warehouse\model.pkl'
            preprocessor_file_path = 'warehouse\preprocessor.pkl'

            model = load_object(file_path=model_file_path)
            preprocessor = load_object(file_path=preprocessor_file_path)

            encoded_data = preprocessor.transform(features)

            pred = model.predict(encoded_data)

            return pred
        except Exception as e:
            raise CustomException(error_detail=sys,error_msg=e)
    
class CustomData:
    def __init__(self,
                 carat:float,
                 depth:float,
                 table:float,
                 x:float,
                 y:float,
                 z:float,
                 cut:str,
                 color:str,
                 clarity:str):
        
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise CustomException(e,sys)


