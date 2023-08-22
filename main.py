import pandas as pd
import streamlit as st
st.header("2023 NFL Survivor Pool")
st.subheader("Please use this page to input your survivor pick week by week")
nfl_teams = ['Arizona Cardinals','Atlanta Falcons','Baltimore Ravens','Buffalo Bills','Carolina Panthers','Chicago Bears','Cincinnati Bengals','Cleveland Browns','Dallas Cowboys','Denver Broncos','Detroit Lions','Green Bay Packers','Houston Texans','Indianapolis Colts','Jacksonville Jaguars','Kansas City Chiefs','Las Vegas Raiders','Los Angeles Chargers','Los Angeles Rams','Miami Dolphins','Minnesota Vikings','New England Patriots','New Orleans Saints','New York Giants','New York Jets','Philadelphia Eagles','Pittsburgh Steelers','San Francisco 49ers','Seattle Seahawks','Tampa Bay Buccaneers','Tennessee Titans','Washington Commanders']
@st.cache_data(ttl=1)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

with st.form("my_form"):
    df = load_data(st.secrets["public_gsheets_url"])
    if 'df' not in st.session_state:
        st.session_state.df = df
    edited_df = st.data_editor(df,
                              {'Week 1': 'TextColumn'
                               ,'Week 2': 'TextColumn'
                               ,'Week 3': 'TextColumn'
                               ,'Week 4': 'TextColumn'
                               ,'Week 5': 'TextColumn'
                               ,'Week 6': 'TextColumn'
                               ,'Week 7': 'TextColumn'
                               ,'Week 8': 'TextColumn'
                               ,'Week 9': 'TextColumn'
                               ,'Week 10': 'TextColumn'
                               ,'Week 11': 'TextColumn'
                               ,'Week 12': 'TextColumn'
                               ,'Week 13': 'TextColumn'
                               ,'Week 14': 'TextColumn'
                               ,'Week 15': 'TextColumn'
                               ,'Week 16': 'TextColumn'
                               ,'Week 17': 'TextColumn'})
    submit = st.form_submit_button(label = 'Submit Pick')
if submit:
    st.write(edited_df)
