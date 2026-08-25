import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Baraka AI - Match Analyzer",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un design Pro et Moderne (Mode Sombre)
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
        background: linear-gradient(90deg, #27ae60 0%, #219150 100%);
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

# En-tête de l'application
st.markdown("<h1>⚽ Baraka AI - Match Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #90a4ae; font-size: 16px;'>Prédisez la mi-temps la plus prolifique en buts !</p>", unsafe_allow_html=True)
st.write("")

# Section Équipe Domicile
st.markdown("### 🏠 Équipe Domicile")
team_home = st.text_input("Nom de l'équipe à domicile", "Barcelone", key="home")
home_1mt = st.slider(f"Moyenne buts 1MT ({team_home})", 0.0, 3.0, 0.8, 0.05)
home_2mt = st.slider(f"Moyenne buts 2MT ({team_home})", 0.0, 3.0, 1.2, 0.05)

st.write("")

# Section Équipe Extérieure
st.markdown("### ✈️ Équipe Extérieure")
team_away = st.text_input("Nom de l'équipe à l'extérieur", "Real Madrid", key="away")
away_1mt = st.slider(f"Moyenne buts 1MT ({team_away})", 0.0, 3.0, 0.5, 0.05)
away_2mt = st.slider(f"Moyenne buts 2MT ({team_away})", 0.0, 3.0, 1.1, 0.05)

st.write("---")

# Bouton et Logique de l'analyse
if st.button("🚀 Lancer l'Analyse Avancée"):
    score_1mt = home_1mt + away_1mt
    score_2mt = home_2mt + away_2mt
    
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("<h3>📊 Résultats de l'Analyse</h3>", unsafe_allow_html=True)
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




