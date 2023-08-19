# importing libraries
import numpy as np
import pickle
import streamlit as st

# loading the saved model using rb  (read binary)
loaded_model = pickle.load(open('C:/Users/ghio_/Desktop/csn Lab/Weather Forecast System/trained_model.sav', 'rb'))


def weather_predict(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction

def show_prediction():
    
    # Set page title and iconS

    
    #title of the web page
    st.title('☀️ Weather Forecast')
    st.markdown("Enter the information from yesterday to get a weather forecast for today.")

    #getting input from the user
    precip = st.number_input('Rate of Precipitation', value=0.0)
    snow = st.number_input('Rate of Snow', value=0.0)
    snowd = st.number_input('Depth of Snow', value=0.0)
    maxt = st.number_input('Maximum temperature (Farenheit)', value=0.0)
    mint = st.number_input('Minimum Temperature (Farenheit)', value=0.0)

  
    #code for prediction
    forecast = ''

    #creating button for Prediction

    if st.button('Give Forecast'):
        forecast = weather_predict([float(precip),float(snow),float(snowd),float(maxt), float(mint)])
        
         
    # Display prediction
    if forecast:
        st.success(f"The predicted weather for today is: {forecast[0]:.3f}")
    else:
        st.info("Click 'Give Forecast' to see the prediction.")




    



