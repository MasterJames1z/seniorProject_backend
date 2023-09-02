from .database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255),nullable=False)
    distance = db.Column(db.Integer)
    car = db.Column(db.String(255), nullable=False)
    battery = db.Column(db.Integer)

    def __init__(self, username, password,distance, car, battery):
        self.username = username
        self.password = password
        self.distance = distance
        self.car = car
        self.battery = battery

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'distance': self.distance,
            'car': self.car,
            'battery' : self.battery
        }
