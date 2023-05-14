import sys
import pandas as pd
from src.exception import CustomException
from src.components.data_classes import DataCollectionConfig
from src.logger import logging
import os
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import TrainModel

class DataCollection:
    def __init__(self):
        self.data_collection_config = DataCollectionConfig()


    def initiate_data_collection(self):

        logging.info('Entered the data ingestion method Or component')
        
        try:
            df = pd.read_csv('notebook\data\diamonds.csv')
            logging.info('read dataset from dataframe')

            # making warehouse .......
            os.makedirs('warehouse',exist_ok=True)

            df.to_csv(path_or_buf=self.data_collection_config.raw_data_path,index=False,header=True)

            logging.info('train test split initiated')

            trainData, testData = train_test_split(df,test_size=.3,random_state=0)

            trainData.to_csv(self.data_collection_config.train_data_path,index = False,header=True)

            testData.to_csv(self.data_collection_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of the data is completed')


            return(
                self.data_collection_config.train_data_path,
                self.data_collection_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)


