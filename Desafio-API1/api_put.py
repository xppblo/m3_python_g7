import requests
import json

url = "https://reqres.in/api/users/2"

payload = json.dumps({
  "name": "morpheus",
  "residence": "zion"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

if response.status_code == 200:
    respuesta = response.json()
    print("")
    updated_user = respuesta
    print(f"Usuario modificado correctamente : {updated_user}")
else:
    print(f"Error, no se puede actualizar el usuario codigo : {response.status_code}")
