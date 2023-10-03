from os import error
import requests
import streamlit as st
import datetime
import json
from PIL import Image
url = 'https://api-hogwarts.vercel.app/CasaHogward?fecha='


start_date = datetime.date(year=1950,month=1,day=1)
end_date = datetime.datetime.now().date()

d = st.date_input("Ingresa tu fecha de nacimiento :baby:", min_value=start_date,max_value= end_date,value=None)
if (d!=None):
    var='La fecha elegida es: '+str(d)
    st.write(var)
##enlace + fecha de para el post
url +=str(d)
response= requests.post(url)
boton_escudo=False
boton_significado=False
num_casa=0
response_dict=0
try:
    response_dict = json.loads(response.text)
    num_casa=int(response_dict["CASA"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(' ')

    with col2:
        boton_escudo=st.button('Mostrar escudo ')
        boton_significado=st.button('Mostrar significado :eyeglasses:')

    with col3:
        st.write(' ')
except ValueError as error:
    
    image = Image.open('harry-potter-broom-png.png')
    image_new=image.resize((400,400))
    st.image(image_new, caption='HP')

if(num_casa==1)or(num_casa==5)or(num_casa==9):
        image = Image.open('gry.png')
       
        scaption_var='Gryffindor'
        Casa_ho="Gryffindor"

        significado_casa="Valentía, coraje y determinación"
        
elif(num_casa==2)or(num_casa==6):
    image = Image.open("hu.png")
    caption_var='Hufflepuff'

    Casa_ho="Hufflepuff"
    significado_casa="Lealtad, paciencia y trabajo duro."

elif(num_casa==3)or(num_casa==7):
    image = Image.open("ra.png")
    
    caption_var='Ravenclaw'

    Casa_ho="Ravenclaw"
    significado_casa="Inteligencia, sabiduría y creatividad. Asociados a los números"
elif(num_casa==4)or(num_casa==8):
    image = Image.open("sly.png")
    caption_var='Slytherin'
    
    
    Casa_ho="Slytherin"
    significado_casa="Astucia, ambición y determinación."

if boton_escudo:
    with col2:
        
        image_new=image.resize((350,400))
        st.image(image_new, caption=caption_var)

if boton_significado:
    boton_escudo=False
    with col2:
        num_casa=str(num_casa)
        st.header("El resultado de la suma de la fecha de nacimiento es: "+num_casa)

        st.header("La casa correspondiente es: "+Casa_ho)
        #https://gist.github.com/rxaviers/7360908
        st.header("La casa representa: "+significado_casa)