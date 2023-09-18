import requests
import streamlit as st
import datetime

url = 'https://api-hogwarts.vercel.app/coin?coin='

today = datetime.datetime.now()
st.write('Your birthday is:', today)

url +=str(today)
x = requests.post(url)


st.title(x.text)