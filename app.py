import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Baraka AI - Match Analyzer",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un design pro et moderne
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    h1 {
        color: #00ff7f;
        font-weight: 800;
        text-align: center;
        letter-spacing: -1px;
    }
    h3 {
        color: #ffffff;
        border-bottom: 2px solid #1f2937;
        padding-bottom: 8px;
    }
    .card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    .result-box {
        background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
        border: 2px solid #00ff7f;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-top: 25px;
        box-shadow: 0 4px 20px rgba(0, 255, 127, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# En-tête de l'application
st.markdown("<h1>⚽ Baraka AI - Match Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 16px;'>Prédisez la mi-temps la plus prolifique en buts avec précision !</p>", unsafe_allow_html=True)
st.write("")

# Section Équipe Domicile
st.markdown("### 🏠 Équipe Domicile")
team_home = st.text_input("Nom de l'équipe à domicile", "Arsenal", key="home")

col1, col2 = st.columns(2)
with col1:
    home_1mt = st.slider(f"Buts 1MT ({team_home})", 0.0, 3.0, 1.5, 0.1)
with col2:
    home_2mt = st.slider(f"Buts 2MT ({team_home})", 0.0, 3.0, 1.4, 0.1)

st.write("")

# Section Équipe Extérieure
st.markdown("### ✈️ Équipe Extérieure")
team_away = st.text_input("Nom de l'équipe à l'extérieur", "Chelsea", key="away")

col3, col4 = st.columns(2)
with col3:
    away_1mt = st.slider(f"Buts 1MT ({team_away})", 0.0, 3.0, 1.1, 0.1)
with col4:
    away_2mt = st.slider(f"Buts 2MT ({team_away})", 0.0, 3.0, 1.6, 0.1)

st.write("---")

# Bouton d'analyse stylé
if st.button("🚀 Lancer l'Analyse Avancée", use_container_width=True):
    total_home = home_1mt + home_2mt
    total_away = away_1mt + away_2mt
    
    score_1mt = home_1mt + away_1mt
    score_2mt = home_2mt + away_2mt
    
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("### 📊 Résultats de l'Analyse Baraka AI")
    
    st.write(f"**{team_home}** (Total attendu : {total_home:.2f}) vs **{team_away}** (Total attendu : {total_away:.2f})")
    
    if score_1mt > score_2mt:
        st.success("🔥 Tendance forte : La 1ère mi-temps sera la plus prolifique en buts !")
    elif score_2mt > score_1mt:
        st.success("🔥 Tendance forte : La 2ème mi-temps sera la plus prolifique en buts !")
    else:
        st.info("⚖️ Équilibre parfait : Autant de buts attendus en 1ère qu'en 2ème mi-temps.")
        
    st.markdown("</div>", unsafe_allow_html=True)


