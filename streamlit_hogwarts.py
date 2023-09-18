import requests
import streamlit as st
import datetime

url = 'https://api-hogwarts.vercel.app/coin?coin='

today = datetime.datetime.now()
d = st.date_input("When's your birthday", datetime.date(today))

st.write('Your birthday is:', d)
url +=str(d)
x = requests.post(url)


st.title(x.text)