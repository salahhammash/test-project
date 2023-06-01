# from flask import Flask, render_template, url_for, flash, redirect
# from new.forms import RegistrationForm,LoginForm
# from flask_sqlalchemy import SQLAlchemy
# from new.models import User

from new import app

# app = Flask(__name__)

# # this will give us the name of python file that we work from it 

# app.config[
#     "SECRET_KEY"
# ] = '149f4d353e32ee77aca7b0fd0fc12d1afa9d2a19106b61da284452fa6a17ceed'

#secret key : will protect our website from csrf(cross side request furgery ) will not allowed any one to do any changes in the coockis that related to the setion 
#by open terminal and write python then hit enter -->import secrets -->secrets0token_hex(32) [32 is the number of characters]


# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonic.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# db = SQLAlchemy(app)


# about_us = [
#     {
#         "name": "Salah",
#         "icon": "https://tse2.mm.bing.net/th?id=OIP.8ot8Y45H1REeX7fKQCwRVQHaE9&pid=Api&P=0&h=180",
#         "description": "civile engeneer",
#     },

#     {
#         "name": "smadi",
#         "icon": "https://cdn.wallpapersafari.com/24/23/J1pmeS.jpg",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "ahmad",
#         "icon": "https://tse3.mm.bing.net/th?id=OIP.CBFZpMOFqyCjyHOJxouwVAHaE8&pid=Api&P=0&h=180",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "shahin",
#         "icon": "salah.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
#     {
#         "name": "Ala'a",
#         "icon": "idea.png",
#         "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!",
#     },
# ]


# @app.route("/")
# # responsable to do all the back end for url that after/
# @app.route("/home")
# def home():
#     return render_template("home.html",  title="Home")


# @app.route("/about")
# def about():
#     return render_template("about.html", about_us=about_us , title="About")


# @app.route("/register", methods=["GET", "POST"])
# #this methods accsept GEt request & POST request
# def register():
#     form = RegistrationForm()
#     # we created an instence from RegistrationForm()
#     if form.validate_on_submit():
#     # its mean chek if all the information that inside the form is correct --> print (flash function (first one is msg with the data that the user is enterd --> form.username.data [here we tooked the user name that the user interd in username filde when he did a regstration ], & the color of msg ))
        
#         flash(f"Account created successfully for {form.username.data}", "success")
#         # we should import flash 
        
#         # then after the registraition sucsesfuly send the user to the login page then after login sucsesfuly go to the home page 
#         return redirect(url_for("login"))
#     return render_template("register.html", title="Register", form=form)
# #لما المستخدم يعبي الفورم ويعمل ساين اب بكون عمل بوست ريكويست وسلم الفورم ل هذا الريكويست ثم بيعمله فاليديشن اذا كلشي تمام بالفورم بطبعلو مسج وبوديه دايركت على صفحة الهوم اذا لا بضل بنفس الصفحة


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         # i will put an dumy data cuze we dont have a data base
#         if (
#             form.email.data == "salah@email.com"
#             # if the email that the user intered in the regestration is this 
#             and form.password.data == "PASS!!word123"
#         ):
#             flash("You have been logged in!", "success")
#             return redirect(url_for("home"))
#         else:
#             flash("Login Unsuccessful. Please check credentials", "danger")
#     return render_template("login.html", title="Login", form=form)


# class User(db.Model):
#     # db : is the name of the variable that we make an inctence from SQLAlchemy(app) 
#     # Model : is class inside SQLAlchemy
    
#     id = db.Column(db.Integer, primary_key=True)
#     # db.Colomn is colomn in the DB ->type of it is integer , for each user ther is a special primary_key
    
#     fname = db.Column(db.String(25), nullable=False)
#     #nullable : its mean that this (خانة) cant be empty in the data base ,
#     # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
    
#     lname = db.Column(db.String(25), nullable=False)
#     #nullable : its mean that this (خانة) cant be empty in the data base ,
#     # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
    
#     username = db.Column(db.String(25), unique=True, nullable=False)
#     #nullable : its mean that this (خانة) cant be empty in the data base ,
#     # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
#     #unique : to tell the user that this user name is used (choose anouther one )
    
#     email = db.Column(db.String(125), unique=True, nullable=False)
#     #nullable : its mean that this (خانة) cant be empty in the data base ,
#     # String(25) = maximum 25 charachter cuz we told him that the max is 25 in forms.py
#     #unique : to tell the user that this email  is used (choose anouther one )
    
#     image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
#     #default : will store the name of img and wel
#     # thew name of img is not allowed to be empty , but if the user didnt put a img --> put a defult emage
   
#     password = db.Column(db.String(60), nullable=False)
#     # password will be an hashed string from 60 charachters , when the user inter tha pass -> will not store the password as tuser input it to protect from attak ---->>> so cuz of that we will take the password from the user and store it inside DB usig hashing
    
    
# def __repr__(self):
#         return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"
#     # __repr__ : this wil represinting the user


# # Wrap the code that uses the database functionality within the application context
# with app.app_context():
#     db.create_all()

   

if __name__ == "__main__":
    app.run(debug=True)
     # this to run the page without turn off the server & tern it on again to see my