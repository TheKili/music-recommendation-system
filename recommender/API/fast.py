import pandas as pd

# $WIPE_BEGIN
from recommender.memory_based import get_recommendations
from recommender.utils_spotify import get_track_info


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
content_df = pd.read_csv('raw_data/content.csv')
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
    recommendations_dict = get_recommendations(track_df,
                        content_df,
                        n_recommendations,
                        metric,
                        pol_degree).to_dict()

    ### TODO: Add weights to recommendations_dict
    ### TODO: Add colab content (playlist data) and get final recommendations based on colab_content_ratio

    # ⚠️ fastapi only accepts simple Python data types as a return value
    # among them dict, list, str, int, float, bool
    # in order to be able to convert the api response to JSON
    return recommendations_dict
    # $CHA_END
