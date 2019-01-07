#!venv/bin/python

import logging, sys

from keraser import model, app
from config import Config

#init logger
logging.basicConfig(format=Config.LOGGING_FORMAT)
logger = logging.getLogger(Config.APP_NAME)
logger.setLevel(Config.LOGGING_LEVEL)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(Config.LOGGING_LEVEL)
formatter = logging.Formatter(Config.LOGGING_FORMAT)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('logging initialized')

# if this is the main thread of execution 
# initialize app and logging infrastructure. Then
# first load the model and
# then start the server
if __name__ == '__main__':
	logger.debug('About to run')
    #Initialization code
	logger.info('Loading Keras model and starting Flask server...')
	logger.info('Please wait until server has fully started')
	model.load_model()
    #run App
	logger.debug( "Running with options: {}".format(Config.APP_RUN_OPTS) )
	app.run(**Config.APP_RUN_OPTS)
	#Tensorflow has trouble unless options are:
	#app.run(debug = False, threaded = False, host='0.0.0.0', port=5000)

