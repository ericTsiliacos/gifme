from flask import Flask, render_template, request
import requests
import json
import url_builders

app = Flask(__name__)


@app.route("/")
def index():
    search = request.args.get('search')
    gif_url = url_builders.build_gif_url(search)
    response = requests.get(gif_url)
    data = json.loads(response.content)
    gify_url = data['data']['fixed_height_downsampled_url']

    return render_template('layout.html', gify_url=gify_url)


if __name__ == "__main__":
    app.run(debug=True)
