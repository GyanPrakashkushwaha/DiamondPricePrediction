from dataclasses import dataclass
import os



@dataclass
class DataCollectionConfig:
    raw_data_path : str = os.path.join('warehouse','data.csv')
    train_data_path :str = os.path.join('warehouse','trainData.csv')
    test_data_path : str = os.path.join('warehouse','testData.csv')


@dataclass
class DataTransformationConfig:
    preprocessorObFilePath = os.path.join('warehouse','preprocessor.pkl')


@dataclass
class ModelTrainerConfig:
    ModelObjFilePath = os.path.join('warehouse','model.pkl')

    