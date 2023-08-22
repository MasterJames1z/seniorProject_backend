import bcrypt

from models.user import User
from sqlalchemy import event
from .database import db


@event.listens_for(User.__table__, 'after_create')
def create_user(*args, **kwargs):
    db.session.add(User(username='user', password=bcrypt.hashpw('password'.encode('utf-8'),bcrypt.gensalt(10)),distance='440'))
    db.session.add(User(username='user01', password=bcrypt.hashpw('user01'.encode('utf-8'), bcrypt.gensalt(10)), distance='380'))
    db.session.commit()