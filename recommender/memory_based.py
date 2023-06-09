import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity, polynomial_kernel, sigmoid_kernel, rbf_kernel
import joblib


def drop_duplicated(df:pd.DataFrame) -> pd.DataFrame:
    '''
    this function takes a dataframe as an argument.
    it is used because some of trackids appear several times in the dataset.
    They only differ in the genre. In the raw data there is only a single genre related to a row.
    this function deletes duplicated rows based on the trackid and modifies the genre column
    to a list in which every genre appears as an entry in the list.
    '''
    genres = df.groupby('track_id').agg({'track_genre' : list})
    df = df.drop_duplicates(subset = 'track_id')
    df = df.drop(columns = 'track_genre')
    df = pd.merge(left = df, right = genres, on= 'track_id')
    #df = df.drop_duplicates(subset = ['artists', 'track_name'])
    return df

def get_recommendations(song_input: pd.DataFrame,
                        df: pd.DataFrame,
                        n_recommendations: int = 5,
                        metric: str ='cosine',
                        pol_degree: str = 3)-> pd.DataFrame:
    '''
    This function takes a 1-row dataframe as an input. This row should contain at least all the features that you can
    see below in the 'audio_feats' list. This kind of dataframe is provided by the output of the 'get_track_info'
    function in the 'utils_spotify' module.

    to implement:
        - check scoring metrics for 'polynomial' and 'sigmoid': higher score-> higher similarity or higher distance?
          those metrics seem not to work properly
        - features as inputs to return recommendations based on those inputs
        - (weights for different input features?)
        - before deploying it: dont return the input song itself as the first recommendation, BUT
          keep it like this till the very end to double check if the recommendation system is working:
          you always expect the song itself to be most similar
    '''
    cv = joblib.load('../recommender/pickle/genre_vectorizer.pickle')
    audio_feats = [
             'popularity',
             'duration_ms',
             'explicit',
             'danceability',
             'energy',
             'key',
             'loudness',
             'mode',
             'speechiness',
             'acousticness',
             'instrumentalness',
             'liveness',
             'valence',
             'tempo'
        ]

    genres = list(cv.get_feature_names_out())
    audio_feats.extend(genres)
    #transforming input -> count vectorizing the genre
    song_input = cv.transform(song_input)

    song_input = song_input.loc[:, audio_feats]
    df_audio = df.loc[:, audio_feats]
    #scaling
    scaler = MinMaxScaler()
    df_audio_scaled = pd.DataFrame(scaler.fit_transform(df_audio), columns = df_audio.columns)
    song_input_scaled = pd.DataFrame(scaler.transform(song_input), columns = df_audio.columns)
    df_audio_scaled = df_audio_scaled.set_index(df['track_id'])
    #choosing metric -> calculating similarities
    if metric == 'cosine':
        similarities = cosine_similarity(X = song_input_scaled, Y = df_audio_scaled).T[:,0]
    elif metric == 'polynomial': #check scoring method: do high numbers indicate similarity or low?
        similarities = polynomial_kernel(
            X = song_input_scaled, Y = df_audio_scaled, degree=pol_degree).T[:,0]
        #similarities = 1/similarities
    elif metric == 'sigmoid': #check scoring method: do high numbers indicate similarity or low?
        similarities = sigmoid_kernel(
            X = song_input_scaled, Y = df_audio_scaled).T[:,0]
    elif metric == 'rbf': #high numbers indicate high similarity
        similarities = rbf_kernel(
            X = song_input_scaled, Y = df_audio_scaled).T[:,0]

    df_sim = pd.DataFrame({'track_id' : df['track_id'],
                           'similarity' : similarities,
                           'track_name' : df['track_name'],
                           'artist' : df['artists']})
    df_sim = df_sim.drop_duplicates(subset = ['artist', 'track_name'], keep = 'first')
    return df_sim.sort_values('similarity', ascending = False)[0:n_recommendations+1]
