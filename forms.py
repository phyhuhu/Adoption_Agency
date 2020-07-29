from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SelectField, RadioField,  BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, DataRequired, NumberRange, URL, Optional, Length

class AddPet(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30, message="Age should be between 0 and 30.")])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPet(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")