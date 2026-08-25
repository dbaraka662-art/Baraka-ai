import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Baraka AI - Match Analyzer",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS Pro et Moderne
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    h1 {
        color: #2ecc71;
        font-weight: 800;
        text-align: center;
        letter-spacing: -1px;
    }
    h3 {
        color: #ffffff;
        border-bottom: 1px solid #333;
        padding-bottom: 8px;
        margin-top: 25px;
    }
    .stButton > button {
        background: linear-gradient(90deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        width: 100%;
        box-shadow: 0 4px 12px rgba(46, 204, 113, 0.3);
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #27ae60 100%, #219150 100%);
    }
    .result-box {
        background: linear-gradient(135deg, #1e1e1e 0%, #2c2c2c 100%);
        border-left: 6px solid #2ecc71;
        padding: 20px;
        border-radius: 12px;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête
st.markdown("<h1>⚽ Baraka AI - Match Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #90a4ae; font-size: 16px;'>Analyse automatisée de la mi-temps la plus prolifique</p>", unsafe_allow_html=True)
st.write("")

# Base de données simulée de statistiques fiables pour éviter les erreurs de saisie
stats_database = {
    "Barcelone": {"1mt": 1.1, "2mt": 1.4},
    "Real Madrid": {"1mt": 1.0, "2mt": 1.5},
    "Manchester City": {"1mt": 1.2, "2mt": 1.6},
    "Arsenal": {"1mt": 0.9, "2mt": 1.3},
    "PSG": {"1mt": 1.3, "2mt": 1.5},
    "Bayern Munich": {"1mt": 1.4, "2mt": 1.7},
    "Liverpool": {"1mt": 1.1, "2mt": 1.4},
    "Autre / Personnalisé": {"1mt": 1.0, "2mt": 1.2}
}

teams_list = list(stats_database.keys())

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏠 Domicile")
    team_home = st.selectbox("Équipe Domicile", teams_list, index=0)
    # Attribution automatique des stats selon l'équipe choisie
    h_1mt = stats_database[team_home]["1mt"]
    h_2mt = stats_database[team_home]["2mt"]
    st.info(f"Moyenne auto : 1MT ({h_1mt}) | 2MT ({h_2mt})")

with col2:
    st.markdown("### ✈️ Extérieur")
    team_away = st.selectbox("Équipe Extérieur", teams_list, index=1)
    # Attribution automatique des stats
    a_1mt = stats_database[team_away]["1mt"]
    a_2mt = stats_database[team_away]["2mt"]
    st.info(f"Moyenne auto : 1MT ({a_1mt}) | 2MT ({a_2mt})")

st.write("---")

# Bouton d'analyse automatisée
if st.button("🚀 Lancer l'Analyse Automatique"):
    score_1mt = h_1mt + a_1mt
    score_2mt = h_2mt + a_2mt
    
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("### 📊 Résultats de l'Analyse Baraka AI", unsafe_allow_html=True)
    st.write(f"**{team_home}** vs **{team_away}**")
    st.write(f"• Buts attendus en 1ère mi-temps (1MT) : **{score_1mt:.2f}**")
    st.write(f"• Buts attendus en 2ème mi-temps (2MT) : **{score_2mt:.2f}**")
    st.write("")
    
    if score_1mt > score_2mt:
        st.success("🔥 Tendance forte : La 1ère mi-temps sera la plus prolifique en buts !")
    elif score_2mt > score_1mt:
        st.success("🔥 Tendance forte : La 2ème mi-temps sera la plus prolifique en buts !")
    else:
        st.info("⚖️ Équilibre parfait entre les deux mi-temps.")
        
    st.markdown("</div>", unsafe_allow_html=True)





