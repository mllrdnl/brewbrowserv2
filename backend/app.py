from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests
import json
from models import db, User, Beer, BeerDetails


app = Flask(__name__)
# CORS(app, resources={r"/api/*":{"origins":"http://127.0.0.1:5000/"}})
app.config['CORS_HEADERS'] = "Content-Type"

cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

#remember to put 2 empty lines between functions
@app.route('/')
def hello_world():
    return ('Hello World!')


@app.route('/super_simple')
def super_simple():
    return jsonify({"message": 'Super Simple'}), 200


@app.route('/not_found')
def not_found():
    return jsonify({"message": "That resource was not found!"}), 404


@app.route('/all_beers', methods=["GET"])
@cross_origin()
def get_all_beers():
    url = "https://api.catalog.beer/beer"
    payload={}
    headers = {
        'accept': 'application/json',
        'Authorization': 'Basic NTFjODNhNDctODEwOS00YTEyLTlkMjctNDM1MjA1YTEzZDgzOg=='
        }
    response = requests.request("GET", url, headers=headers, data=payload)
    response.json()

    # print(response.text)
    return jsonify(response.json())


@app.route('/all_beers_list', methods=["POST"])
def save_beers():
    content = request.get_json(silent=True)
    beer_id = content["id"]
    r = requests.get_json(beer_id)
    response = r.json()

    beer = Beer(id = response["id"], name = response["name"])

    db.session.add(beer)
    db.session.commit()

    return jsonify(beer.serialize()), 200




if __name__ == '__main__':
    app.run()