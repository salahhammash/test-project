# to do a data base we will use SQLalchemy  as OOP 
## for protoction sql database

first pip install flask-sqlalchemy

then in the p.py 
from flask_sqlalchemy import SQLAlchemy

لازم نحدد المكان اللي بدنا نعمل فيه الداتا بيز

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

sqlite : نوع الداتا بيز المستخدمة 
/// : معناها انو بستخدم relativ path (PROJECT-TEAM3)
pythonic.db : اسم الداتا بيز
db = SQLAlchemy(app) : we will do an instence from (SQLAlchemy )

### بما انو الداتا بيز عبارة عن جداول مثلا بكون عندي جدول خاص للدروس او لليوزرز والباسوورد
### the calass in the DATABASE is called Model

# how to do DB in (CMD)/Terminal
 in the terminal 
 * python 
 * from p (the name of python file that we created DB inside it) // or you can use p.py  -> import db
* db.create_all()
* from p import User
 ## to add user to data base :
 user_1 = User(fname = 'salah', lname='new' , username='newsalah', email='absd@email.com' ,password='PASS!!word123')

* db.session.add(user_1)

 user_2 = User(fname = 'ahmad', lname='new' , username='ahmad new', email='ahmad2@email.com' ,password='PASS!!word123')

* db.session.add(user_2)


 * db.sessoion.commit()
this comand to do the session.add 

### to cheak what i have inside DATA BASE 
* user.query.all()
or 
* user.query.first
 --> this will return for me the first user in the db 

-- i can also do a check using filter :
* user.query.filter_by(email=ahmad2@email.com).all()
this will return for me a list that show me wich user have this email

* i can put a variable for any user :
user = user.query.filter_by(email=ahmad2@email.com).all()
this will return for me the whole info about this user 

* user.id 
will give me the id for this user 

## to be in python in the terminal & you want to clear the screen : 
* import os 
os.system('cls')

## to exit the python -> 
* exit()