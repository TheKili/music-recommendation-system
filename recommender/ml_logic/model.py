import numpy as np
import pandas as pd
import time

from colorama import Fore, Style
from typing import Tuple


def create_k_recommendations (df: pd.DataFrame, distance: str, weights: list, k : int  ) -> pd.DataFrame:
    """
    Calculates distance matrix for given dataframe
    (returns distnance matrix or )
    (returns a dataframe with k recommendations for each song)
    (or saves them on a big query cloud)
    """


    return df

def create_colab_recommendations(track_matrix: np.ndarray, playlist_df, target_track_id):
    """
    Returns a list of recommended tracks for a given track_id
    Based on track_matrix
    (aka tracks that are in the same playlists as the given track_id)
    """
    idx = np.where(playlist_df['track_id'] == target_track_id)[0][0]
    sorted_indices = np.argsort(-track_matrix[idx])
    merged_array = np.column_stack((sorted_indices, track_matrix[idx][sorted_indices]))
    return merged_array
