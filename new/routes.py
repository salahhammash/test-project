from flask import render_template, url_for, flash, redirect
from new.forms import RegistrationForm,LoginForm
from new.models import User
from new import app,bcrypt,db 
from flask_login import login_user,current_user,logout_user

about_us = [
    {
        "name": "Salah",
        "icon": "https://tse2.mm.bing.net/th?id=OIP.8ot8Y45H1REeX7fKQCwRVQHaE9&pid=Api&P=0&h=180",
        "description": "civile engeneer",
    },

    {
        "name": "M.Smadi",
        "icon": "https://cdn.wallpapersafari.com/24/23/J1pmeS.jpg",
        "description": "sowftwear devloper",
    },
    {
        "name": "ahmad",
        "icon": "https://tse4.mm.bing.net/th?id=OIP.PWkvllDVCfQTzc5w7cRoyQHaEo&pid=Api&P=0&h=180",
        "description": "sowftwear devloper",
    },
    {
        "name": "M.Sharef",
        "icon": "https://tse3.mm.bing.net/th?id=OIP.b7MI8EuWUJWOBvpvckB2vQHaE6&pid=Api&P=0&h=180",
        "description": "sowftwear devloper",
    },
    {
        "name": "Ala'a",
        "icon": "https://tse3.mm.bing.net/th?id=OIP.CBFZpMOFqyCjyHOJxouwVAHaE8&pid=Api&P=0&h=180",
        "description": "sowftwear devloper",
    },
]


@app.route("/")
# responsable to do all the back end for url that after/
@app.route("/home")
def home():
    return render_template("home.html",  title="Home")


@app.route("/about")
def about():
    return render_template("about.html", about_us=about_us , title="About")


@app.route("/register", methods=["GET", "POST"])
#this methods accsept GEt request & POST request
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    # this is mean that if the user is logged in go to home page directly
    
    form = RegistrationForm()
    # we created an instence from RegistrationForm()
    if form.validate_on_submit():
    # its mean chek if all the information that inside the form is correct --> print (flash function (first one is msg with the data that the user is enterd --> form.username.data [here we tooked the user name that the user interd in username filde when he did a regstration ], & the color of msg ))
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(fname=form.fname.data , lname=form.lname.data,username=form.username.data,email=form.email.data,password=hashed_password,)
        db.session.add(user)
        db.session.commit()
        
        flash(f"Account created successfully for {form.username.data}", "success")
        # we should import flash 
        
        # then after the registraition sucsesfuly send the user to the login page then after login sucsesfuly go to the home page 
        return redirect(url_for("login"))
    return render_template("register.html", title="Register", form=form)
#لما المستخدم يعبي الفورم ويعمل ساين اب بكون عمل بوست ريكويست وسلم الفورم ل هذا الريكويست ثم بيعمله فاليديشن اذا كلشي تمام بالفورم بطبعلو مسج وبوديه دايركت على صفحة الهوم اذا لا بضل بنفس الصفحة


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    # this is mean that if the user is logged in go to home page directly
    form = LoginForm()
    if form.validate_on_submit():
        # i will put an dumy data cuze we dont have a data base
        # if (
        #     form.email.data == "salah@gmail.com"
        #     # if the email that the user intered in the regestration is this 
        #     and form.password.data == "PASS!!word123"
        # ):
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # next_page = request.args.get('next')
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)


         
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))