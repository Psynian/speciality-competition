import streamlit as st
import requests
import pandas as pd

key = 'Specialty and level'
origins = ['UK','EU', 'Rest of the World']


@st.cache_resource
def get_data():
  url = 'https://medical.hee.nhs.uk/medical-training-recruitment/medical-specialty-training/equality-and-diversity/equality-and-diversity-2023-recruitment-data/country-of-qualification-2023-recruitment-data'
  header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}


  r = requests.get(url, headers=header)
  tables = pd.read_html(r.text)
  dump = [x.replace("<5","4",inplace=True) for x in tables]
  dump = [x.drop("Non medical",axis=1,inplace=True) for x in tables]
  dump = [table[x].astype('int64',copy=False) for x in origins for table in tables]
  dump = [table.set_index(key,inplace=True) for table in tables]
  return tables




st.dataframe(tables[0])
st.dataframe(tables[1])
st.dataframe(tables[2])
st.dataframe(tables[3])

st.write(tables[0].index)
st.write(tables[0].name)


