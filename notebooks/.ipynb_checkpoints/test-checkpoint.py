%load_ext autoreload
%autoreload 2
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import sys
import os

# Get the parent directory path
parent_dir = os.path.dirname(os.path.abspath(''))
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from recommender.data_preprocessing import drop_duplicated, cust_cv
from recommender.memory_based import get_recommendations
from recommender.utils_spotify import get_track_info

artist = 'Sister Sledge'
track = 'greatest dancer'

song = get_track_info(track, artist)
print(song)