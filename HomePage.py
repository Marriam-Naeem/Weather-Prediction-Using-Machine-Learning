import streamlit as st
from Weather_Forecast import show_prediction
import numpy as np
import pandas as pd
import matplotlib
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Weather Forecast App", page_icon=":partly_sunny:")

col1, col2 = st.columns([3, 2])

with col2:
       
       url = requests.get("https://assets10.lottiefiles.com/private_files/lf30_jmgekfqg.json")
       url_json = dict()
       if url.status_code == 200:
                    url_json = url.json()
       else:
            print("Error in URL")
       st_lottie(url_json,
                height=400,  
                width=400,
                speed=1,  
                loop=True,  
                quality='high',
                key='Cloud' 
                )
# Right column (parameters and prediction)
with col1:
       show_prediction()



