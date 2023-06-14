import streamlit as st
import  streamlit_vertical_slider  as svs
import numpy as np
import pandas as pd
import requests
import plotly.graph_objects as go
from st_btn_select import st_btn_select
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(layout="wide")
'''
# Music Recommendation Frontend
### Here you can find recommendations for your favorite songs!
'''
""
# User Song Input
"<------ First, let us know the **song you want to get recommendations** for"

with st.sidebar:
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
    sim_measure = st_btn_select(('Cosine', 'RBF'))
    st.write("Chosen similarity measure:", sim_measure)
    if sim_measure == "Polynomial":
        poly_degree = st.number_input("Please specifiy polynomial degree", min_value=2, max_value=10, value=2)
        st.info("Note default degree of 2")
    ""
    # Individual weights on (selected) features
    "(*Optional*) Change weights on song features"
    col1, col2, col3 = st.columns(3)
    with col1:
        danceability = svs.vertical_slider(
                            key="danceability",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "danceability"
    with col2:
        energy = svs.vertical_slider(
                            key="energy",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "energy"
    with col3:
        key = svs.vertical_slider(
                            key="key",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "key"
    col4, col5, col6 = st.columns(3)

    with col4:
        mode = svs.vertical_slider(
                            key="mode",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "mode"
    with col5:
        speechiness = svs.vertical_slider(
                            key="speechiness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "speechniness"
    with col6:
        acousticness = svs.vertical_slider(
                            key="acousticness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "acousticness"

    col7, col8, col9 = st.columns(3)

    with col7:
        instrumentalness = svs.vertical_slider(
                            key="instrumentalness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "instrumentalness"
    with col8:
        liveness = svs.vertical_slider(
                            key="liveness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "liveness"
    with col9:
        tempo = svs.vertical_slider(
                            key="tempo",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "tempo"


        ######## API CALL #######
        "### Your Recommendations"
        url = 'https://test-t3ozapnnrq-ew.a.run.app/predict'
        params = {
                    'track_input':  input_title,
                    'artist_input': input_artist,
                    'n_recommendations': recom_amount,
                    'metric':sim_measure.lower(),
                    'danceability' : danceability,
                    'energy' : 1,
                    'key' : 1,
                    'mode' : 1,
                    'speechiness' : 1,
                    'acousticness' : 1,
                    'instrumentalness' : 1,
                    'liveness' : 1,
                    'valence' : 1,
                    'tempo' : 1
            }





if st.button('Get Recommendations'):
    st.write(params)
    response = requests.get(url, params=params)
    if response.status_code == 200:
    #st.write(response.json())

        prev_urls = response.json()['prevurl']
        prev_songs = [f'<audio id="{url}" controls="" src="{url}" class="stAudio" style="width: 50px;"></audio>' for url in prev_urls]
        track_id = response.json()['track_id']
        similarity = response.json()['similarity']
        track_name = response.json()['track_name']
        artist = response.json()['artist']
        danceability = response.json()['danceability']
        key = response.json()['key']
        mode = response.json()['mode']
        speechiness = response.json()['speechiness']
        acousticness = response.json()['acousticness']
        instrumentalness = response.json()['instrumentalness']
        liveness = response.json()['liveness']
        valence = response.json()['valence']
        tempo = response.json()['tempo']


        recommendations =  pd.DataFrame({'track_id' : track_id,
                                    'similarity' : similarity,
                                    'track_name' : track_name,
                                    'artist' : artist,
                                    'danceability' : danceability,
                                    'key' : key,
                                    'mode' : mode,
                                    'speechiness' : speechiness,
                                    'acousticness' : acousticness,
                                    'instrumentalness' : instrumentalness,
                                    'liveness' : liveness,
                                    'valence' : valence,
                                    'tempo' : tempo
                                    })

        recommendations.drop(columns=["track_id"], axis=1, inplace=True)
        recommendations.reset_index(drop=True, inplace=True)
        recommendations.rename(columns={"similarity": "Level of Similarity",
                                    "track_name": "Song Title",
                                    "artist": "Song Artist"}, inplace=True)
        recommendations["song_preview"] = prev_songs


        feature_scale = ["danceability","key" ,"mode","speechiness" ,"acousticness","instrumentalness","liveness","valence","tempo"]
        scaler = MinMaxScaler()
        recommendations[feature_scale] = pd.DataFrame(scaler.fit_transform(recommendations[feature_scale]), columns = feature_scale)
        features = ["Level of Similarity","danceability","speechiness" ,"acousticness","liveness","valence","tempo"]

        fig = go.Figure()
        for row in recommendations.iterrows():
            fig.add_trace(go.Scatterpolar(
                    r= row[1][features],
                    theta=features,
                    fill='none',
                    name= row[1]["Song Title"],
                    textposition="top center"
                ))

        fig.update_layout(
        width=1500,
        height=1500,
        polar=dict(
        radialaxis=dict(
        visible=True
        ),
        ),
        legend=dict(
        orientation="h",

        )
        )
        st.plotly_chart(fig, use_container_width=True)


        st.snow()
        st.write(recommendations.to_html(escape=False, index=False), unsafe_allow_html=True)
        values = recommendations.loc[0,["Level of Similarity"]]
    else:
        st.write("Bad Connection Gateway")
