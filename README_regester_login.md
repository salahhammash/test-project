### PIP INSTALL flask-wtf

open new py page -> forms.py, 

from flask_wtf import FlaskForm

<br>


we will do some classes
inside it we be have some fildes (7o8ol) like user name & password --> this fildes is classes that we can fined it inside wtforms

from wtforms import StringField

<br>

# REGISTRATION 

class RegistrationForm(FlaskForm):

    firstname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
<br>

#### ** StringField(this class take 2 argument ** ->

a- label that told the user what is this field for  "First Name",

b-validators : its some conditions that we put for inputs  -->
-- DataRequired() this for tell the user that its nessusery filde and cant be emptt .
-- Length(min=2, max=25) : this to let the username minimum 2 charachter & max 25 )

<br>

#### also do the same for last name & user name :

### from wtforms.validators import DataRequired, Length,
 firstname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )


but for email :
### from wtforms.validators import DataRequired, Length,Email 
 email = StringField("Email", validators=[DataRequired(), Email()])


<br>
 
 we need to : pip install email_validator

 for password :
 from wtforms import StringField, PasswordField

 ### from wtforms.validators import DataRequired, Length, Regexp, EqualTo ,Email

  password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )

# login

for login :

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")

# go back to the  main python file 
### dont forget to do this step in the 
from forms import RegistrationForm,LoginForm

### do the routes 




<br>

app.config[
    "SECRET_KEY"
] = '149f4d353e32ee77aca7b0fd0fc12d1afa9d2a19106b61da284452fa6a17ceed'
#secret key : will protect our website from csrf(cross side request furgery ) will not allowed any one to do any changes in the coockis that related to the setion 
#by open terminal and write python then hit enter -->import secrets -->secrets0token_hex(32) [32 is the number of characters]


# regster.html
