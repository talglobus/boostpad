import numpy as np
import pandas as pd
import tensorflow as tf
import sklearn as sk

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

def model_value_linear(data, test):
    df = pd.read_csv(data)
    X = df[['bathrooms', 'bedrooms', 'finishedsqft', 'totalrooms', 'yearbuilt', 'zindexvalue']]
    Y = df['lastsoldprice']

    n = pd.get_dummies(sf.group)
    X = pd.concat([X, n], axis=1)
    m = pd.get_dummies(sf.usecode)
    X = pd.concat([X, m], axis=1)
    
    #X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
    regressor = LinearRegression()
    #regressor.fit(X_train, y_train)
    
    regressor.fit(X, Y)
    y_pred = regressor.predict(test)
    
    return y_pred

def model_value_forest(data, test):
    pass

def model_decide(index, test):
    if index > 50:
        return True
    else:
        return False

def model_future_value_short(test, years):
    return test * 1.06**years

def predict_savings_short(v1, v2):
    return v1 - v2

def main():
    pass

if __name__ == "__main__":
    main()