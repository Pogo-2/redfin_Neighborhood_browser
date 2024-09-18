import streamlit as st
from src.tim_sheet_logic.TimSheet import TimSheet
from src.tim_sheet_logic.tim_utils import get_neighborhood_ppsf

def draw_map():
    df = st.session_state["hood_data"]
    st.map(st.session_state["hood_data"])

def draw_headers():
    df = st.session_state["hood_data"]
    st.session_state["ppsf"] = get_neighborhood_ppsf(df)
    st.header(f"Found {len(df)} results with a estimated PPSF of {st.session_state['ppsf']}")
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
    col1.header("Address")
    col2.header("Property Type")
    col3.header("Price")
    col4.header("SQFT")
    col5.header("All in Investment")
    col6.header("profit %")

def get_tim_sheet(row):
    ts = TimSheet()
    ts.comp_square_feet = st.session_state["ppsf"]
    ts.purchase_price = row["PRICE"]
    ts.square_feet = row["SQUARE FEET"]
    ts.get_calculations()
    return ts

def draw_rows():
    df = st.session_state["hood_data"]
    for i, row in df.iterrows():
        ts = get_tim_sheet(row)
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
        col1.write(row["ADDRESS"])
        col2.write(row["PROPERTY TYPE"])
        col3.write(row["PRICE"])
        col4.write(row["SQUARE FEET"])
        col5.write(ts.all_in_investment)
        col6.write(ts.profit_percent)
        with col7:
            st.button("View", key=i)


def display_hood():
    draw_map()
    draw_headers()
    draw_rows()