from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jenks!0429@localhost/brewbrowser'
db = SQLAlchemy(app)

class Beer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'Beer: {self.name}'

    def __init__(self, name):
        self.name = name


def format_beer(beer):
    return {
        "id": beer.id,
        "name": beer.name,
        "description": beer.description
    }

# @app.route('/beers', methods=["POST"])
# def create_beers():
#     name = request.json['name']
#     description = request.json['description']
#     beer = Beer(name, description)
#     db.session.add(beer)
#     db.session.commit()

#     return format_beer(beer)




@app.route('/')
def hello_world():
    return "<h3>Hello World<h3>"


@app.route('/all_beers', methods=["GET"])
# @cross_origin()
def get_all_beers():
    url = "https://api.catalog.beer/beer"
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Basic NTFjODNhNDctODEwOS00YTEyLTlkMjctNDM1MjA1YTEzZDgzOg=='
        }
    response = requests.request("GET", url, headers=headers, data=payload)
    response.json()

    return jsonify(response.json())

@app.route('/abeer', methods=["GET"])
def get_single_beer():
    beer_id = request.args.get('beer_id')
    r = requests.get(f'https://api.catalog.beer/beer/{beer_id}')
    response = r.json()

    return jsonify(response[{}]), 200


# def get_beer_deets():


if __name__ == '__main__':
    app.run(debug=True)