import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import requests
import pandas as pd 

id="https://api.ibb.gov.tr/ispark-bike/GetAllStationStatus"

yanit=requests.get(id).json()["dataList"]  #önemli

#st.json(yanit)

veri=pd.DataFrame(yanit)

filtered_df = dataframe_explorer(veri, case = False)
st.dataframe(filtered_df, use_container_width=True)

st.dataframe()

#st.table(veri) 
#st.dataframe(veri)
#st.data_editor(veri) 