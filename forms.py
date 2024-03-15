from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class AddNewPetForm(FlaskForm):
    """form for adding new pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Pet Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[optional(), URL()])
    age = IntegerField("Pet Age", validators=[optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Additional Notes", validators=[optional()])

class EditPetForm(FlaskForm):
    """form for editing existing pet"""

    photo_url = StringField("Photo URL", validators=[optional(), URL()])
    notes = TextAreaField("Additional Notes", validators=[optional()])
    available = BooleanField("Pet Availability")
