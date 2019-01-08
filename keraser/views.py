#!venv/bin/python

'''
Main flask routes/actions
'''

from config import Config
import logging
logger = logging.getLogger(Config.APP_NAME)

import os, io, json
from datetime import datetime
from socket import gethostname
from PIL import Image
from flask import \
request,redirect,render_template, url_for, flash, jsonify, g

from keraser import app
from keraser.forms import UploadForm 
import keraser.img as img
import keraser.model as model #import the global variable inside the module, not the module

FILENAME = "uploads/uploaded_file"

#####################
#  Web UI           #
#####################

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	'''
	Homepage 
	'''
	form = UploadForm()

	#POST
	if form.validate_on_submit():
		#filename = secure_filename(form.file.data.filename)
		form.file.data.save(FILENAME) #'uploads/' + filename)
		return redirect(url_for('predict'), code=307) #307=preserve method POST
	#GET
	return render_template('index.html',
							current_time=datetime.utcnow(),
							form=form
							)

#####################
#  Predict          #
#####################

#this method can be hit directly or from the "upload image" form
@app.route("/predict", methods=["POST"])
def predict():
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if request.method == "POST":
		logger.debug('POST received in /predict')
		
		if os.path.isfile(FILENAME):
			#this is coming from the UI which saved a file
			logger.debug('IMAGE posted through UI and found in '+FILENAME)
			image = Image.open(FILENAME)

		if request.files.get("image"):
			#there is an image in the request, it's an API request
			logger.debug('IMAGE posted to /predict')
			# read the image in PIL format
			image = request.files["image"].read()
			image = Image.open(io.BytesIO(image))

		if image:
			# preprocess the image and prepare it for classification
			image = img.prepare_image(image, target=(224, 224))
			# classify the input image and then initialize the list
			# of predictions to return to the client
			logger.debug('calling model')
			preds = model.model.predict(image) #the model object in the "model" module
			results = img.decode_predictions(preds)
			data["predictions"] = []

			# loop over the results and add them to the list of
			# returned predictions
			for (imagenetID, label, prob) in results[0]:
				r = {"label": label, "probability": float(prob)}
				data["predictions"].append(r)
			# indicate that the request was a success
			data["success"] = True

			# show the responses as message
			flash('SUCCESS. Received responses:\n','message')
			for prediction in data["predictions"]:
				flash( prediction['label']+": "+str(prediction['probability'])+'\n', 'message')
			#if there was an image uploaded, delete it
			if os.path.isfile(FILENAME):
				os.remove(FILENAME)

		else:
			flash('No File received','error')
			logger.error('No file received')

		# return the data dictionary as a JSON response
		return jsonify(data)
