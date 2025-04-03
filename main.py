from flask import Flask, render_template
import requests

app = Flask(__name__)

# Replace this URL with your own npoint.io endpoint if needed
API_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"

@app.route('/')
def index():
    response = requests.get(API_ENDPOINT)
    posts = response.json()  # Expecting a list of post dictionaries
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
