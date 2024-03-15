from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    app.app_context().push()
    db.app = app
    db.init_app(app)

DEFAULT_PHOTO_URL = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

class Pet(db.Model):
    """pets that are potentially up for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          default=True,
                          nullable=False)
    
    def image_url(self):
        """returns an image url for pet"""
        return self.photo_url or DEFAULT_PHOTO_URL