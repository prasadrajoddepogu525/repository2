import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import src
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.utils import save_object

@dataclass

#config class is used, inputs where we need to store the files
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig() #this will call the datatransformationconfig function

    def get_data_transformer_obj(self):
        """
        This function is responsible for data transformation
        """

        try:
            numerical_columns=['id', 'carat', 'depth', 'table', 'x', 'y', 'z']
            categorical_column=['cut', 'color', 'clarity']

            order1 = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            oder2=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            order3 = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
            numerical_pipeline=Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy='median')),
                    ("Scaler",StandardScaler())
                ]
            )

            categorical_pipeline=Pipeline(
                steps=[
                    ("Imputer",SimpleImputer(strategy='most_frequent')),
                    ("ordinal",OrdinalEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info(f"Categorical columns: {categorical_column}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",numerical_pipeline,numerical_columns),
                    ("cat_pipeline",categorical_pipeline,categorical_column)
                ]
            )

            return preprocessor


        except Exception as e:
            return CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
       try:
           train_df=pd.read_csv(train_path)
           test_df=pd.read_csv(test_path)

           logging.info("Read train and test data completed")

           logging.info("Obtaining preprocessing object")

           preprocessing_obj=self.get_data_transformer_obj()

           #target_column='price'

           input_feature_train_df=train_df.iloc[:,:-1]
           target_feature_train_df=train_df.iloc[:,-1]

           input_feature_test_df=test_df.iloc[:,:-1]
           target_feature_test_df=test_df.iloc[:,-1]

           logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
           
           
           input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
           input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

           train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
           test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

           logging.info(f"Saved preprocessing object.")
           save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

           return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,
            )
       except Exception as e:
           raise CustomException(e,sys)

            


