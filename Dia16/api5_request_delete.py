import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)