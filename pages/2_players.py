import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

dataFrame = st.session_state['data']

clubes = dataFrame["Club"].value_counts().index
club = st.sidebar.selectbox("Clubes", clubes)

dataFrame_Players= dataFrame[dataFrame["Club"] == club]
players = dataFrame_Players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players)

player_stats = dataFrame[dataFrame["Name"] == player].iloc[0]

st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Position:** {player_stats['Position']}")

col1,col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura**{player_stats['Height(cm.)']/100} m")
col3.markdown(f"**Peso**{player_stats['Weight(lbs.)'] * 0.453:.2f} kg")

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1,col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
