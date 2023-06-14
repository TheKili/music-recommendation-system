import pandas as pd


# $WIPE_BEGIN
from recommender.memory_based import get_recommendations
from recommender.utils_spotify import get_track_info, get_previews
# $WIPE_END

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Get data
# $CHA_BEGIN
content_df = pd.read_csv('preprocessed_data/data_preprocessed.csv')
content_df = content_df.drop_duplicates(subset='track_id')
app.state.content_df = content_df
# $CHA_END

@app.get("/")
def root():
    # $CHA_BEGIN
    return dict(greeting="Welcome to our music-recommendation-system!")
    # $CHA_END

@app.get("/spotify_data")
def get_spotify_data(
        track_input: str = 'Greatest Dancer', # Yesterday
        artist_input: str = 'Sister Sledge', # The Beatles
        ):
    """
    Get a dict with spotify data for one track.
    """
    # $CHA_BEGIN

    # Get Track_dict
    track_dict = get_track_info(track_input, artist_input).to_dict()

    return track_dict
    # $CHA_END


@app.get("/predict")
def predict(
        track_input: str = 'Yesterday', # Yesterday
        artist_input: str = 'The Beatles', # The Beatles
        n_recommendations: int = 5,  # 10
        metric: str ='cosine',    # cosine, sigmoid, polynomial...
        colab_content_ratio: float = 1,     # 0-1
        pol_degree : str = 2
        # weights (popularity, danceability, speechiness, instrumentalness, tempo)
    ):      # 1
    """
    Get a dict with n recommendations based on several inputs.
    """
    # $CHA_BEGIN

    # Get Track_df
    track_df = get_track_info(track_input, artist_input)

    #Get Content_df
    content_df = app.state.content_df

    #Get recommendations
    ### TODO: Add weights to recommendations_dict

    recommendations_df = get_recommendations(track_df,
                        content_df,
                        n_recommendations,
                        metric,
                        pol_degree)

    prevurl_list = get_previews(recommendations_df['track_id'])

    recommendations_dict = recommendations_df.to_dict()

    recommendations_dict['prevurl'] = prevurl_list

    ### TODO: Add colab content (playlist data) and get final recommendations based on colab_content_ratio
    #get colab matrix

    #get recommendations from colab matrix
        #get song row in colab matrix
        #sort descending
        #return

    #implement weighting between content & colab recommendations


    return recommendations_dict
    # return recommendations_dict, prevurl_list
    # $CHA_END


### TESTS ###
import os

# Test the environment variables
@app.get("/env")
def env():
    # $CHA_BEGIN
    return dict(SPOTIFY_CLIENT_ID = f'{os.environ.get("SPOTIFY_CLIENT_ID")}',
                SPOTIFY_CLIENT_SECRET = f'{os.environ.get("SPOTIFY_CLIENT_SECRET")}'
                )
    # $CHA_END
