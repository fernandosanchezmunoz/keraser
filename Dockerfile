FROM tensorflow/tensorflow:1.12.0

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "keraser:app"]
