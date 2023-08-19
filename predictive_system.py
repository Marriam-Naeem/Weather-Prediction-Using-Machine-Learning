import numpy as np
import pickle

# loading the saved model using rb  (read binary)

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input = [0.17,0.0,0.0,36,25]
input_data_as_numpy_array = np.asarray(input[0:])
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
input_data_reshaped
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
