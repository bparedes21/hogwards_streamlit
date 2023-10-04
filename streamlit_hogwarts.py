from os import error
import requests
import streamlit as st
import datetime
import json
from PIL import Image
url = 'https://api-hogwarts.vercel.app/CasaHogward?fecha='


start_date = datetime.date(year=1950,month=1,day=1)
end_date = datetime.datetime.now().date()
st.header("Enterate a que casa de HOGWARTS perteneces :european_castle:")

d = st.date_input("Ingresa tu fecha de nacimiento :baby:", min_value=start_date,max_value= end_date,value=None)

    
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
    col4, col5 = st.columns(2)

    with col1:
        st.write(' ')

    with col2:
        boton_escudo=st.button('Mostrar escudo ')
        boton_significado=st.button('Mostrar significado ')

    with col3:
        st.write(' ')
except ValueError as error:
    
    image = Image.open('harry-potter-broom-png.png')
    image_new=image.resize((400,400))
    st.image(image_new, caption='HP')

if(num_casa==1)or(num_casa==5)or(num_casa==9):
    image = Image.open('gry.png')
    
    caption_var='Gryffindor'
    Casa_ho="Gryffindor"

    significado_casa="Valentía, coraje y determinación"
    color_text="red"
        
elif(num_casa==2)or(num_casa==6):
    image = Image.open("hu.png")
    caption_var='Hufflepuff'

    Casa_ho="Hufflepuff"
    significado_casa="Lealtad, paciencia y trabajo duro."
    color_text="gray"

elif(num_casa==3)or(num_casa==7):
    image = Image.open("ra.png")
    
    caption_var='Ravenclaw'

    Casa_ho="Ravenclaw"
    significado_casa="Inteligencia, sabiduría y creatividad. Asociados a los números"
    color_text="blue"

elif(num_casa==4)or(num_casa==8):
    image = Image.open("sly.png")
    caption_var='Slytherin'
    
    
    Casa_ho="Slytherin"
    significado_casa="Astucia, ambición y determinación."
    color_text="green"

  
    if boton_escudo:
        with col2:
        
            image_new=image.resize((350,400))
            st.image(image_new, caption=caption_var)
       
        
            var='La fecha elegida es: '+str(d)
            st.write(var)
            num_casa=str(num_casa)
            st.write("El resultado de la suma de la fecha de nacimiento es :eyeglasses::")
       
            st.caption(":"+color_text+"["+num_casa+"]")


if boton_significado:
    boton_escudo=False
    with col2:
        st.write("La casa correspondiente es ✨ :")
        st.caption(":"+color_text+"["+Casa_ho+"]")
        #https://gist.github.com/rxaviers/7360908
      
        
    
        st.write("La casa representa 🎇:")
        st.caption(":"+color_text+"["+significado_casa+"]")    

        
       