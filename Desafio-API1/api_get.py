import requests

url = "https://reqres.in/api/users"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    #print(response.json())  La respuesta la convierte en un json
    respuesta = response.json()
    print("")    
    user_data = respuesta['data']   
    print(user_data)
    
else :
    print(f"Error en la solicitud código : {response.status_code}")