FROM python:3.10.6-buster
WORKDIR /prod
RUN apt-get update && apt-get install -y nano
COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt
COPY recommender /prod/recommender
COPY preprocessed_data /prod/preprocessed_data
COPY setup.py /prod/setup.py
RUN pip install .
COPY Makefile /prod/Makefile
CMD uvicorn recommender.API.fast:app --host 0.0.0.0 --port $PORT
