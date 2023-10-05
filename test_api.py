#here I'll test the API
import requests
import json

#URL from my API Flask
api_url = 'http://localhost:5000/ner'

#create JSON files in order to use them as a test
input_data ={
    "sentences": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera.",
        "Esta es una prueba para Ingeniero de Aprendizaje Automático en Kosmos",
        "Las redes neuronales líquidas están listas para catapultar la inteligencia artificial. Palabra del MIT"
    ]
}

# make a POST request to the API Flask NER
response = requests.post(api_url, json=input_data)

# check if the request was execute successfully (code 200)
if response.status_code == 200:
    # check the response JSON
    result = response.json()
    print(json.dumps(result, indent=2, ensure_ascii = False))
else:
    print("Error en la solicitud:", response.status_code)
