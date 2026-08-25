import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="BARAKA AI - Match Analyzer Pro",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style CSS pour un design professionnel type grand site de paris
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #161b22;
        padding: 12px 24px;
        border-bottom: 1px solid #30363d;
        border-radius: 8px;
        margin-bottom: 20px;
    }
    .logo {
        color: #2ea043;
        font-weight: 900;
        font-size: 1.5rem;
        letter-spacing: 1px;
    }
    .nav-links {
        color: #8b949e;
        font-size: 0.95rem;
        font-weight: 600;
    }
    .hero {
        background: linear-gradient(135deg, #090d16 0%, #162235 100%);
        border: 1px solid #30363d;
        padding: 40px;
        border-radius: 16px;
        margin-bottom: 30px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.5);
    }
    .hero h1 {
        color: #ffffff;
        font-weight: 900;
        font-size: 2.3rem;
        margin-bottom: 10px;
    }
    .hero p {
        color: #8b949e;
        font-size: 1.1rem;
    }
    .card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stButton > button {
        background: linear-gradient(90deg, #238636 0%, #2ea043 100%);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1.1rem;
        width: 100%;
        box-shadow: 0 4px 14px rgba(35, 134, 54, 0.4);
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #2ea043 100%, #3fb950 100%);
    }
    .result-box {
        background: linear-gradient(135deg, #161b22 0%, #1f242c 100%);
        border-left: 6px solid #2ea043;
        border: 1px solid #30363d;
        padding: 25px;
        border-radius: 12px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Barre de navigation supérieure
st.markdown("""
    <div class="navbar">
        <div class="logo">⚽ BARAKA<span style="color: #ffffff;">AI</span></div>
        <div class="nav-links">Accueil &nbsp;&nbsp;|&nbsp;&nbsp; Expert Analyzer &nbsp;&nbsp;|&nbsp;&nbsp; Live Stats &nbsp;&nbsp;|&nbsp;&nbsp; Aide</div>
    </div>
""", unsafe_allow_html=True)

# Bannière principale
st.markdown("""
    <div class="hero">
        <h1>EXPERT FOOTBALL ANALYZER,<br><span style="color: #2ea043;">IA & STATISTIQUES AVANCÉES.</span></h1>
        <p>Saisissez n'importe quelle équipe au monde et obtenez une analyse spécialisée sur les mi-temps, les buts et les tendances 1N2.</p>
    </div>
""", unsafe_allow_html=True)

# Saisie libre des équipes et des paramètres d'expert
col_home, col_vs, col_away = st.columns([5, 1, 5])

with col_home:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### 🏠 Équipe Domicile")
    team_home = st.text_input("Nom de l'équipe Domicile", "Barcelone", key="h_name")
    home_form = st.selectbox("Forme récente (3 derniers matchs)", ["🔥 Excellente (3V)", "⚖️ Moyenne (2V-1N)", "⚖️ Alternée (1V-2D)", "❌ Mauvaise (3D)"], index=0, key="h_form")
    home_g1 = st.slider("Puissance offensive 1ère mi-temps (1MT)", 0.5, 2.5, 1.2, 0.1, key="h_1mt")
    home_g2 = st.slider("Puissance offensive 2ème mi-temps (2MT)", 0.5, 2.5, 1.6, 0.1, key="h_2mt")
    st.markdown("</div>", unsafe_allow_html=True)

with col_vs:
    st.markdown("<br><br><br><h2 style='text-align: center; color: #8b949e;'>VS</h2>", unsafe_allow_html=True)

with col_away:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("#### ✈️ Équipe Extérieure")
    team_away = st.text_input("Nom de l'équipe Extérieure", "Real Madrid", key="a_name")
    away_form = st.selectbox("Forme récente (3 derniers matchs)", ["🔥 Excellente (3V)", "⚖️ Moyenne (2V-1N)", "⚖️ Alternée (1V-2D)", "❌ Mauvaise (3D)"], index=1, key="a_form")
    away_g1 = st.slider("Puissance offensive 1ère mi-temps (1MT)", 0.5, 2.5, 1.0, 0.1, key="a_1mt")
    away_g2 = st.slider("Puissance offensive 2ème mi-temps (2MT)", 0.5, 2.5, 1.5, 0.1, key="a_2mt")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# Bouton d'analyse spécialisée
col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    run_expert_analysis = st.button("🚀 LANCER L'ANALYSE EXPERTE")

if run_expert_analysis:
    # 1. Logique spécialisée des buts par mi-temps
    score_1mt = home_g1 + away_g1
    score_2mt = home_g2 + away_g2
    
    # 2. Logique de calcul des points de forme pour les probabilités 1N2
    form_weights = {"🔥 Excellente (3V)": 3, "⚖️ Moyenne (2V-1N)": 2, "⚖️ Alternée (1V-2D)": 1, "❌ Mauvaise (3D)": 0}
    
    h_power = (home_g1 + home_g2) * 1.5 + form_weights[home_form]
    a_power = (away_g1 + away_g2) * 1.2 + form_weights[away_form] # Léger handicap extérieur expert
    
    total_power = h_power + a_power
    if total_power == 0:
        total_power = 1
        
    p_home = (h_power / total_power) * 100
    p_away = (a_power / total_power) * 100
    p_draw = max(15, 100 - (abs(p_home - p_away) + 40))
    
    # Normalisation à 100%
    sum_p = p_home + p_away + p_draw
    p_home = (p_home / sum_p) * 100
    p_away = (p_away / sum_p) * 100
    p_draw = (p_draw / sum_p) * 100

    # 3. Calcul spécialisé GG / NG (Les deux équipes marquent)
    gg_probability = "Élevée (Tendance GG ⚽)" if (home_g1 + home_g2 > 2.0 and away_g1 + away_g2 > 2.0) else "Modérée / Fermée"

    # Affichage du rapport expert
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #2ea043; text-align: center;'>📊 RAPPORT D'ANALYSE EXPERT - BARAKA AI</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.2rem;'><b>{team_home}</b> vs <b>{team_away}</b></p>", unsafe_allow_html=True)
    st.write("---")
    
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.markdown("#### 🎯 Probabilités & Marchés Clés")
        st.write(f"• Victoire **{team_home}** : **{p_home:.1f}%**")
        st.write(f"• Match Nul : **{p_draw:.1f}%**")
        st.write(f"• Victoire **{team_away}** : **{p_away:.1f}%**")
        st.write(f"• Option **GG / NG** : **{gg_probability}**")
        
    with res_col2:
        st.markdown("#### ⏱️ Analyse Avancée des Mi-Temps")
        st.write(f"• Indice de buts attendus (1MT) : **{score_1mt:.2f}**")
        st.write(f"• Indice de buts attendus (2MT) : **{score_2mt:.2f}**")
        
    st.write("")
    if score_1mt > score_2mt:
        st.success(f"🔥 **Conseil Stratégique Expert :** La 1ère mi-temps de **{team_home} vs {team_away}** présente un potentiel de buts supérieur !")
    elif score_2mt > score_1mt:
        st.success(f"🔥 **Conseil Stratégique Expert :** La 2ème mi-temps de **{team_home} vs {team_away}** sera la plus explosive (pression et fatigue adverses).")
    else:
        st.info(f"⚖️ **Conseil Stratégique Expert :** Rythme de match constant et équilibré attendu entre les deux mi-temps.")
        
    st.markdown("</div>", unsafe_allow_html=True)












