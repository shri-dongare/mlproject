from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn import preprocessing
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application 

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    print("Request received")

    if request.method == 'GET':
        print("GET")
        return render_template('home.html')

    print("POST")

    data = CustomData(
        gender=request.form.get('gender'),
        race_ethnicity=request.form.get('ethnicity'),
        parental_level_of_education=request.form.get('parental_level_of_education'),
        lunch=request.form.get('lunch'),
        test_preparation_course=request.form.get('test_preparation_course'),
        reading_score=float(request.form.get('reading_score')),
        writing_score=float(request.form.get('writing_score'))
    )

    pred_df = data.get_data_as_data_frame()

    print("========== DATAFRAME ==========")
    print(pred_df)
    print("===============================")

    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)

    print("Prediction:", result)

    return render_template("home.html", results=result[0])


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True, use_reloader=False)