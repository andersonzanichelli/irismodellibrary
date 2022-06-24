import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), 'iris.knn.model')

def __load_model__():
    with open(model_path, 'rb') as file:
        return pickle.load(file)

def run(data):
    model = __load_model__()
    return model.predict(data)

def square(value):
    return value * value