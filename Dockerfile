FROM jfloff/alpine-python:3.7-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "glitnir:app"]
