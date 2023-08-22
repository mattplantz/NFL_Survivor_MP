import pandas as pd
import streamlit as st
st.header("2023 NFL Survivor Pool")
st.subheader("Please use this page to input your survivor pick week by week")
nfl_teams = ['Arizona Cardinals','Atlanta Falcons','Baltimore Ravens','Buffalo Bills','Carolina Panthers','Chicago Bears','Cincinnati Bengals','Cleveland Browns','Dallas Cowboys','Denver Broncos','Detroit Lions','Green Bay Packers','Houston Texans','Indianapolis Colts','Jacksonville Jaguars','Kansas City Chiefs','Las Vegas Raiders','Los Angeles Chargers','Los Angeles Rams','Miami Dolphins','Minnesota Vikings','New England Patriots','New Orleans Saints','New York Giants','New York Jets','Philadelphia Eagles','Pittsburgh Steelers','San Francisco 49ers','Seattle Seahawks','Tampa Bay Buccaneers','Tennessee Titans','Washington Commanders']
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

with st.form("my_form"):
    df = load_data(st.secrets["public_gsheets_url"])
    if 'df' not in st.session_state:
        st.session_state.df = df
    edited_df = st.data_editor(df)
    submit = st.form_submit_button(label = 'Submit Pick')
    if submit:
        st.write("Edited df:", edited_df)
