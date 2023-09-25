from .database import db


class Tripplan(db.Model):
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    origin = db.Column(db.String(255), nullable=False)
    destination = db.Column(db.String(255), nullable=False)
    distance = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(255), nullable=False)
    ac_type = db.Column(db.String(255), nullable=False)
    dc_type = db.Column(db.String(255), nullable=False)
    ev = db.Column(db.String(255), nullable=False)
    elexa = db.Column(db.String(255), nullable=False)
    mea = db.Column(db.String(255), nullable=False)
    pea = db.Column(db.String(255), nullable=False)
    ea = db.Column(db.String(255), nullable=False)
    evolt = db.Column(db.String(255), nullable=False)
    mg = db.Column(db.String(255), nullable=False)

    def __init__(self, user_id, origin, destination, distance, duration, ac_type, dc_type, ev, elexa,
                 mea, pea, ea, evolt, mg):
        self.user_id = user_id,
        self.origin = origin,
        self.destination = destination,
        self.distance = distance,
        self.duration = duration,
        self.ac_type = ac_type,
        self.dc_type = dc_type,
        self.ev = ev,
        self.elexa = elexa,
        self.mea = mea,
        self.pea = pea,
        self.ea = ea,
        self.evolt = evolt,
        self.mg = mg,

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'origin': self.origin,
            'destination': self.destination,
            'distance': self.distance,
            'duration': self.duration,
            'ac_type': self.ac_type,
            'dc_type': self.dc_type,
            'ev': self.ev,
            'elexa': self.elexa,
            'mea': self.mea,
            'pea': self.pea,
            'ea': self.ea,
            'evolt': self.evolt,
            'mg': self.mg,
        }
