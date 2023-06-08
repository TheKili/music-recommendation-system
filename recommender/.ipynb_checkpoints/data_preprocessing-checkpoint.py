import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import os
from sklearn.base import BaseEstimator, TransformerMixin

def preprocessing():
    data_path = os.path.join(os.path.dirname(os.getcwd()), 'raw_data/dataset.csv')
    df = pd.read_csv(data_path, index_col = 0)
    df = drop_duplicated(df)
    gv = Genre_vec()
    gv.fit(df, 'track_genre')
    df = gv.transform(df)
    gv.save_to_pickle()
    df.to_csv('../preprocessed_data/data_preprocessed.csv')

    
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

class Genre_vec(BaseEstimator, TransformerMixin):
    def __init__(self):
        # Initialize your transformer
        pass
    
    def fit(self, df, genre_col):
        '''
        If needed, this method will store information instance attributes.
        Returns "self".
        '''
        self.genre_col = genre_col
        slice = df.loc[:,genre_col]
        self.cv = CountVectorizer()
        slice.apply(lambda x: [i.replace('-', '_') for i in x])
        slice = slice.apply(lambda x: ' '.join(x))
        self.cv.fit(slice)
        self.col_names = self.cv.get_feature_names_out()
        
        return self     
    
    def transform(self, df):
        # Implement the transformation logic
        slice = df.loc[:,self.genre_col]
        slice.apply(lambda x: [i.replace('-', '_') for i in x])
        slice = slice.apply(lambda x: ' '.join(x))
        vectorized = self.cv.transform(slice).todense()
        df_vec = pd.DataFrame(vectorized, columns = self.col_names)
        df = df.drop(columns = [self.genre_col])
        df = pd.concat([df, df_vec], axis = 1)
        
        return df

    def get_feature_names_out(self):
        # Return the output feature names based on the input feature names
        return self.col_names

    def save_to_pickle(self):
        joblib.dump(self.cv, '../recommender/pickle/genre_vectorizer.pickle')  

if __name__ == '__main__':
    preprocessing()