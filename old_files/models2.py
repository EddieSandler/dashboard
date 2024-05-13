from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
db = SQLAlchemy()
bcrypt = Bcrypt()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'app_user'
    id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String(50))
    last_name = Column(String(50))
    user_name =Column(String(50))
    login_id = Column(String(50), unique=True, nullable=False)
    horoscope_sign = Column(String(50))
    city = Column(String(50))
    watchlists = relationship('Watchlist', backref='user')

    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    ticker_id = Column(Integer, primary_key=True)
    ticker_code = Column(String(10), nullable=False)
    ticker_name = Column(String(50), nullable=False)
    ticker_type = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('app_user.id'), nullable=False)
