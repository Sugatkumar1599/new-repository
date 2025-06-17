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
    y= np.array(df['salary']).reshape(-1,1)
    
  
#    #split the training data and testist data
#     train_X,test_X,train_y,test_y=train_test_split(X ,y, random_state=0 ,test_size=.20) 
#     # print('train_X',train_X.tolist())
#     # print('train_y',train_X.tolist())
#     # print('test_X',test_X.tolist())
#     # print('test_y',test_y.tolist())


#     #Intialise the data 
#     model= LinearRegression()
#     model.fit(train_X,train_y)

#     #Make the prediction
#     y_prediction = model.predict([[years_of_experience]])
#     print('Prediction:',y_prediction)
#     #used to check how accurate the model is'
#     y_test_prediction = model.predict(test_X)
#     y_line = model.predict(X)
#     #Extra_info
#     print('Slope :',model.coef_)
#     print('Intercept :',model.intercept_)
#     print('MAE :',mean_absolute_error(test_y,y_test_prediction))
#     print('r2 :',r2_score(test_y,y_test_prediction))

#     plt.scatter(X, y, s=12)
#     plt.xlabel('Years (Exp)')
#     plt.ylabel('salary')
#     plt.plot(X,y_line, color='r')
#     plt.show()

predict_salary(14)