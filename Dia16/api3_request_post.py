import requests,json

url = "https://jsonplaceholder.typicode.com/posts"

payload = json.dumps({
    "userId": 1,
    "title": "estamos haciendo un post con postman",
    "body": "esto es un ejemplo de post"
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)