import requests
import json

url = "https://jsonplaceholder.typicode.com/posts/1"

payload = json.dumps({
  "userId": 1,
  "title": "modificando los datos mi pana",
  "body": "esto se ha modificado mi pana"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)