FROM tensorflow/tensorflow:latest-gpu-py3

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python run.py
