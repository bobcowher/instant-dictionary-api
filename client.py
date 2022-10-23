import requests

req = requests.get(f"http://localhost:8000/api?w=moon")

data = req.json()

print(data['definition'])