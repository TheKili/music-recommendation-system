import streamlit as st
import  streamlit_vertical_slider  as svs
import numpy as np
import pandas as pd
import requests
import plotly.graph_objects as go
from st_btn_select import st_btn_select
from sklearn.preprocessing import MinMaxScaler

st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:11em !important;

}
.bg-image{
    background-image:url('radar.png')
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font bg-image"><i>Rhythm</i> </br> Radar</p> <p style="text-align:right;"> Your <i> customizable</i> Music Recommendation System</p>', unsafe_allow_html=True)
search,  customise = st.tabs(["1. Select your Song and Artist", "2. Customise"])

with search:
    col_song, col_artist = st.columns(2)
    with col_song:
        input_title = st.text_input("Please input your song title", max_chars=30)
    with col_artist:
        input_artist = st.text_input("Please input your song artist", max_chars=30)
    st.write("We will search for recommendations for:", f"*{input_artist}, {input_title}*")

    if input_artist and input_title:
        st.success("Sufficient Information to search for recommendations")
        "Please proceed after Optional Settings for recommendations"
    else:
        st.warning("Please specify at least Title and Artist")

    ""
    # Amount Recommendations asked
    "Next, adjust the **amount of recommendations** you want to get"
    recom_amount = st.slider("How many recommendations would you like?", 1, 100, value=5)
    ""


with customise:


    "### How do _you_ want your similarity to be measured"
    "There are several ways to measure 'similarity'. Here, you can choose between two. Have fun playing around!"
    sim_measure = st_btn_select(('Cosine', 'RBF'))
    st.write("Chosen similarity measure:", sim_measure)
    if sim_measure == "Polynomial":
        poly_degree = st.number_input("Please specifiy polynomial degree", min_value=2, max_value=10, value=2)
        st.info("Note default degree of 2")
    ""
    # Individual weights on (selected) features
    "### Become _your_ own DJ"
    "Let the _algorithm_ know what about the song is important to _you_."
    col1, col2, col3, col4, col5 = st.columns(5)
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
    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        acousticness = svs.vertical_slider(
                            key="acousticness",
                            default_value=1,
                            step=0.1,
                            min_value=0,
                            max_value=10
                            )
        "acousticness"


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
    with col10:
        valence = svs.vertical_slider(
                                key="valence",
                                default_value=1,
                                step=0.1,
                                min_value=0,
                                max_value=10
                                )
        "valence"


######## API CALL #######
    url = 'https://musicrecommender-t3ozapnnrq-ew.a.run.app/predict'
    params = {
                'track_input':  input_title,
                'artist_input': input_artist,
                'n_recommendations': recom_amount,
                'metric':sim_measure.lower(),
                'danceability' : danceability,
                'energy' : energy,
                'key' : key,
                'mode' : mode,
                'speechiness' : speechiness,
                'acousticness' : acousticness,
                'instrumentalness' : instrumentalness,
                'liveness' : liveness,
                'valence' : valence,
                'tempo' : tempo
        }

submit_button =  st.button('Get Recommendations')

if submit_button:
    with st.spinner('Wait for it...'):
        response = requests.get(url, params={"n_recommendattions" : 0})
        response = requests.get(url, params=params)
        st.write(response)
    if response.status_code == 200:


        prev_urls = response.json()['prevurl']
        prev_songs = [f'<audio id="{url}" controls="" src="{url}" class="stAudio" style="width: 70px;"></audio>' for url in prev_urls]
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

        rc_scaled = recommendations.copy()
        feature_scale = ["danceability","key" ,"mode","speechiness" ,"acousticness","instrumentalness","liveness","valence","tempo"]
        scaler = MinMaxScaler()
        rc_scaled[feature_scale] = pd.DataFrame(scaler.fit_transform(rc_scaled[feature_scale]), columns = feature_scale)
        features = ["Level of Similarity","danceability","speechiness" ,"acousticness","liveness","valence","tempo"]

        fig = go.Figure()
        for row in rc_scaled.iterrows():
            fig.add_trace(go.Scatterpolar(
                    r= row[1][features],
                    theta=features,
                    fill='none',
                    name= row[1]["Song Title"],
                    textposition="top center"
                ))

        fig.update_layout(
        width=1000,
        height=1000,
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
        st.write(recommendations.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.write("Bad Connection Gateway")
