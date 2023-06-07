import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os

scope = 'playlist-modify-public'
username = 'buggy0811'    
token = SpotifyOAuth(scope = os.environ['SPOTIFY_SCOPE'],
                    username = os.environ['SPOTIFY_USERNAME'],
                    client_id = os.environ['SPOTIFY_CLIENT_ID'],
                    client_secret = os.environ['SPOTIFY_CLIENT_SECRET'],
                    redirect_uri = 'http://127.0.0.1:8080/')
sp = spotipy.Spotify(auth_manager = token)

def get_track_info(track:str, artist:str) -> pd.DataFrame:
    '''
    this function takes the trackname and the artistname as input
    it will return a dataframe with a single row which contains all the features that
    the songs of the original df have so that you can use the output of the function to get recommendations
    '''
    search = f'{artist} {track}'
    song_info = sp.search(q = search)['tracks']['items'][0]
    track_id = song_info['id']
    artist_id = song_info['artists'][0]['id']
    album_id = song_info['album']['id']
    audio_feats = sp.audio_features(track_id)[0]

    df = pd.DataFrame({
                'track_id' : [track_id],
                'artists'  : [song_info['artists'][0]['name']],
                'album_name' : [song_info['album']['name']],
                'track_name' : [song_info['name']],
                'popularity' : [song_info['popularity']],
                'duration_ms' : [song_info['duration_ms']],
                'explicit' : [song_info['explicit']],
                'danceability' : [audio_feats['danceability']],
                'energy' : [audio_feats['energy']],
                'key' : [audio_feats['key']],
                'loudness' : [audio_feats['loudness']],
                'mode' : [audio_feats['mode']],
                'speechiness' : [audio_feats['speechiness']],
                'acousticness' : [audio_feats['acousticness']],
                'instrumentalness' : [audio_feats['instrumentalness']],
                'liveness' : [audio_feats['liveness']],
                'valence' : [audio_feats['valence']],
                'tempo' : [audio_feats['tempo']],
                'time_signature' : [audio_feats['time_signature']],
                'track_genre' : [sp.artist(artist_id)['genres']] 
})

    
    return df
    