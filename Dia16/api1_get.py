import requests, json


url = "https://jsonplaceholder.typicode.com/posts"

payload = {} # Datos que seran enviados
headers = {}

#response = requests.request("GET", url, headers=headers, data=payload)

response = requests.get(url) # otro metodo

print("")
print(response) # <Response [200]> codigo

if response.status_code == 200:
    print(response.text) #-> esto convierte la respuesta en un string
    respuesta = json.loads(response.text)
    print(type(respuesta))
    for posicion, dicc in enumerate(respuesta):
        print(f"diccionario {posicion} {dicc}")
    
else :
    print(f"Error en la solicitud código : {response.status_code}")