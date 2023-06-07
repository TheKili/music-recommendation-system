import streamlit as st
import numpy as np
import plotly.express as px

'''
# Music Recommendation Frontend
'''


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)

df = px.data.iris() # iris is a pandas DataFrame
fig = px.line(df, x="sepal_width", y="sepal_length")
fig.add_scatter()



st.plotly_chart(fig, use_container_width=True)
