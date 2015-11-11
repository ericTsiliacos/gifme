from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route("/")
def hello():
    search = request.args.get('search')
    response = requests.get("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=%s" % search)
    data = json.loads(response.content)
    gify_url = data['data']['fixed_width_small_url']

    return render_template('layout.html', gify_url=gify_url)

if __name__ == "__main__":
    app.run(debug=True)
