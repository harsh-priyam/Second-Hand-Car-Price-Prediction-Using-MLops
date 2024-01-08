import pandas as pd
import os 
from CarPrediction import logger 
from sklearn.linear_model import ElasticNet 
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import joblib 
from CarPrediction.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config 
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_columm],axis=1)
        test_x = test_data.drop([self.config.target_columm],axis=1)
        train_y = train_data[[self.config.target_columm]]
        test_y = test_data[[self.config.target_columm]]

        ohe = OneHotEncoder()
        ohe.fit(train_data[['name','company','fuel_type']])
        column_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')
      

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=101)

        pipe = make_pipeline(column_trans,lr)

        pipe.fit(train_x,train_y) 

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))