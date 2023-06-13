import streamlit as st
import numpy as np
import pandas as pd
import requests
import plotly.express as px
from st_btn_select import st_btn_select

'''
# Music Recommendation Frontend
### Here you can find recommendations for your favorite songs!
'''
""
# User Song Input
"First, let us know the **song you want to get recommendations** for"
input_title = st.text_input("Please input your song title", max_chars=30)
input_artist = st.text_input("Please input your song artist", max_chars=30)
st.write("We will search for recommendations for:", f"*{input_artist}, {input_title}*")
""
# Amount Recommendations asked
"Next, adjust the **amount of recommendations** you want to get"
recom_amount = st.slider("Select recommendation quantity", 1, 100, value=5)
""
if input_artist and input_title:
    st.success("Sufficient Information to search for recommendations")
    "Please proceed after Optional Settings for recommendations"
else:
    st.warning("Please specify at least Title and Artist")


"#### Optional Settings"
# Similarity Measure to apply
"(*Optional*) Change the similarity measure to get different results"
sim_measure = st_btn_select(('Cosine', 'RBF', 'Polynomial', 'Sigmoid'))
st.write("Chosen similarity measure:", sim_measure)
if sim_measure == "Polynomial":
    poly_degree = st.number_input("Please specifiy polynomial degree", min_value=2, max_value=10, value=2)
    st.info("Note default degree of 2")
""
# Individual weights on (selected) features
"(*Optional*) Change weights on song features"
col1, col2, col3, col4, col5 = st.columns(5)
popularity = col1.number_input('Popularity', min_value=0.0, max_value=10.0, value=1.0)
danceability = col2.number_input('Danceability', min_value=0.0, max_value=10.0, value=1.0)
speechiness = col3.number_input('Speechiness', min_value=0.0, max_value=10.0, value=1.0)
instrumentalness = col4.number_input('Instrumentalness', min_value=0.0, max_value=10.0, value=1.0)
tempo = col5.number_input('Tempo', min_value=0.0, max_value=10.0, value=1.0)


######## API CALL #######
"### Your Recommendations"
url = 'https://musicrecommender-t3ozapnnrq-ew.a.run.app/predict'
if sim_measure != "Polynomial":
    params = {
            'track_input':  input_title,
            'artist_input': input_artist,
            'n_recommendations': recom_amount,
            'metric': sim_measure.lower(),
            'colab_content_ratio': 1,
    }
else:
    params = {
            'track_input':  input_title,
            'artist_input': input_artist,
            'n_recommendations': recom_amount,
            'metric': sim_measure.lower(),
            'colab_content_ratio': 1,
            'pol_degree' :  poly_degree
    }
if st.button('Get Recommendations'):
    response = requests.get(url, params=params)
    
    #st.write(response.json())
    prev_urls = response.json()['prevurl']
    track_id = response.json()['track_id']
    similarity = response.json()['similarity']
    track_name = response.json()['track_name']
    artist = response.json()['artist']
    
    recommendations =  pd.DataFrame({'track_id' : track_id,
                                     'similarity' : similarity,
                                     'track_name' : track_name,
                                     'artist' : artist})
    
    recommendations.drop(columns=["track_id"], axis=1, inplace=True)
    recommendations.reset_index(drop=True, inplace=True)
    recommendations.rename(columns={"similarity": "Level of Similarity",
                                    "track_name": "Song Title",
                                    "artist": "Song Artist"}, inplace=True)
    
    col1, col2 = st.columns([4, 1])
    with col1:
        st.dataframe(recommendations)
    with col2:
        for url in prev_urls:
            st.audio(url, format='audio/mp3')


"### For Testing"
""
audio_url = "https://p.scdn.co/mp3-preview/1bf99c2808f44cf89dd9f42e6e3a7804362e53ed?cid=3d24a9c30a8348af9da7088a04163f6b"
st.audio(audio_url, format='audio/mp3')



x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)

df = px.data.iris() # iris is a pandas DataFrame
fig = px.line(df, x="sepal_width", y="sepal_length")
fig.add_scatter()



st.plotly_chart(fig, use_container_width=True)
