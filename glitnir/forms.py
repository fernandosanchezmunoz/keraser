#!venv/bin/python

'''
Forms for use in Flask templates / pages. Buttons and textboxes and stuff.
'''

from config import Config
import logging
logger = logging.getLogger(Config.APP_NAME)

from flask_wtf import FlaskForm
from flask_wtf.file import FileField
    
class UploadForm(FlaskForm):
    file = FileField()