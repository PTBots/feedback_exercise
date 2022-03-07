from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect db to app"""

    db.app = app
    db.init_app(app)

class User(db.Model):
    
    __tablename__ = 'users'

    username = db.Column(
        db.String(20),
        nullable = False,
        unique = True,
        primary_key = True
    )
    password = db.Column(db.String(), nullable = False)
    email = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)

    feedback = db.relationship("Feedback", backref="user", cascade="all, delete-orphan")

    @classmethod
    def register(cls, username, password, first_name, last_name, email):
        """Register a new user, hash their password"""

        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode("utf8")
        user = cls(
            username = username,
            password = hashed_utf8,
            email = email,
            first_name = first_name,
            last_name = last_name
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """comapre username and password to what is stored in the database"""

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

class Feedback(db.Model):
    """Feedback"""

    __tablename__= "feedback"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.Text, nullable = False)
    username = db.Column(
        db.String,
        db.ForeignKey('user.username'),
        nullable = False
    )