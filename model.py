import pickle
from sklearn.linear_model import LinearRegression
import numpy as np

# Dummy training data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(X, y)

def predict_value(input_value):
    return model.predict([[input_value]])[0]