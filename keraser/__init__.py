#!venv/bin/python
import logging, sys, os, datetime

from flask import Flask, g
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from config import Config

#create app
#init handlers and flask app
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
moment = Moment(app)

from keraser import views

