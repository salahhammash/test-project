* when the  user creat an account he will need an password & he will store his info in the data base , but its not secure to store the paswoord in the Data base cuz if any haker can do hacking in our db --> he can see the password 

* so we will do a hashing for password that come from the user and saving the hashing inside the DATA BASe

((  pip install flask-bcrypt  ))

an  explain with example :
[
then open the terminal -> python 
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()
* now we have an inctence from the class Bcrypt

* to do a hash for a string :
hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')

[decode('utf-8') --> to change to string]
* to cheak if the password that the user enterd is correct (if hashedpasword is = pasword) :
bcrypt.check_password_hash(hashed_password ,'password')
--> if its correct it will print True 
but if i wrot as an example :
bcrypt.check_password_hash(hashed_password ,'password123') -> it will give me false 

then exit()

]

now :
go to the p.py -> __init__.py :
as we did in the terminal :
* pip install flask-bcrypt 

* from flask_bcrypt import Bcrypt

* bcrypt = Bcrypt(app)

--> go to routes.py 
in the regester & login :
actualy in the routes ther is a dumy data & we arent store the ino inside the database ,inside the form & the module

so cuz of that we will do the user when the user do a regestration we will set it as an obj and store it inside the DB
---------------------
-----------------------
#  solution steps
* from new import app ,bcrypt,db 
( we need the inctence of Bcrypt() & SQLAlchemy(app)--> we give them a variable  bcrypt,db )

* inside the --> if form.validate_on_submit(): & befor the flash
hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

this is mean : take the data that the user has interd in the password field  

after hashed_password

* user=User(fname=form.fname.data , lname=form.lname.data,
username=form.username.data,
email=form.email.data,
password=hashed_password,)

after addin the user 
db.session.add(user)
db.session.commit

after that countinue --->
flash(f"Account created successfully for {form.username.data}", "success") ......
..... as we wrote in the regester rout 

## to cheak if the user that we created has been stored in the DB :
in our websit try to do a regestration then 

in terminal 
python
from new import db
from new import user
user = User.query.first
user.password :--> it should give us an hashed password 
exit()


### WT-form has an method to catch errors :

## go to forms.py

* in the end of class registation :
* after the submit 

to cheak if the user name is unice

* from new.models import User
& from wtforms.validators import ValidationError

example :
def validate_field(self,field):
[ field = the name of the field that we want to do a validation on it ]
    if true :
        raise ValidationError('Validation Message')

now we will do this for evrey field we want to do a validation on it ,
to cheak if the user name is unice :

* def validate_username(self,username):

 from wtforms.validators import ValidationError

we will cheak if we have a user has this user name :

    user = User.query,filter_by(username.data).first()
{do a from new.models import User}

    if user : --> its mean if true that we have a user name in the Db as you entered :
    if user:
        raise ValidationError('USER NAME ALREADY EXIST CHOSS DEFRENT ONE ')

* a nouther on for email 
def validate_email(self,email):
    user = User.query.filter_by(email.data).first() 
    if user:
        raise ValidationError('Email ALREADY EXIST CHOSSE DEFRENT ONE ')        