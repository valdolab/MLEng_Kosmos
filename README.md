# MLEng Challenge for Kosmos

Objetivo: Crear una API REST sencilla que reciba una lista de oraciones en español y devuelva una lista de las entidades nombradas identificadas en cada oración.
Requisitos:
1. La API debe estar escrita en Python usando el microframework Flask.
2. Usa la biblioteca Spacy para el reconocimiento de entidades nombradas (NER), (asegúrate de usar el modelo 'es_core_news_sm' para español.)
3. La API debe aceptar una petición POST que contenga un JSON con una lista de oraciones en español.

```bash
git clone https://github.com/valdolab/MLEng_Kosmos.git
```

## Prerequisites and Installation
List any prerequisites or dependencies that need to be installed before running the app.

Install the required dependencies:
```bash
pip install -r requirements.txt
```
Download the spacy model running the .sh file
```bash
download_spacy_model.sh
```

## Usage
```bash
python app.py
```

## Test the Flask API
```bash
python test_api.py
```
## Examples
