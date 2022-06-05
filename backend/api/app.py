# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "<h3>Hello World<h3>"


# @app.route('/members')
# def members():
#     return {"members": ["Member1", "Member2", "Member3"]}

# if __name__ == '__main__':
#     app.run(debug=True)




# import os
# from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
# from flask_migrate import Migrate
# from flask_cors import CORS, cross_origin
# import requests
# import json


# ENV = os.getenv("FLASK_ENV")
# static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../public/')

# app = Flask(__name__)
# ma = Marshmallow(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
# app.config['CORS_HEADERS'] = "Content-Type"

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# MIGRATE = Migrate(app, db)
# db.init_app(app)

# cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

# from api.models import db, User, Beer, BeerDetails

#remember to put 2 empty lines between functions
#cut routes from here and moved them to api/routes


# @app.route('/all_beers_list', methods=["POST"])
# def save_beers():
#     content = request.get_json(silent=True)
#     beer_id = content["id"]
#     r = requests.get_json(beer_id)
#     response = r.json()

#     beer = Beer(id = response["id"], name = response["name"])

#     db.session.add(beer)
#     db.session.commit()

#     return jsonify(beer.serialize()), 200

# if __name__ == '__main__':
#     app.run()