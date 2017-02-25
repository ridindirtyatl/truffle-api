
from flask_wtf import Form
from wtforms.validators import DataRequired, Length, Regexp, NumberRange, required
from wtforms import TextField, FormField, IntegerField, FloatField, FileField, BooleanField, DateField, FieldList
from input_validators import multiple_of



class Aggregates(Form):
    
    avg_adherence_count = IntegerField(validators=[DataRequired(message="")])
    avg_passenger_count = IntegerField(validators=[DataRequired(message="")])
    max_adherence_count = IntegerField(validators=[DataRequired(message="")])
    max_passenger_count = IntegerField(validators=[DataRequired(message="")])
    min_adherence_count = IntegerField(validators=[DataRequired(message="")])
    min_passenger_count = IntegerField(validators=[DataRequired(message="")])
