import pandas as pd
import os
from mlProject import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]

        rand = RandomForestClassifier()
        rand.fit(train_x, train_y)

        joblib.dump(rand, os.path.join(self.config.root_dir, self.config.model_name))

