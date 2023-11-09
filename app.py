import json

import bcrypt
from flask import Flask, jsonify, request
from flask_cors import CORS
# from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy_utils.functions import database_exists, create_database

# from controllers import authController
from controllers.authController import AuthController
# from controllers.compareController import CompareController
from models import User
from models.data import Tripplan
from models.database import db
from routes.auth_bp import AuthBlueprint
# from routes.compare_bp import CompareBlueprint

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
app.config.from_object('config')

if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
    print('Creating a database')
    create_database(app.config["SQLALCHEMY_DATABASE_URI"])

db.init_app(app)
with app.app_context():
    db.create_all()

class FlaskApp:
    app.register_blueprint(AuthBlueprint.auth_bp)
    # app.register_blueprint(CompareBlueprint.compare_bp)

@app.route('/login', methods=['POST'])
def AuthLogin():
    return AuthController.auth()

@app.route('/auth/register', methods=['POST'])
def register():
    try:
        username = request.get_json()['username']
        password = request.get_json()['password']
        distance = request.get_json()['distance']
        car = request.get_json()['car']
        battery = request.get_json()['battery']

        # Check if the username already exists in the user table
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return jsonify({'message': 'Username already exists'}), 400

        # Create a new user
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(username=username, password=hashed_password, distance=distance, car=car, battery=battery)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Registration successful'}), 201

    except KeyError:
        return jsonify({'message': 'The request body requires username and password'}), 400


@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test route is working"})

@app.route('/items', methods=['GET', 'POST'])
def items():
    user_id = request.json['user_id']
    origin = request.json['origin']
    destination = request.json['destination']
    distance = request.json['distance']
    duration = request.json['duration']
    ac_type = request.json['ac_type']
    dc_type = request.json['dc_type']
    ev = request.json['ev']
    elexa = request.json['elexa']
    mea = request.json['mea']
    pea = request.json['pea']
    ea = request.json['ea']
    evolt = request.json['evolt']
    mg = request.json['mg']

    print(user_id, origin, distance, duration,destination, ac_type, dc_type, ev, elexa, mea, pea, ea, evolt, mg)

    db.session.add(Tripplan(user_id=user_id, origin=origin, distance=distance, duration=duration,destination=destination, ac_type=ac_type,
                            dc_type=dc_type, ev=ev, elexa=elexa, mea=mea, pea=pea, ea=ea, evolt=evolt, mg=mg))
    db.session.commit()
    return "keep it"

@app.route('/get_list_tripplan',methods=['POST'])
def get_items():
    user_id = request.json['user_id']
    print(user_id)
    data = Tripplan.query.filter_by(user_id=user_id).all()
    data_serialize = [item.serialize for item in data]
    for item in data_serialize:
        print(item)
    return data_serialize

# @app.route('/summary', method=['POST'])
# def compare():
#     return CompareController.addCost()

if __name__ == '__main__':
    app.run(debug=False)