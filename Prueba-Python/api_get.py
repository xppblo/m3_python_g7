import requests

def get_aves():
    response = requests.get('https://aves.ninjas.cl/api/birds')
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos de las aves")
        return None
