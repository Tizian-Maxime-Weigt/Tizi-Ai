import requests
import json
import os

url = 'http://localhost:5000/chat'

headers = {'Content-Type': 'application/json'}
os.system('clear')
prompt = input('Schreibe hier deine Frage: ')

data = {
    'model': 'gpt-3.5-turbo',
    'provider': 'tiziai.Provider.GetGpt',
    'messages': [
        {'role': 'user', 'content': prompt}
    ]
}

os.system('clear')

print("Warte Kurz...")

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    os.system('clear')
    print()
    print(result)
    print()
else:
    print('Error:', response.status_code)
