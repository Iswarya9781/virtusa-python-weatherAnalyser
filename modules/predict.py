import os
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('Agg') 

BASE_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "weather_data.csv"))

def predict_temperature():
    df = pd.read_csv("data/weather_data.csv")
    df["temp"] = pd.to_numeric(df["temp"], errors="coerce")

    df["date"] = pd.to_datetime(df["date"])
    
    df["date_num"] = df["date"].map(lambda x: x.timestamp())
    
    if(len(df)< 5):
        return df["temp"].mean()
    
    
        
    X = df[["date_num"]]
    y = df["temp"]
    model = LinearRegression()
    model.fit(X, y)
    
    future = pd.DataFrame([[df["date_num"].iloc[-1] + 86400]], columns=["date_num"])
    prediction = model.predict(future)
    return prediction[0]
