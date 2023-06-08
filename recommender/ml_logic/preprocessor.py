import numpy as np
import pandas as pd
import math
from colorama import Fore, Style
import pygeohash as gh

from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer

from taxifare.ml_logic.encoders import transform_time_features, transform_lonlat_features, compute_geohash



def process_data_chunks (song_list: {}  json: dict) -> pd.DataFrame:
    """
    processes data chunks and add result to co-occurence matrix
    """


    return df
