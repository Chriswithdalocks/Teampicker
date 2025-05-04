import streamlit as st
import pandas as pd
import random

# Excel-Datei einlesen
df = pd.read_excel("spieler.xlsx")  # <- deine Excel-Datei hier

# Stärke berechnen (einfaches Beispiel)
rank_order = {
    'IRON': 1, 'BRONZE': 2, 'SILBER': 3, 'SILVER': 3,
    'GOLD': 4, 'PLATIN': 5, 'PLATINUM': 5, 'EMERALD': 6,
    'DIAMANT': 7, 'DIAMOND': 7, 'MASTER': 8, 'GRANDMASTER': 9, 'CHALLENGER': 10
}
df['Rank_Num'] = df['Rank'].str.upper().map(rank_order)
df['Strength'] = df['Rank_Num'] * 100 + df['Points']

# UI
st.title("Team Picker für Einsteiger")
selected_players = st.multiselect("Wähle 10 Spieler:", df['Name'].tolist())

if len(selected_players) == 10:
    if st.button("Neu zusammenstellen"):
        selected_df = df[df['Name'].isin(selected_players)].copy()
        selected_df = selected_df.sample(frac=1, random_state=random.randint(0, 10000))  # Spieler mischen

        team1, team2 = [], []
        strength1, strength2 = 0, 0

        for _, row in selected_df.iterrows():
            if strength1 <= strength2:
                team1.append(row)
                strength1 += row['Strength']
            else:
                team2.append(row)
                strength2 += row['Strength']

        st.subheader(f"Team 1 (Stärke: {strength1})")
        st.write(pd.DataFrame(team1)[['Name', 'Rank', 'Points']])
        
        st.subheader(f"Team 2 (Stärke: {strength2})")
        st.write(pd.DataFrame(team2)[['Name', 'Rank', 'Points']])
else:
    st.info("Bitte genau 10 Spieler auswählen.")


