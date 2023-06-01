from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from new import routes



app = Flask(__name__)
# this will give us the name of python file that we work from it 
bcrypt = Bcrypt()

login_manager = LoginManager(app)

app.config[
    "SECRET_KEY"
] = '149f4d353e32ee77aca7b0fd0fc12d1afa9d2a19106b61da284452fa6a17ceed'
#secret key : will protect our website from csrf(cross side request furgery ) will not allowed any one to do any changes in the coockis that related to the setion 
#by open terminal and write python then hit enter -->import secrets -->secrets0token_hex(32) [32 is the number of characters]


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pythonic.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)

