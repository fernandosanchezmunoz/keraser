#!venv/bin/python

'''
Keras model definition and initialization.
'''

from config import Config
import logging
logger = logging.getLogger(Config.APP_NAME)

# import the necessary packages
from keras.applications import ResNet50

#initialize Model
#model = None

def load_model():
	# load the pre-trained Keras model (here we are using a model
	# pre-trained on ImageNet and provided by Keras, but you can
	# substitute in your own networks just as easily)
	logger.debug("Loading ML model")
	global model
	model = ResNet50(weights="imagenet")
