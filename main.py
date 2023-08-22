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
    edited_df = st.data_editor(df,
                              column_config = {
                              "Week 1": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                              "Week 2": st.column_config.SelectboxColumn("Week 2", options = nfl_teams),
                              "Week 3": st.column_config.SelectboxColumn("Week 3", options = nfl_teams),
                              "Week 4": st.column_config.SelectboxColumn("Week 4", options = nfl_teams),
                              "Week 5": st.column_config.SelectboxColumn("Week 5", options = nfl_teams),
                              "Week 6": st.column_config.SelectboxColumn("Week 6", options = nfl_teams),
                              "Week 7": st.column_config.SelectboxColumn("Week 7", options = nfl_teams),
                              "Week 8": st.column_config.SelectboxColumn("Week 8", options = nfl_teams),
                              "Week 9": st.column_config.SelectboxColumn("Week 9", options = nfl_teams),
                              "Week 10": st.column_config.SelectboxColumn("Week 10", options = nfl_teams),
                              "Week 11": st.column_config.SelectboxColumn("Week 11", options = nfl_teams),
                              "Week 12": st.column_config.SelectboxColumn("Week 12", options = nfl_teams),
                              "Week 13": st.column_config.SelectboxColumn("Week 13", options = nfl_teams),
                              "Week 14": st.column_config.SelectboxColumn("Week 14", options = nfl_teams),
                              "Week 15": st.column_config.SelectboxColumn("Week 15", options = nfl_teams),
                              "Week 16": st.column_config.SelectboxColumn("Week 16", options = nfl_teams),
                              "Week 17": st.column_config.SelectboxColumn("Week 17", options = nfl_teams)
                              })
    submit = st.form_submit_button(label = 'Submit Pick')
    if submit:
        st.session_state.df = edited_df
