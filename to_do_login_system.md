# flask-login

pip install flask-login

in the __init__.py :

from flask_login import LoginManager


login_manager = LoginManager(app)

##  then go to the models.py  :

from new import db,login,login_manager
& 

to activate the login extension :
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

''' this def do relod for the user using user id that is store in the session , when the user do a login will open for him session and will storing in this sussion the user id , so this def will take this user id and return the user from the DB '''
* to do this we need 4 method :
[
- is authontecated : proberty the value of it is true if the user enterd a correct info ,else False 
- is active :proberty the value of it is true if the user account is active ,else False 
-is anonymuc : always will be false 
- Get id : unic id for the user 
]
all this method is stored in login extention that we installed , ther is a class called usermixen

* so : in models.py : 
 from flask_login import UserMixin
 and in the class User(db.Model,UserMixin)

# --------------------------
* now go to routs.py in  login

* from flask_login import login_user



delet the Dumy data 

after 
if form.validate_on_submit():
delete:
'''
   if (
            form.email.data == "salah@gmail.com"
            # if the email that the user intered in the regestration is this 
            and form.password.data == "PASS!!word123"
        ):
''' 

* and will take the user that enterd his info from DB:
     if form.validate_on_submit()
 *       user = User.query.filter_by(email=form.email.data).first()

  we used the email --> cuz we logging in using email not the username
        

        '''
        now we will cheak if we have this user & cheak the pass -> (form.password.data) that the user wrote in the login filed is the same that he did in the regestraiton -> user.password: (is the password that stored in the DB and we did the hash on it ),, form.password.data :(is  the password that the user is enterd in login page)
         اعمل تسجيل دخول اذا  كان اليوزر موجود و كان الباسوورد المدخل في الداتا بيز هو نفسه المدخل عند تسجيل الدخول 

        '''
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)


