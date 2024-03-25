import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from pathlib import Path
from typing import Any
from mlProject.utils.common import save_bin_data,save_bin_array
from mlProject.config.configuration import DataTransformationConfig
import numpy as np

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.data = pd.read_csv(self.config.data_path)
        
    def original(self):
        save_bin_data(self.data, Path(os.path.join(self.config.root_dir, self.config.original_data)))
    
    def transform(self):
        self.data["Online"]=self.data["Online"].apply(lambda x : 1 if x == "Online" else 0)
        self.data["Need_GRE"]=self.data["Need_GRE"].apply(lambda x : 1 if x == "Needed" else 0)
        self.data["Institution Type"]=self.data["Institution Type"].apply(lambda x : 1 if x == "Public" else 0)
        sc= StandardScaler()
        self.data[["Ranking","Total_Tuition_Cost","Median_Salary_10yr"]]=sc.fit_transform(self.data[["Ranking",
                                                                                       "Total_Tuition_Cost",
                                                                                       "Median_Salary_10yr"]])
    
    def distances(self):
        df  = self.data.copy()
        pd.set_option('future.no_silent_downcasting', True)
        df.drop(["LINK"],axis="columns",inplace=True)
        df.drop(["School Name"],axis="columns",inplace=True)
        df=pd.get_dummies(df)
        df.replace(False,0,inplace=True)
        df.replace(True,1,inplace=True)
        cos_sim = cosine_similarity(df)
        save_bin_array(cos_sim,Path(os.path.join(self.config.root_dir,self.config.distances_data)))
    
    def save_train_Data(self):
        df  = self.data.copy()
        df=df.drop(["State","Ranking","Min_Undergraduate_GPA",
                    "Median_Salary_10yr","LINK"],axis="columns")  
        dummies=pd.get_dummies(df.drop(["School Name"],axis="columns"))
        df = pd.concat([df["School Name"],dummies],axis="columns")
        df.replace(False,0,inplace=True)
        df.replace(True,1,inplace=True)  
        
        df.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)

        logger.info("Saved data for training")
        ds_cols  =np.array(df.columns.to_list()[1:])
        save_bin_array(ds_cols,Path(os.path.join(self.config.root_dir,self.config.ds_cols)))

        logger.info("Saved columns names")