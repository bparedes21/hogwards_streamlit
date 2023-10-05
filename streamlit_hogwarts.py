from os import error
import requests
import streamlit as st
import datetime
import json
from PIL import Image
from io import BytesIO

url = 'https://api-hogwarts.vercel.app/CasaHogward?fecha='
url_casa="https://api-hogwarts.vercel.app/CasaHogward?fecha="

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
    house_ho=response_dict["CASA"]
    House_propertie=response_dict["caracteristicas"]
    image_name=response_dict["nombre_img"]
    color_font=response_dict["color_font"]

    caption_var=house_ho
    Casa_ho=house_ho

    significado_casa=House_propertie
    color_text=color_font
    

    url1="https://api-hogwarts.vercel.app/img_casa?casa_="+image_name
    r = requests.post(url1,stream=True)
    image = Image.open(BytesIO(r.content))
    

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
    
    url_harry="https://api-hogwarts.vercel.app/img_harry/"
    r = requests.get(url_harry,stream=True)
    image = Image.open(BytesIO(r.content))
    image_new=image.resize((400,400))
    st.image(image_new, caption='HP')
 
    if boton_escudo:
        with col2:
        
            image_new=image.resize((350,400))
            st.image(image_new, caption=caption_var)
       
        
            var='La fecha elegida es: '+str(d)
            st.write(var)
            num_casa=str(num_casa)
            st.write("El resultado de la suma de la fecha de nacimiento es :eyeglasses: :"+color_text+"["+num_casa+"]")

if boton_significado:
    boton_escudo=False
    with col2:
        st.write("La casa de HOGWARTS es ✨ :")
        st.caption(":"+color_text+"["+Casa_ho+"]")
        #https://gist.github.com/rxaviers/7360908
      
        
    
        st.write(":"+color_text+"["+Casa_ho+"] representa 🎇:")
        st.caption(":"+color_text+"["+significado_casa+"]")    
