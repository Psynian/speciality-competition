import streamlit as st
import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = 'https://medical.hee.nhs.uk/medical-training-recruitment/medical-specialty-training/equality-and-diversity/equality-and-diversity-2023-recruitment-data/country-of-qualification-2023-recruitment-data'
#soup = BeautifulSoup(page.content, "html.parser")
#tables = pd.read_html(str(soup))

header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)


tables = pd.read_html(r.text)

st.title("🎈 My new apppppp")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(len(tables))

st.dataframe(tables[0])