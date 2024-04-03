import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "userId": 1,
    "title": "estamos haciendo un post con postman",
    "body": "esto es un ejemplo de post"
}


response = requests.post(url, json=payload)

if response.status_code == 201: #Created -> creación exitosa 
    print("Inserción exitosa")
    print(response.text)
else:
    print("Error en la creación del post")