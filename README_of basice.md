# Flask

open the folder that you want to do yor work inside it -> mkdir -> cd .... ,todo

do a vertual enviroment inside the file that you created & want to work inside it (.venv) -> :
python -m venv .venv
(
Get-ExecutionPolicy -List
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
Get-ExecutionPolicy -List
.venv\Scripts\activate
)
code .

install flask by -> pip install flask
in vs code open a new py file :

from flask import Flask

# some basics

### this will give us the name of python file that we work from it
app = Flask(__name__)

<br>

### responsable to do all the back end for url that after ("/")

@app.route("/home")
def home():
    return "<h6>hello home </h6>"
you can run the python file by (python and the name of file .py)

<br>

#### this to run the page without turn off the server & tern it on again to see my

if __name__ == "__main__":
    app.run(debug=True)
<br>

## Beter we should add render templeat and import it with Flask

@app.route("/home")
def home():
    return render_template("home.html",  title="Home")
    [the title i will explaine later ]

## & we should have a folder templates  -> inside it we need to do home.html / about.html ... (layout.html) & all the routes that i need

inside each file of htmlexept layout.html we need to do this without using (!) just write this command :

{% extends "layout.html"%}
{% block content%}

here we can add the code that we want to show .

{% endblock content%}

# layout .html 

## & dont forget to use {% block content%} {% endblock %} inside layout.html

some explains about title that we pased in the routs , in layout we should add this :
in the head after writing ( ! )

  {% if title %}

    <title>{{title}}</title>
    {% else %}
    <title>random</title>
    {%endif%}

& here we can add footer & nav bar inside the body in the layout.html --> cuz it wil be shown in all pagez

1-add nav bar

 2- {% block content%} {% endblock %}

3- foteer 

<br>

## be sure that this work inside layout template befor the ({% block content%} {% endblock %}), to use bootstrap we should put this link in the head  :
<h5> link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"> 
        </h5>

 <br>

### to use some icons put this in the head 
  <h5>
  link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
        </h5>

 <br>


# URL_for

## also if you have some css code that isnt inside boot strap 
 
 (link rel="stylesheet" type="text/css" 
 href="{{url_for('static', filename='main.css')}}">)

  cuz of that we use   ( url_for ) will go to the file that inside the folder that named (static -> we should creat it ) , and will take the name of file that we put the changes inside it (main.css)  ,&&& we should import url_for in the py file



### to do some stiling using JS BUNDEL without writing JS code , put it in the body 
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
        crossorigin="anonymous"></script>


# for loop

### how to do a loop using jinja2 

we should creat a variable inside the file .py [{}] -> array of dic  
about_us =[{add here wat you want info to show them }] -->
[{{
        "name": "Salah",
        "icon": "path of foto",
    },}]

then pass the variable to the rout that you want to show the info inside it
example :

@app.route("/about")
def about():
    return render_template("about.html", about_us = about_us , title="About")

then go to about.html and write this  as an example

{% for i in about_us %}


<h5 class="card-title">{{i.name}}</h5>
<img src="{{i.icon}}" class="card-img-top" alt="...">
to show the img wriet this code 
img src="{{i.icon}}" class="card-img-top" alt="..." 


{% endfor %}
