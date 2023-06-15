### Utility Functions to test API ###


import requests
#from utils_spotify import authenticate_spotify
from .utils_spotify import *
import sys


def get_welcome():
    url = 'http://127.0.0.1:8000/'
    response = requests.get(url)

    print(response.status_code)
    print(response.json())

    return response


def get_env():
    url = 'http://127.0.0.1:8000/env'
    response = requests.get(url)

    print(response.status_code)
    print(response.json())

    return response




def get_spotify_data():
    url = 'http://127.0.0.1:8000/spotify_data'
    artist = 'Sister Sledge'
    track = 'greatest dancer'

    params = {
    'track_input':  artist,
    'artist_input': track,
    }
    response = requests.get(url, params=params)

    print(response.status_code)
    print(response.json())

    return response


def get_recommendations():
    url = 'http://127.0.0.1:8000/predict'

    params = {
            'track_input':  'Yesterday',
            'artist_input': 'The Beatles',
            'n_recommendations': 5,
            'metric':'cosine',
            'colab_content_ratio': 1,
            'pol_degree' :  3
    }

    response = requests.get(url, params=params)

    print(response.status_code)
    print(response.json())

    return response



def get_welcome_gcp():
    url = 'https://musicrecommender-t3ozapnnrq-ew.a.run.app'
    # url = 'https://test-t3ozapnnrq-ew.a.run.app'

    response = requests.get(url)

    print(response.status_code)
    print(response.json())

    return response

def get_env_gcp():
    url = 'https://musicrecommender-t3ozapnnrq-ew.a.run.app/env'
    # url = 'https://test-t3ozapnnrq-ew.a.run.app'
    response = requests.get(url)

    print(response.status_code)
    print(response.json())

    return response


def get_spotify_data_gcp():
    url = 'https://musicrecommender-t3ozapnnrq-ew.a.run.app/spotify_data'
    # url = 'https://test-t3ozapnnrq-ew.a.run.app'
    artist = 'Sister Sledge'
    track = 'greatest dancer'

    params = {
    'track_input':  artist,
    'artist_input': track,
    }
    response = requests.get(url, params=params)

    print(response.status_code)
    print(response.json())

    return response


def get_recommendations_gcp():
    #url = 'https://musicrecommender-t3ozapnnrq-ew.a.run.app/predict'
    url = 'https://test-t3ozapnnrq-ew.a.run.app/predict'

    params = {
            'track_input':  "He's the greatest dancer",
            'artist_input': 'Sister Sledge',
            'n_recommendations': 5,
            'metric':'cosine',
            'danceability' : 100,
            'energy' : 100,
            'key' : 1,
            'mode' : 1,
            'speechiness' : 0,
            'acousticness' : 0,
            'instrumentalness' : 1,
            'liveness' : 1,
            'valence' : 1,
            'tempo' : 100
    }

    response = requests.get(url, params=params)

    print(response.status_code)
    print(response.json())

    return response
