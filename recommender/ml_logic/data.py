import pandas as pd

from google.cloud import bigquery
from colorama import Fore, Style
from pathlib import Path

from taxifare.params import *

def clean_content_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw contnet data by
    - deleting duplicates
    - removing non-necessary features
    """


    return df


def create_k_recommendations (df: pd.DataFrame, distance: str, weights: list, k : int  ) -> pd.DataFrame:
    """
    Calculates distance matrix for given dataframe
    (returns distnance matrix or )
    (returns a dataframe with k recommendations for each song)
    (or saves them on a big query cloud)
    """


    return df
