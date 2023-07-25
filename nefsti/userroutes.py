import re,random,os,json
from functools import wraps
from flask import render_template, request, redirect, flash,make_response,session,url_for
from sqlalchemy.sql import text
from nefsti import app, csrf
from nefsti.models import db,User,State,Contact,Service
from nefsti.forms import SignupForm
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.exceptions import InternalServerError
import errno
def login_required(f):
    @wraps(f)
    def login_decorator(*args,**kwargs):
        if session.get("userid") and session.get('user_loggedin'):
            return f(*args,**kwargs)
        else:
            flash("access Denied,Please Login")
            return redirect("/login")
    return login_decorator 
@app.errorhandler(PermissionError)
def handle_permission_error(error):
    # Log the error or perform any necessary actions
    app.logger.error('PermissionError: %s', error)

    # Render a custom error page
    return render_template('500.html', error_message='Permission denied'), 500
@app.route("/")
def home():
     
   
     return render_template("user/index.html")
@app.route("/contact",methods=["POST","GET"])
def contact():
     state=db.session.query(State).all()
     services=db.session.query(Service).all()
     if request.method=="GET" :
         return render_template("user/contact.html",state=state,services=services)
   
     else:
       catf=request.form.get('first')
       catn=request.form.get('name')
       cata=request.form.get('address')
       cate=request.form.get('email')
       catc=request.form.get('city')
       catst=request.form.get('state')
       cats=request.form.get('services')
       catp=request.form.get('phone')
       u=Contact(firstname=catf,lastname=catn,address=cata,email=cate,city=catc,state=catst,services=cats,phone=catp)
       db.session.add(u)
       db.session.commit()
       flash("Thank you")
       return redirect("/contact")

@app.route("/about")
def about():
   
   
     return render_template("user/about.html")