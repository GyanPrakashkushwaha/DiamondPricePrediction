import sys
import pandas as pd
import os
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler , LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.components.data_classes import DataTransformationConfig
from src.utils import save_object
from src.exception import CustomException
from src.logger import logging
import numpy as np

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):

        try:
            num_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
            ordinal_cols = ['cut','clarity']
            nominal_col = ['color']


            num_pipeline = Pipeline(
            steps=[
            ('standardScaler',StandardScaler()),
            ('imputer',SimpleImputer(strategy='median'))
            ]
            )


            preprocessor_col = ColumnTransformer(
            transformers=[
                ('num_pipeline', num_pipeline, num_cols),
                ('cut_col_pipeline', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinal_encoder', OrdinalEncoder(categories=[['Good', 'Very Good', 'Fair', 'Ideal', 'Premium']]))
                ]), ['cut']),
                ('clarity_col_pipeline', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('ordinal_encoder', OrdinalEncoder(categories=[['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']]))
                ]), ['clarity']),
                ('color_col_pipeline', Pipeline(steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('lableEncoder', OrdinalEncoder())
                ]), ['color'])
                ]
                )
            
            return preprocessor_col
            
        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_transformation(self,train_data_path_transformation,test_data_path_transformation):

        try:
            train_df = pd.read_csv(train_data_path_transformation)
            test_df = pd.read_csv(test_data_path_transformation)

            logging.info('Reading train and test data completed')

            logging.info('Obtaining preprocessing object')

            preprocessor_obj = self.get_data_transformation_object()


            target_col_name = 'price'
            input_feature_train_df = train_df.drop(columns=[target_col_name], axis=1)
            target_feature_train_df = train_df[target_col_name]

            input_feature_test_df = test_df.drop(columns=[target_col_name], axis=1)
            target_feature_test_df = test_df[target_col_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
                ] # np.c_ this concatenate like np.concat function but its axis is by default '1'

            logging.info(f"Saving preprocessing object.")

            save_object(
                file_path= self.data_transformation_config.preprocessorObFilePath,
                obj=preprocessor_obj
                )
            
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessorObFilePath
            )

            
        except Exception as e:
            raise CustomException(e,sys)


    