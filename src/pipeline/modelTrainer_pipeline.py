import sys
from src.exception import CustomException
from src.components.data_collection import DataCollection
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import TrainModel

if __name__ == '__main__':
    try:
        obj = DataCollection()
        traindata , testdata = obj.initiate_data_collection()

        obj2 = DataTransformation()
        train_array , test_array,_ = obj2.initiate_data_transformation(train_data_path_transformation=traindata,test_data_path_transformation=testdata)
        
        obj3 = TrainModel()
        obj3.initiate_model_trainer(train_arr=train_array,test_arr=test_array)
        
    except Exception as e:
        raise CustomException(e,sys)


    