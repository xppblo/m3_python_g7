import requests
import json

url = "https://reqres.in/api/users"

payload = json.dumps({
  "id": 6
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)
print("")
if response.status_code == 204: #-> La respuesta el servidor la recibe correctamente  y no devuelve contenido adicional
    print(f"Se elimino correctamente el usuario codigo : {response.status_code}")
    codigo_eliminado = response.status_code
    print("")
else:
    print(f"No se ha podido eliminar correctamente  el usuario, codigo : {response.status_code}")
    