from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
csrf=CSRFProtect()


def createapp():
    from flask_sqlalchemy import SQLAlchemy
    from flask_wtf.csrf import CSRFProtect
    app=Flask(__name__,instance_relative_config=True)
    app.config.from_pyfile('config.py',silent=True)
    from nefsti.models import db
    db.init_app(app)
    csrf.init_app(app)
    migrate=Migrate(app,db)
    return app


app=createapp()
#csrf=CSRFProtect(app)#means that csrf protection is automatically available for all our routes created with app.route as long as it is post request

from nefsti import models,userroutes,adminroutes

