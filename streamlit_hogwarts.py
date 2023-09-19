import requests
import streamlit as st
import datetime
import json
url = 'https://api-hogwarts.vercel.app/CasaHogward?fecha='


start_date = datetime.date(year=1950,month=1,day=1)
end_date = datetime.datetime.now().date()
d = st.date_input("When's your birthday", min_value=start_date,max_value= end_date)
var='La feccha elegida es: '+str(d)
st.write(var)
##enlace + fecha de para el post
url +=str(d)
response= requests.post(url)

response_dict = json.loads(response.text)
num_casa=response_dict["CASA"]
st.title(num_casa)