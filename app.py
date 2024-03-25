from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline
import joblib
from mlProject.constants import *
from mlProject.utils.common import read_yaml

config = read_yaml(CONFIG_FILE_PATH)

distances = joblib.load(os.path.join(config.data_transformation.root_dir,config.data_transformation.distances_data))
original = joblib.load(os.path.join(config.data_transformation.root_dir,config.data_transformation.original_data))
ds_cols = joblib.load(os.path.join(config.data_transformation.root_dir,config.data_transformation.ds_cols))
Scaling = joblib.load(os.path.join(config.data_transformation.root_dir,config.data_transformation.Scaling))
cities=list(set(original["City"]))


app = Flask(__name__) # initializing a flask app


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html",cities=cities)



@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 




@app.route('/recommendations',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            mode = request.form['mode']
            tuition_cost = request.form['tuition_cost']
            program_years = request.form['program_years']
            need_gre = request.form['need_gre']
            institution_type = request.form['institution_type']
            city = request.form['city']

            predict_values = {}
            for i in ds_cols:   
                predict_values[i]=None

            predict_values["Online"] = 1 if mode == "Online" else 0    
            predict_values["Total_Tuition_Cost"]=tuition_cost
            predict_values["Program_Years_Full_Time"]= program_years
            predict_values["Need_GRE"]=1 if need_gre == "Needed" else 0
            predict_values["Institution Type"]= 1 if institution_type == "Public" else 0
            
            for i in predict_values.keys():
                if i == "City_"+city:
                    predict_values[i]=1
                index = range(1)
            
            data=pd.DataFrame(predict_values,index=index)
            data.fillna(0,inplace=True)   

            data[["Total_Tuition_Cost"]]=Scaling.transform(data[["Total_Tuition_Cost"]])

            obj = PredictionPipeline()
            predict = obj.predict(data)[0]

            college_index = original.index[original['School Name'] == predict].tolist()[0]
            college_list  = sorted(list(enumerate(distances[college_index])),reverse=True,key=lambda x : x[1])[0:6]
            college_list = [i[0] for i in college_list]
            show = original.iloc[college_list]

            recommendations = show.values.tolist()

            return render_template('Recommend.html', recommendations = recommendations)

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 8050)