#import os
#from flask_script import Manager
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_basicauth import BasicAuth
#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config.from_object('config')
#manager = Manager(app)
bootstrap = Bootstrap(app)

#app.config['BASIC_AUTH_USERNAME'] = 'admin'
#app.config['BASIC_AUTH_PASSWORD'] = 'admin'
basic_auth = BasicAuth(app)

#app.config['SQLALCHEMY_DATABASE_URI'] =\
#'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

#basedir = os.path.abspath(os.path.dirname(__file__))

   

import views

#if __name__ == '__main__':
#    manager.run()

