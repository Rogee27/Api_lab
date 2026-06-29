import requests
import json

url = "http://127.0.0.1:5000/catalogo"

payload = json.dumps({
  "Producto": "Batería inalámbrica",
  "Precio": 44.5,
  "Stock": 4
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
