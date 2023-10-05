from flask import Flask, request, jsonify
import spacy


app = Flask(__name__)
nlp = spacy.load("es_core_news_sm")

@app.route('/ner', methods=['POST'])
def get_entity_name():
    #add a try Exception
    try:
        #get the sentences from the request body in JSON format
        data = request.get_json()
        sentences = data['sentences']

        #initializes a list to store the results
        result = []

        #process each sentence and perform entity recognition NER
        for sentence in sentences:
            doc = nlp(sentence)
            entities = {}

            #get the identified entities along with their types
            for entity in doc.ents:
                entities[entity.text] = entity.label_

            #add the result to the list
            result.append({
                "sentence": sentence,
                "entity": entities
            })

        #returns the results as a JSON response
        return jsonify({"resultado": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    #app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)

