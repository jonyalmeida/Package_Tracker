from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from ..map.map import map

choices = [(item, item) for item in list(map.keys())]


class ShippingForm(FlaskForm):
    sender_name = StringField('Sender name', validators=[DataRequired()])
    receiver_name = StringField('Receiver name', validators=[DataRequired()])
    origin = SelectField('Origin', choices=choices,
                         validators=[DataRequired()])
    destination = SelectField(
        'Destination', choices=choices, validators=[DataRequired()])
    is_express = BooleanField('Express', validators=[DataRequired()])
    submit_button = SubmitField('Submit', validators=[DataRequired()])
    cancel_button = SubmitField('Cancel', validators=[DataRequired()])
