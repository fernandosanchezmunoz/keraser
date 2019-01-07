#!venv/bin/python

'''
Useful stuff for image processing.
'''

from config import Config
import logging
logger = logging.getLogger(Config.APP_NAME)

from keras.applications import imagenet_utils
from keras.preprocessing.image import img_to_array
import numpy as np

def prepare_image(image, target):
	# if the image mode is not RGB, convert it
	if image.mode != "RGB":
		image = image.convert("RGB")

	# resize the input image and preprocess it
	image = image.resize(target)
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)

	# return the processed image
	return image

def	decode_predictions(preds):
	return imagenet_utils.decode_predictions(preds)