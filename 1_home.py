import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

if "data" not in st.session_state:
    dataFrame = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    dataFrame = dataFrame[dataFrame["Contract Valid Until"] >= datetime.today().year]
    dataFrame = dataFrame[dataFrame["Value(£)"] > 0]
    dataFrame = dataFrame.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = dataFrame

st.markdown("# FIFA OFFICIAL DATASET! ⚽")

button = st.button("Acesse os dados no Kaggle")
if button:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """O conjunto de dados de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém 
    uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características
    físicas, estatísticas de jogo, detalhes de contratos e afiliações de clubes.

    Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados ​​em explorar vários aspectos 
    do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho, 
    avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento do
    jogador ao longo do tempo."""
)
