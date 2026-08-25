import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Baraka AI - Match Analyzer Pro",
    page_icon="⚽",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Style CSS Pro et Moderne (Mode Sombre)
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
st.markdown("<h1>⚽ Baraka AI - Match Analyzer Pro</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #90a4ae; font-size: 16px;'>Analyse Avancée : Forme, Classement & Mi-temps Prolifique</p>", unsafe_allow_html=True)
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🏠 Équipe Domicile")
    team_home = st.text_input("Nom Domicile", "Barcelone", key="home_name")
    home_rank = st.number_input("Classement actuel", min_value=1, max_value=20, value=2, key="h_rank")
    home_form = st.selectbox("Forme (3 derniers matchs)", ["🔥 3 Victoires", "⚖️ 2V - 1N", "⚖️ 1V - 2D", "❌ 3 Défaites"], index=0, key="h_form")
    home_goals_1mt = st.slider("Moy. buts 1MT", 0.0, 3.0, 1.1, 0.1, key="h_g1")
    home_goals_2mt = st.slider("Moy. buts 2MT", 0.0, 3.0, 1.5, 0.1, key="h_g2")

with col2:
    st.markdown("### ✈️ Équipe Extérieur")
    team_away = st.text_input("Nom Extérieur", "Real Madrid", key="away_name")
    away_rank = st.number_input("Classement actuel", min_value=1, max_value=20, value=1, key="a_rank")
    away_form = st.selectbox("Forme (3 derniers matchs)", ["🔥 3 Victoires", "⚖️ 2V - 1N", "⚖️ 1V - 2D", "❌ 3 Défaites"], index=1, key="a_form")
    away_goals_1mt = st.slider("Moy. buts 1MT", 0.0, 3.0, 0.9, 0.1, key="a_g1")
    away_goals_2mt = st.slider("Moy. buts 2MT", 0.0, 3.0, 1.3, 0.1, key="a_g2")

st.write("---")

# Bouton d'analyse professionnelle
if st.button("🚀 Lancer l'Analyse Professionnelle"):
    
    # 1. Calcul des buts par mi-temps
    score_1mt = home_goals_1mt + away_goals_1mt
    score_2mt = home_goals_2mt + away_goals_2mt
    
    # 2. Logique de calcul de la probabilité de victoire (basée sur le classement et la forme récente)
    # Plus le classement est petit (ex: 1er vs 5e) et la forme bonne, plus l'équipe a de points de score
    form_points = {"🔥 3 Victoires": 3, "⚖️ 2V - 1N": 2, "⚖️ 1V - 2D": 1, "❌ 3 Défaites": 0}
    
    home_strength = (21 - home_rank) * 2 + form_points[home_form]
    away_strength = (21 - away_rank) * 2 + form_points[away_form]
    
    total_strength = home_strength + away_strength
    if total_strength == 0:
        total_strength = 1
        
    prob_home = (home_strength / total_strength) * 100
    prob_away = (away_strength / total_strength) * 100
    prob_draw = max(10, 100 - (abs(prob_home - prob_away) + 40)) # Estimation réaliste du match nul
    # Rééquilibrage pour centrer sur 100%
    sum_p = prob_home + prob_away + prob_draw
    prob_home = (prob_home / sum_p) * 100
    prob_away = (prob_away / sum_p) * 100
    prob_draw = (prob_draw / sum_p) * 100

    # Affichage des résultats professionnels
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("<h3>📊 Rapport d'Analyse Avancée - Baraka AI</h3>", unsafe_allow_html=True)
    st.write(f"**Affiche :** {team_home} (Classé {home_rank}e) vs {team_away} (Classé {away_rank}e)")
    st.write("")
    
    st.markdown("#### 🎯 Probabilités de Victoire & Issue du Match")
    st.write(f"• Victoire **{team_home}** : **{prob_home:.1f}%**")
    st.write(f"• Match Nul : **{prob_draw:.1f}%**")
    st.write(f"• Victoire **{team_away}** : **{prob_away:.1f}%**")
    st.write("")
    
    st.markdown("#### ⏱️ Analyse des Mi-Temps (Buts Attendus)")
    st.write(f"• Buts 1ère mi-temps (1MT) : **{score_1mt:.2f}**")
    st.write(f"• Buts 2ème mi-temps (2MT) : **{score_2mt:.2f}**")
    
    if score_1mt > score_2mt:
        st.success("🔥 **Conseil Mi-Temps :** La 1ère mi-temps sera la plus prolifique en buts !")
    elif score_2mt > score_1mt:
        st.success("🔥 **Conseil Mi-Temps :** La 2ème mi-temps sera la plus prolifique en buts !")
    else:
        st.info("⚖️ **Conseil Mi-Temps :** Équilibre parfait entre les deux mi-temps.")
        
    st.markdown("</div>", unsafe_allow_html=True)







