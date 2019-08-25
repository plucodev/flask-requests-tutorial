import requests
import json

r = requests.get('http://192.168.10.139:5000/platinum')

print(r.status_code)

print(r.json)


r = requests.get('http://192.168.10.139:5000/platinum', stream=True)
for line in r.iter_lines():
    if line:
        print(json.loads(line))