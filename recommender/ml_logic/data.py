import pandas as pd
import numpy as np
import json
import multiprocessing
import dask.array as da
import os

from google.cloud import bigquery
from colorama import Fore, Style
from pathlib import Path

#from recommender import params?


def get_content_data() -> pd.DataFrame:
    """
    Get raw content data from bigquery
    """


    return


def clean_content_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw contnet data by
    - deleting duplicates
    - removing non-necessary features
    """


    return df

def get_content_helper_data() -> pd.DataFrame:
    """
    Helper function to get content data from local for merging with colab data
    Get raw content data from local (future: bigquery?)
    Delete duplicates
    Return dataframe
    """
    #local data location
    local_content_path = os.path.join(os.getcwd(), 'raw_data/content.csv')

    #create dataframe
    content = pd.read_csv(local_content_path)

    #delete duplicates
    content_df = content.groupby('track_id', as_index=False).first()
    content_df = content_df.reset_index(drop=True)

    #get rid of unnecessary columns
    content_df = content_df[['track_id', 'track_name', 'artists']]

    return content_df

def get_colab_data(slice_amount = 3) -> pd.DataFrame:
    """
    Get raw colab data from local (bigquery?)
    slice_amount: amount of slices to be read (starting from 0)
    """
    # Specify the path to your JSON file
    local_playlist_path = os.path.join(os.getcwd(), 'raw_data/content.csv')
    print(local_playlist_path)
    json_file_paths = os.listdir(local_playlist_path)

    # Read the JSON file
    def load_json_file(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    #pool = multiprocessing.Pool()
    #json_data = pool.map(load_json_file, json_file_paths)
    #pool.close()
    #pool.join()

    # Create a list of all tracks
    tracklist = [f'{k*1000 + i} ||| {track["artist_name"]} ||| {track["track_name"]} ||| {track["track_uri"].replace("spotify:track:", "")}'
                for k, data in enumerate(json_data)
                for i, playlist in enumerate(data['playlists'])
                for track in playlist['tracks']]

    # Create a dataframe with the tracklist
    split_tracklist = [item.split(' ||| ') for item in tracklist]
    for item in split_tracklist:
        item[3] = item[3].replace('spotify:track:', '')
    tracklist_df = pd.DataFrame(split_tracklist, columns=['playlist_number', 'artist_name', 'track_name', 'track_id'])

    #Merge with content data (to remove tracks that are not in content data)
    content_df = get_content_helper_data()
    clean_df = pd.merge(tracklist_df, content_df.drop(columns=['track_name', 'artists']), on='track_id', how='inner')

    return clean_df


def clean_colab_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw colab data by
    - deleting duplicates
    - removing non-necessary features
    """

    return df

def get_track_matrix(df: pd.DataFrame, normalize=True, chunk_size_mb = 100) -> np.array:
    """
    Creates a track matrix from a dataframe
    (len(playlist_df) = Amount of unique Tracks)**2
    Index: (playlist_df['track_id'], playlist_df['track_id'])
    with track_matrix[i][j] = amount of playlists including track i and track j
    """

    #Group df by track_id and create a list of playlist numbers for each track
    playlist_df = df.groupby('track_id', as_index=False).agg({'playlist_number': list})
    playlist_df = playlist_df.reset_index(drop=True)

    #Get a list of all unique playlists
    unique_playlists = playlist_df['playlist_number'].explode().unique()
    unique_playlists.sort()

    # Create track_to_playlist_matrix with shape:
    # (len(playlist_df) = Amount of unique Tracks, len(unique_playlists) = Amount of unique Playlists)
    # Index: (playlist_df['track_id'], unique_playlists)
    track_to_playlist_matrix = np.zeros((playlist_df.shape[0], len(unique_playlists)))
    for i, playlists in enumerate(playlist_df['playlist_number']):
        track_to_playlist_matrix[i, np.searchsorted(unique_playlists, playlists)] = 1


    # Create track_matrix with shape:
    # (len(playlist_df) = Amount of unique Tracks)**2
    # Index: (playlist_df['track_id'], playlist_df['track_id'])
    # with track_matrix[i][j] = amount of playlists including track i and track j

    # Use Dask to minimize memory usage
    chunk_size_bytes = chunk_size_mb * 2**20  # 100 MB chunks

    #Convert track_to_playlist_matrix to dask array and transpose
    track_to_playlist_da = da.from_array(track_to_playlist_matrix, chunks=chunk_size_bytes)
    x_transposed = track_to_playlist_da.transpose()
    track_to_playlist_da_T = x_transposed.compute()

    #Compute
    result = da.dot(track_to_playlist_da, track_to_playlist_da_T)
    result = result.compute() # <-- This is where the magic happens

    return result



    if normalize == True:
        #normalize track_matrix
        for i in range(len(track_matrix)):
            if track_matrix[i, i] != 1:
                # Normalize values
                track_matrix[i, :] /= track_matrix[i, i]
                track_matrix[:, i] /= track_matrix[i, i]

    return track_matrix





def create_k_recommendations (df: pd.DataFrame, distance: str, weights: list, k : int  ) -> pd.DataFrame:
    """
    Calculates distance matrix for given dataframe
    (returns distnance matrix or )
    (returns a dataframe with k recommendations for each song)
    (or saves them on a big query cloud)
    """


    return df
