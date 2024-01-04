#IMPORT LIBRARIES
#import streamlit
import streamlit as st
#specklepy libraries
from specklepy.api.client import SpeckleClient
from specklepy.api.credentials import get_account_from_token
#import pandas
import pandas as pd
#import plotly express
import plotly.express as px
print("his Majesty")
#--------------------------
#PAGE CONFIG
st.set_page_config(
    page_title="Speckle Stream Activity",
    page_icon="📊"
)
#--------------------------
#CONTAINERS
header = st.container()
input = st.container()
viewer = st.container()
report = st.container()
graphs = st.container()
#--------------------------
#HEADER
#Page Header
with header:
    st.title("Speckle Stream Activity App📈")
#About info
with header.expander("About this app🔽", expanded=True):
    st.markdown(
        """This is a beginner web app developed using Streamlit. My goal was to understand how to interact with Speckle API using SpecklePy, 
        analyze what is received and its structure. This was easy and fun experiment.
        """
    )
#--------------------------