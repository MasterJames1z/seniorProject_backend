from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from models import db
from models.data import Tripplan


class ItemController:
    @staticmethod
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

        print(user_id,origin,distance,destination,duration,ac_type,dc_type,ev,elexa,mea,pea,ea,evolt,mg)

        db.session.add(Tripplan(user_id=user_id,origin=origin,distance=distance,duration=duration,destination=destination,ac_type=ac_type,dc_type=dc_type,ev=ev,elexa=elexa,mea=mea,pea=pea,ea=ea,evolt=evolt,mg=mg))
        db.session.commit()
        return  "keep it"

    @staticmethod
    def get_items():
        user_id = request.json['user_id']
        data = Tripplan.query.filter_by(user_id=user_id)
        data_serialize = data.serialize
        print(data_serialize)

        return "return"