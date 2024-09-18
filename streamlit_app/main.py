import streamlit as st
import pandas as pd
from src.redfin_core.TimRedfin import TimRedfin
from io import StringIO
from streamlit_app.streamlit_utils import transform_dataframe
from streamlit_app.display_hood import display_hood

def initialize_session_state():
    st.session_state.setdefault('init', True)
    st.session_state.setdefault('hood_search', None)
    st.session_state['redfin'] = TimRedfin()
    st.session_state.setdefault('hood_data', None)
    st.session_state.setdefault('ppsf', None)
    
def search_neighborhood():
    st.session_state["hood_search"] = st.text_input("Neighborhood")
    if st.button("Search"):
        tim_redfin = st.session_state["redfin"]
        tim_redfin.set_region_id(hood_name=st.session_state["hood_search"])
        response = tim_redfin.get_hood_data()
        df = pd.read_csv(StringIO(response))
        df = transform_dataframe(df)
        st.session_state["hood_data"] = df

def main():
    # Initialize session state
    st.set_page_config(page_title="Redfin Neighborhood Data", page_icon="🏠", layout="wide")
    st.title("Redfin Neighborhood Data")
    st.divider()

    if 'init' not in st.session_state:
        initialize_session_state()

    search_neighborhood()
    if st.session_state["hood_data"] is not None:
        display_hood()