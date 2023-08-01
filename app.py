from flask import Flask, request, jsonify
import nltk
from nltk.corpus import wordnet

app = Flask(__name__)

nltk.download('wordnet')

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

@app.route("/get_synonyms")
def get_synonyms_api():
    word = request.args.get("word", "")
    synonyms_list = get_synonyms(word)
    return jsonify({"synonyms": synonyms_list})

if __name__ == "__main__":
    app.run(debug=True)
