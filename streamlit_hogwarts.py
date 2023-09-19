import requests
import streamlit as st
import datetime

url = 'https://api-hogwarts.vercel.app/coin?coin='


start_date = datetime.date(year=1950,month=1,day=1)
end_date = datetime.datetime.now().date()
d = st.date_input("When's your birthday", min_value=start_date,max_value= end_date)
var='Your birthday is:'+str(d)
st.write(var, d)

url +=str(d)
x = requests.post(url)


st.title(x.text)