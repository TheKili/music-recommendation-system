FROM python:3.10.6-buster
WORKDIR /prod
RUN apt-get update && apt-get install -y direnv
COPY requirements_prod.txt requirements.txt
RUN pip install -r requirements.txt
COPY recommender /prod/recommender
COPY recommender/utils_spotify.py /prod/recommender/utils_spotify.py

COPY .env /prod/.env
COPY .envrc /prod/.envrc
COPY .cache-k3m4 /prod/.cache-k3m4
COPY raw_data/content.csv /prod/raw_data/content.csv
COPY Makefile /prod/Makefile
RUN direnv allow
RUN direnv reload
#RUN make api
