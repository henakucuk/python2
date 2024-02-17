import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer  ###
import requests
import pandas as pd
adres="https://data.ibb.gov.tr/dataset/bd3b9489-c7d5-4ff3-897c-8667f57c70bb/resource/6800ea2d-371b-4b90-9cf1-994a467145fd/download/salk-kurum-ve-kurulularna-ait-bilgiler.json"
yanit=requests.get(adres).json()

#st.json(yanit)
veri=pd.DataFrame(yanit,columns=["MAHALLE","ADI","ALT_KATEGORI","ENLEM","BOYLAM"])
filtered_df = dataframe_explorer(veri, case=False)
st.dataframe(filtered_df, use_container_width=True)
filtered_df.rename(columns={"ENLEM": "lat","BOYLAM": "lon"},inplace=True)
st.map(filtered_df,color="#ff00ff")