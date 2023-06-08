import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import os

def preprocessing():
    data_path = os.path.join(os.path.dirname(os.getcwd()), 'raw_data/dataset.csv')
    df = pd.read_csv(data_path, index_col = 0)
    df = drop_duplicated(df)
    ret = genre_vectorizer(df, 'track_genre')
    df = ret[0]
    cv = ret[1]
    df.to_csv('../preprocessed_data/data_preprocessed.csv')
    joblib.dump(cv, 'pickle/count_vectorizer.pickle')

    
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

def genre_vectorizer(df, genre_col):
    '''
    this function is using sklearns count vectorizer but additionally
    appending the column names
    cols_to_vec: list of columns that will be vectorized
    run this function when setting up the project to 'onehotencode' the genres
    this function also returns a pickle file for the countvectorizer instance
    which will be used for transforming the genre of a new song
    '''
    cv = CountVectorizer()
    slice = df.loc[:,genre_col]
    slice.apply(lambda x: [i.replace('-', '_') for i in x])
    slice = slice.apply(lambda x: ' '.join(x))
    vectorized = cv.fit_transform(slice).todense()
    col_names = cv.get_feature_names_out()
    df_vec = pd.DataFrame(vectorized, columns = col_names)
    df = df.drop(columns = [genre_col])
    df = pd.concat([df, df_vec], axis = 1)
    return df, cv

if __name__ == '__main__':
    preprocessing()