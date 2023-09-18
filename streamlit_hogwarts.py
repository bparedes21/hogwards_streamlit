import requests
import streamlit as st
import datetime

url = 'https://api-hogwarts.vercel.app/coin?coin='


start_date = datetime.date(year=1950,month=1,day=1)
end_date = datetime.datetime.now().date()
d = st.date_input("When's your birthday", end_date)
st.write('Your birthday is:', d)

url +=str(end_date)
x = requests.post(url)


st.title(x.text)