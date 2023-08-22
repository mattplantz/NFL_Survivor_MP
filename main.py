import pandas as pd
import streamlit as st

nfl_teams = ['Arizona Cardinals','Atlanta Falcons','Baltimore Ravens','Buffalo Bills','Carolina Panthers','Chicago Bears','Cincinnati Bengals','Cleveland Browns','Dallas Cowboys','Denver Broncos','Detroit Lions','Green Bay Packers','Houston Texans','Indianapolis Colts','Jacksonville Jaguars','Kansas City Chiefs','Las Vegas Raiders','Los Angeles Chargers','Los Angeles Rams','Miami Dolphins','Minnesota Vikings','New England Patriots','New Orleans Saints','New York Giants','New York Jets','Philadelphia Eagles','Pittsburgh Steelers','San Francisco 49ers','Seattle Seahawks','Tampa Bay Buccaneers','Tennessee Titans','Washington Commanders']
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])
edited_df = st.data_editor(df,
                          column_config = {
                          "Week 1": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 2": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 3": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 4": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 5": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 6": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 7": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 8": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 9": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 10": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 11": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 12": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 13": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 14": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 15": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 16": st.column_config.SelectboxColumn("Week 1", options = nfl_teams),
                          "Week 17": st.column_config.SelectboxColumn("Week 1", options = nfl_teams)
                          })
