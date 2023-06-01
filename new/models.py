from new import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    # db : is the name of the variable that we make an inctence from SQLAlchemy(app) 
    # Model : is class inside SQLAlchemy
    
    id = db.Column(db.Integer, primary_key=True)
    # db.Colomn is colomn in the DB ->type of it is integer , for each user ther is a special primary_key
    
    fname = db.Column(db.String(25), nullable=False)
    #nullable : its mean that this (خانة) cant be empty in the data base ,
    # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
    
    lname = db.Column(db.String(25), nullable=False)
    #nullable : its mean that this (خانة) cant be empty in the data base ,
    # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
    
    username = db.Column(db.String(25), unique=True, nullable=False)
    #nullable : its mean that this (خانة) cant be empty in the data base ,
    # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
    #unique : to tell the user that this user name is used (choose anouther one )
    
    email = db.Column(db.String(125), unique=True, nullable=False)
    #nullable : its mean that this (خانة) cant be empty in the data base ,
    # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
    #unique : to tell the user that this email  is used (choose anouther one )
    
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    #default : will store the name of img and wel
    # thew name of img is not allowed to be empty , but if the user didnt put a img --> put a defult emage
   
    password = db.Column(db.String(60), nullable=False)
    # password will be an hashed string from 60 charachters , when the user inter tha pass -> will not store the password as tuser input it to protect from attak ---->>> so cuz of that we will take the password from the user and store it inside DB usig hashing

def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"
    # __repr__ : this wil represinting the user    
    
# Wrap the code that uses the database functionality within the application context
# with app.app_context():
#     db.create_all()    