import requests
import json
from pprint import pprint

url = 'https://randomuser.me/api/'
payload = {
    'results':10,
    'gender':'female'
}


res = requests.get(url=url,params=payload)
users = []

if res.status_code == 200:
    users_data = res.json()['results']
    for user in users_data:
        
        users.append(
            {
                'fullname': f"{user['name']['first']} {user['name']['last']}",
                'age': user['dob']['age'],
                'gender':user['gender'],
                'phone':user['phone'],
                'email':user['email'],
                'country':user['location']['country'],  
                'nat':user['nat']
            }
        )
with open('us9ers.json', 'w') as f:
    json.dump(users,f,indent=4)
    