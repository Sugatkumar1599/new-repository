import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

def predict_salary(years_of_experience):
    #data
    raw_data ={
        'years_worked':[1,2,3,4,5,6,7,8,9,10],
        'salary':[10102.04,20102.04,30102.04,40102.04,50102.04,60102.04,70102.04,80102.04,90102.04,100102.04]
    }
    df=pd.DataFrame(raw_data)

    X= np.array(df['years_worked']).reshape(-1,1)
    y= np.array(df['salary'])

    print(X)
    print(y)
    
predict_salary(10)