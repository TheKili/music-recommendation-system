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
# url = "something.endpoint" ### Needs real API Url

if sim_measure != "Polynomial":
    params = dict(
        title = input_title,
        artist = input_artist,
        metric = sim_measure,
        popularity = popularity,
        danceability = danceability,
        speechiness = speechiness,
        instrumentalness = instrumentalness,
        tempo = tempo
    )
else:
    params = dict(
        title = input_title,
        artist = input_artist,
        metric = sim_measure,
        poly_degree = poly_degree,
        popularity = popularity,
        danceability = danceability,
        speechiness = speechiness,
        instrumentalness = instrumentalness,
        tempo = tempo
    )

#response = requests.get(url, params=params)
#recommendations = response.json



"### For Testing"
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)

df = px.data.iris() # iris is a pandas DataFrame
fig = px.line(df, x="sepal_width", y="sepal_length")
fig.add_scatter()



st.plotly_chart(fig, use_container_width=True)
