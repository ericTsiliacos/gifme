from flask import Flask, request
from flask.ext.cors import CORS
from flask.json import jsonify
import requests
import json
import url_builders

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return ""

@app.route("/search.json")
def search():
    search_term = request.args.get('term')
    gif_url = url_builders.build_gif_url(search_term)
    response = requests.get(gif_url)
    data = json.loads(response.content)
    gify_url = data['data']['fixed_height_downsampled_url']
    json_url = {"url": gify_url}

    return jsonify(json_url)

if __name__ == "__main__":
    app.run(debug=True)
