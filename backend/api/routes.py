from flask import Flask, request, jsonify
import requests
import json
from models import db, User, Beer, BeerDetails
from app import app
from flask_cors import CORS, cross_origin

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

    return jsonify(response.json())


# if __name__ == '__main__':
#     app.run()