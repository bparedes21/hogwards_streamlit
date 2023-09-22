from os import error
import requests
import streamlit as st
import datetime
import json
from PIL import Image
url = 'https://api-hogwarts.vercel.app/CasaHogward?fecha='


start_date = datetime.date(year=1950,month=1,day=1)
end_date = datetime.datetime.now().date()
d = st.date_input("When's your birthday", min_value=start_date,max_value= end_date,value=None)
var='La feccha elegida es: '+str(d)
st.write(var)
##enlace + fecha de para el post
url +=str(d)
response= requests.post(url)

num_casa=0
response_dict=0
try:
    response_dict = json.loads(response.text)
    num_casa=int(response_dict["CASA"])
except ValueError as error:
    
    image = Image.open('harry-potter-broom-png.png')
    st.image(image, caption='Sunrise by the mountains')


if(num_casa==1)or(num_casa==5)or(num_casa==9):
    Casa_ho="Gryffindor"

    significado_casa="Valentía, coraje y determinación."
    

    
elif(num_casa==2)or(num_casa==6):
    Casa_ho="Hufflepuff"
    significado_casa="Lealtad, paciencia y trabajo duro."
elif(num_casa==3)or(num_casa==7):
    Casa_ho="Ravenclaw"
    significado_casa="Inteligencia, sabiduría y creatividad. Asociados a los números"
elif(num_casa==4)or(num_casa==8):
    Casa_ho="Slytherin"
    significado_casa="Astucia, ambición y determinación."
if(num_casa!=0):
    num_casa=str(num_casa)
    st.title("El resultado de la suma de la fecha de nacimiento es: "+num_casa)

    st.title("La casa correspondiente es: "+Casa_ho)
    #https://gist.github.com/rxaviers/7360908
    st.title("La casa representa: "+significado_casa)