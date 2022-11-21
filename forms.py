from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length,Email, ValidationError
from __main__ import contact
    


class Addform(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(min=2,max=20)])
    email=StringField('Email',validators=[Email()])
    number = StringField('Mobile No.', validators=[DataRequired(), Length(min=10,max=10)])
    submit=SubmitField('Submit')
    def validate_number(self,number):
        if (not (number.data).isnumeric()):
            raise ValidationError('Enter Valid Number')
        else:
            if contact:
                for i,j in contact.items():
                    if (number.data == j[1]):
                        raise ValidationError('Number already exists in Repository')

            


        

    
