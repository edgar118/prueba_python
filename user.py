import requests
import json

def created_data():
        url = "https://jsonplaceholder.typicode.com/users"

        payload = json.dumps({
                "name": "Antonio",
                "age": 59,
                "has_children": 15,
                "gender": "Undefined",
                "full_name": "Antonio acevedo bolivar",
                "studies": "Any",
                "job": "searching",
                "id": 11
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)

        return response.json()  

def fetch_data(id):
                 
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    return response.json()