from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'app_user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    login_id = Column(String(50), unique=True, nullable=False)
    horoscope_sign = Column(String(50))
    city = Column(String(50))
    watchlists = relationship('Watchlist', backref='user')

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = Column(Integer, primary_key=True)
    ticker_code = Column(String(10), nullable=False)
    ticker_name = Column(String(50), nullable=False)
    ticker_type = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('app_user.id'), nullable=False)
