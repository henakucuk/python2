import streamlit as st
import requests
import pandas as pd 

id="https://data.ibb.gov.tr/dataset/bd3b9489-c7d5-4ff3-897c-8667f57c70bb/resource/6800ea2d-371b-4b90-9cf1-994a467145fd/download/salk-kurum-ve-kurulularna-ait-bilgiler.json"

yanit=requests.get(id).json()

#st.json(yanit)
veri=pd.DataFrame(yanit)
st.table(veri) #klasik tablo
#st.dataframe(veri) #filtre yapabilecegim
#st.data_editor(veri) #veriyi değiştirme gücüne sahip