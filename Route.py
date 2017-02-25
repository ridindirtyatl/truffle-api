
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of

from Aggregates import Aggregates


class Route(Form):
    
    aggregates = FormField(Aggregates)
    vehicle_list = FieldList(IntegerField('vehicle_list', [required()]), DataRequired(message=""))
