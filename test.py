import requests

BASE_URL = 'http://127.0.0.1:5000/metadecks'

response = requests.get(BASE_URL+'/modern')
data=response.json()['data']

print(data[0]['decks'])


print(response.headers)
print(response.status_code)