import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "email": "ignacio.pizarro@reqres.in",
  "first_name": "Ignacio",
  "profesion": "Profesor",
  "avatar": "https://reqres.in/img/faces/1-image.jpg"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print("")

if response.status_code == 201: #Created -> creación exitosa 
    print("Usuario creado exitosamente")
    respuesta = response.json()
    created_user = respuesta
    print(created_user)
    print("")
else:
    print("Error en la creación del post")