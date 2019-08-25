import requests
import json

r = requests.get('https://api.github.com/users/plucodev')

print(r.status_code)

print(r.json)


r = requests.get('https://api.github.com/users/plucodev', stream=True)
for line in r.iter_lines():
    if line:
        print(json.loads(line))