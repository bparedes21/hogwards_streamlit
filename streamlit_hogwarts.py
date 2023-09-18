import requests
url = 'https://api-hogwarts.vercel.app/coin?coin='
url += "{'coin': 'somevalue'}"
x = requests.post(url)


st.title(x.text)