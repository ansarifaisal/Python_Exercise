"""
    https://www.youtube.com/watch?v=XEgRSum4Zps&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=86&ab_channel=CodeWithHarry
    Pickling with IRIS Dataset

    Pickle
    Request

    uci ml dataset
    

"""
from time import time;
import pickle
init_time = time()

data = []

with open("Exercise_12\Data_Set.csv") as f:
    data = f.readlines()
file = "Exercise_12\data.pkl"
file_obj = open(file, "wb")
pickle.dump(data, file_obj)
file_obj.close()

file_obj = open(file, "rb")
data_list = pickle.load(file_obj)
