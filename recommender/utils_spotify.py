import os
import base64
import json
import requests
import pandas as pd



def get_access_token() -> str:
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_headers = {
        'Authorization': 'Basic ' + base64.b64encode((os.environ.get("SPOTIFY_CLIENT_ID")
        + ':' + os.environ.get("SPOTIFY_CLIENT_SECRET")).encode()).decode()
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }

    response = requests.post(auth_url, headers=auth_headers, data=auth_data)
    if response.status_code == 200:
        token = response.json().get('access_token')
        print('access token retrieved')
        return token
    else:
        print('Error:', response.status_code)
        return None


def get_track_id(track:str = 'Yesterday', artist:str = 'The Beatles') -> str:
    token = get_access_token()

    search_url = 'https://api.spotify.com/v1/search'
    headers = {
        'Authorization': 'Bearer ' + token
    }
    search = f'{artist} {track}'
    params = {
        'q': search,  # Replace with the name of the track you want to search
        'type': 'track',
        'limit': 1  # Number of results to retrieve
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        results = response.json()
        track_id = results['tracks']['items'][0]['id']
        print('Track ID:', track_id)
        return results, track_id
    else:
        print('Error:', response.status_code)
        return None


def get_track_info(track:str = 'Yesterday', artist:str = 'The Beatles') -> pd.DataFrame:
    '''
    this function takes the trackname and the artistname as input
    it will return a dataframe with a single row which contains all the features that
    the songs of the original df have so that you can use the output of the function to get recommendations
    '''
    token = get_access_token()
    results, track_id = get_track_id(track, artist)

    url = f'https://api.spotify.com/v1/audio-features/{track_id}'

    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        audio_features = response.json()

        song_info = results['tracks']['items'][0]

        artist_id = song_info['artists'][0]['id']
        artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'
        artist_response = requests.get(artist_url, headers=headers)

        if artist_response.status_code == 200:
            artist_info = artist_response.json()
            genres = artist_info['genres']
        else:
            genres = []

        df = pd.DataFrame({
            'track_id': [track_id],
            'artists': [song_info['artists'][0]['name']],
            'album_name': [song_info['album']['name']],
            'track_name': [song_info['name']],
            'popularity': [song_info['popularity']],
            'duration_ms': [song_info['duration_ms']],
            'explicit': [song_info['explicit']],
            'danceability': [audio_features['danceability']],
            'energy': [audio_features['energy']],
            'key': [audio_features['key']],
            'loudness': [audio_features['loudness']],
            'mode': [audio_features['mode']],
            'speechiness': [audio_features['speechiness']],
            'acousticness': [audio_features['acousticness']],
            'instrumentalness': [audio_features['instrumentalness']],
            'liveness': [audio_features['liveness']],
            'valence': [audio_features['valence']],
            'tempo': [audio_features['tempo']],
            'time_signature': [audio_features['time_signature']],
            'track_genre': [genres]
        })

        print(df)

        return df
    else:
        print('Error:', response.status_code)
        return None
