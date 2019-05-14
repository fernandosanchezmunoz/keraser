# Keraser

Serves a Keras model through REST and UI. 

This version serves a model trained on ImageNet and will return labels for a picture. The picture can be:
- Sent through a REST API call as "image"

`curl -F image=@keraser/static/dog.jpg localhost:5000/predict`

- Uploaded through the GUI, accessing the server's IP address with a web browser

## Usage 

`docker run -p 5000:5000 fernandosanchez/keraser`
