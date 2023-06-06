import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

class Memory:
        def __init__(self):
            pass
    
        def drop_duplicated(self, df):
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
            df = df.drop_duplicates(subset = ['artists', 'track_name'])
            return df
        
        def get_recommendations(self, song_input, df, n_recommendations = 5, metric='cosine'):
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
                df_audio = df.loc[:, audio_feats]
                song_input = song_input.loc[:, audio_feats]
                scaler = MinMaxScaler()
                df_audio_scaled = pd.DataFrame(scaler.fit_transform(df_audio), columns = df_audio.columns)
                song_input_scaled = pd.DataFrame(scaler.transform(song_input), columns = df_audio.columns)
                df_audio_scaled = df_audio_scaled.set_index(df['track_id'])
                similarities = cosine_similarity(X = song_input_scaled, Y = df_audio_scaled).T[:,0]
                df_sim = pd.DataFrame({'track_id' : df['track_id'],
                                       'similarity' : similarities,
                                       'track_name' : df['track_name'],
                                       'artist' : df['artists']})
                
                
                
                return df_sim.sort_values('similarity', ascending = False)[0:n_recommendations+1]