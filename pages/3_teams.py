import streamlit as st

st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

dataFrame = st.session_state["data"]
# Selecione o clube a partir do sidebar
clubes = dataFrame["Club"].value_counts().index
club = st.sidebar.selectbox("Clubes", clubes)

# Filtrando o DataFrame pelo clube selecionado
dataFrame_filtered = dataFrame[dataFrame["Club"] == club].set_index("Name")
st.image(dataFrame_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# Definindo as colunas a serem exibidas no DataFrame
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined',
            'Height(cm.)', 'Weight(lbs.)', 
            'Contract Valid Until', 'Release Clause(£)']

st.dataframe(dataFrame_filtered[columns], 
            column_config={
                "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0),
                "Value(£)": st.column_config.NumberColumn(),
                "Wage(£)": st.column_config.NumberColumn("Weekly Wage", format="£%f", min_value=0, max_value=dataFrame_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country")
    }
)