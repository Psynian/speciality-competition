import streamlit as st
import requests
from bs4 import BeautifulSoup

URL = "https://medical.hee.nhs.uk/medical-training-recruitment/medical-specialty-training/equality-and-diversity/equality-and-diversity-2023-recruitment-data/country-of-qualification-2023-recruitment-data"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

tables = pd.read_html(str(soup))



st.title("🎈 My new apppppp")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.write(len(tables))

st.dataframe(tables[0])