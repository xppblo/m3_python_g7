import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {} # Datos que seran enviados
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#response = requests.get(url)  otro metodo

print("")
print(response) # <Response [200]> codigo

if response.status_code == 200:
    #print(response.text) -> esto convierte la respuesta en un string
    print(response.json()) # La respuesta la convierte en un json
    respuesta = response.json()
    print("")
    print(respuesta["title"])
    for clave, valor in respuesta.items():
        print(f"clave {clave} - valor {valor}")
    
else :
    print(f"Error en la solicitud código : {response.status_code}")