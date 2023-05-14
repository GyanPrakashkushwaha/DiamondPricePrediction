import sys
from src.utils import load_object
from src.exception import CustomException
import pandas as pd



class PredictionPipeline:
    
    def predict(self,features):
        try:
            model_file_path = 'warehouse\model.pkl'
            preprocessor_file_path = 'warehouse\preprocessor.pkl'

            model = load_object(file_path=model_file_path)
            encoded_data = load_object(file_path=preprocessor_file_path)

            pred = model.predict(encoded_data)

            return pred
        except Exception as e:
            raise CustomException(error_detail=sys,error_msg=e)
    
class CustomData:
    def __init__(
            self,
        carat,
        cut,
        color,
        clarity,
        depth,
        table,
        x,
        y,
        z):
        self.carat = carat

        self.cut = cut

        self.color = color

        self.clarity = clarity

        self.depth = depth

        self.table = table

        self.x = x

        self.y = y
        
        self.z = z


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "carat": [self.carat],
                "cut": [self.cut],
                "color": [self.color],
                "clarity": [self.clarity],
                "depth": [self.depth],
                "table": [self.table],
                "x": [self.x],
                "y":[self.y],
                "z":[self.z]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)


    