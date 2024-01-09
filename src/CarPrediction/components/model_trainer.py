import pandas as pd
import os 
from CarPrediction import logger 
from sklearn.linear_model import LinearRegression
import joblib 
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from CarPrediction.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config 
    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Separate features and target variable
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]

        # Define a column transformer for preprocessing
        numeric_features = train_x.select_dtypes(include=['int32']).columns
        numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])

        categorical_features = train_x.select_dtypes(include=['object']).columns
        categorical_transformer = Pipeline(steps=[('onehot', OneHotEncoder(handle_unknown='ignore'))])

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numeric_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        # Combine preprocessing with the model
        model = Pipeline(steps=[('preprocessor', preprocessor),
                                ('model', LinearRegression(fit_intercept=self.config.fit_intercept, copy_X =self.config.copy_X,positive=self.config.positive))])

        # Fit the model
        model.fit(train_x, train_y)

        # Save the trained model
        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))

