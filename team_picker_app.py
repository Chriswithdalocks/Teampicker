import streamlit as st
import pandas as pd
import random

# Excel-Datei einlesen
df = pd.read_excel("spieler.xlsx")

# Nur Punkte für Stärke verwenden
df['Strength'] = df['Points']

# UI
st.title("Team Picker für Einsteiger")
selected_players = st.multiselect("Wähle 10 Spieler:", df['Name'].tolist())

# Zustand merken
if 'shuffle' not in st.session_state:
    st.session_state.shuffle = False

if len(selected_players) == 10:
    if st.button("Neu zusammenstellen"):
        st.session_state.shuffle = not st.session_state.shuffle

    # Spieler zufällig mischen
    selected_df = df[df['Name'].isin(selected_players)].copy()
    selected_df = selected_df.sample(frac=1, random_state=random.randint(0, 10000))

    # Abwechselnd in zwei Teams aufteilen
    team1 = selected_df.iloc[::2]
    team2 = selected_df.iloc[1::2]

    strength1 = team1['Strength'].sum()
    strength2 = team2['Strength'].sum()

    st.subheader(f"Team 1 (Stärke: {strength1})")
    st.write(team1[['Name', 'Rank', 'Points']])
    
    st.subheader(f"Team 2 (Stärke: {strength2})")
    st.write(team2[['Name', 'Rank', 'Points']])
else:
    st.info("Bitte genau 10 Spieler auswählen.")




