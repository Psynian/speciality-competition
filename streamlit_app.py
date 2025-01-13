import streamlit as st
import requests
import pandas as pd

key = 'Specialty and level'
origins = ['UK','EU', 'Rest of the World']
table_names = ['Applications made','Appointable applicants','Offers mades','Offers accepted']

@st.cache_resource
def get_data():

  data = {}

  url = 'https://medical.hee.nhs.uk/medical-training-recruitment/medical-specialty-training/equality-and-diversity/equality-and-diversity-2023-recruitment-data/country-of-qualification-2023-recruitment-data'
  header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

  r = requests.get(url, headers=header)
  tables = pd.read_html(r.text)
  dump = [x.replace("<5","4",inplace=True) for x in tables]
  dump = [x.drop("Non medical",axis=1,inplace=True) for x in tables]
  dump = [table.set_index(key,inplace=True) for table in tables]

  for x in range(len(tables)):
      tables[x].attrs['name'] = table_names[x]
      data[table_names[x]] = tables[x].astype('int')
  return data

data = get_data()

st.set_page_config(layout="wide")

numerator = st.selectbox(
    "Numerator",
    data.keys(),
)

denominator = st.selectbox(
   "Denominator",index='Appointable applicants',
   data.keys()
)
   
st.write("Competition Ratios: " + numerator + "/" + denominator)
competition = data[numerator]/data[denominator]
competition['UK vs Rest of the World'] = competition[origins[2]]/ competition[origins[0]]
st.dataframe(competition)

st.bar_chart(competition,y='UK vs Rest of the World')


col1, col2 = st.columns(2)

with col1:
   st.write(numerator)
   st.dataframe(data[numerator])
with col2:
  st.write(denominator)
  st.dataframe(data[denominator])