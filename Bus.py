
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of



class Bus(Form):
    
    actual_passenger_count = IntegerField(validators=[DataRequired(message="")])
    adherence = IntegerField(validators=[DataRequired(message="")])
    destination = TextField(validators=[DataRequired(message="")])
    next_stop = TextField(validators=[DataRequired(message="")])
    prev_stop = TextField(validators=[DataRequired(message="")])
    route_id = IntegerField(validators=[DataRequired(message="")])
    vehicle_id = IntegerField(validators=[DataRequired(message="")])
