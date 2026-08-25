import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Baraka AI - Match Analyzer Pro",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Style CSS pour un design horizontal, sombre et haut de gamme
st.markdown("""
    <style>
    .stApp {
        background-color: #0d1117;
        color: #f0f6fc;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    .hero-banner {
        background: linear-gradient(135deg, #1f6feb 0%, #238636 100%);
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }
    .hero-banner h1 {
        color: #ffffff;
        font-weight: 900;
        font-size: 2.2rem;
        margin-bottom: 10px;
    }
    .hero-banner p {
        color: #e6edf3;
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
        border-left: 6px solid #238636;
        border-top: 1px solid #30363d;
        border-right: 1px solid #30363d;
        border-bottom: 1px solid #30363d;
        padding: 25px;
        border-radius: 12px;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Bannière d'en-tête professionnelle
st.markdown("""
    <div class="hero-banner">
        <h1>⚽ BARAKA AI - MATCH ANALYZER PRO</h1>
        <p>Analyse européenne globale : Premier League, La Liga, Serie A, Bundesliga, Ligue 1 & République tchèque.</p>
    </div>
""", unsafe_allow_html=True)

# Base de données massive : Top championnats européens + République tchèque
db_teams = {
    # --- ANGLETERRE (Premier League) ---
    "Manchester City (ENG)": {"rank": 1, "form": "🔥 3 Victoires", "g1": 1.3, "g2": 1.8},
    "Arsenal (ENG)": {"rank": 2, "form": "🔥 3 Victoires", "g1": 1.2, "g2": 1.5},
    "Liverpool (ENG)": {"rank": 3, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.6},
    "Aston Villa (ENG)": {"rank": 4, "form": "⚖️ 2V - 1N", "g1": 1.0, "g2": 1.4},
    "Tottenham (ENG)": {"rank": 5, "form": "⚖️ 1V - 2D", "g1": 1.2, "g2": 1.5},
    "Chelsea (ENG)": {"rank": 6, "form": "⚖️ 1V - 2D", "g1": 1.0, "g2": 1.4},
    "Manchester United (ENG)": {"rank": 7, "form": "⚖️ 1V - 2D", "g1": 0.9, "g2": 1.2},
    "Newcastle (ENG)": {"rank": 8, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.3},
    "West Ham (ENG)": {"rank": 9, "form": "❌ 3 Défaites", "g1": 0.8, "g2": 1.2},

    # --- ESPAGNE (La Liga) ---
    "Real Madrid (ESP)": {"rank": 1, "form": "🔥 3 Victoires", "g1": 1.1, "g2": 1.7},
    "Barcelone (ESP)": {"rank": 2, "form": "🔥 3 Victoires", "g1": 1.2, "g2": 1.6},
    "Girona (ESP)": {"rank": 3, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.5},
    "Atlético de Madrid (ESP)": {"rank": 4, "form": "⚖️ 2V - 1N", "g1": 0.9, "g2": 1.3},
    "Athletic Bilbao (ESP)": {"rank": 5, "form": "⚖️ 2V - 1N", "g1": 1.0, "g2": 1.2},
    "Real Sociedad (ESP)": {"rank": 6, "form": "⚖️ 1V - 2D", "g1": 0.8, "g2": 1.1},
    "Real Betis (ESP)": {"rank": 7, "form": "⚖️ 1V - 2D", "g1": 0.9, "g2": 1.2},

    # --- ITALIE (Serie A) ---
    "Inter Milan (ITA)": {"rank": 1, "form": "🔥 3 Victoires", "g1": 1.2, "g2": 1.6},
    "AC Milan (ITA)": {"rank": 2, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.4},
    "Juventus (ITA)": {"rank": 3, "form": "⚖️ 2V - 1N", "g1": 0.8, "g2": 1.3},
    "Atalanta (ITA)": {"rank": 4, "form": "🔥 3 Victoires", "g1": 1.1, "g2": 1.5},
    "Bologna (ITA)": {"rank": 5, "form": "⚖️ 2V - 1N", "g1": 0.9, "g2": 1.1},
    "AS Roma (ITA)": {"rank": 6, "form": "⚖️ 1V - 2D", "g1": 1.0, "g2": 1.3},
    "Napoli (ITA)": {"rank": 7, "form": "⚖️ 1V - 2D", "g1": 1.0, "g2": 1.3},
    "Lazio (ITA)": {"rank": 8, "form": "⚖️ 1V - 2D", "g1": 0.9, "g2": 1.2},

    # --- ALLEMAGNE (Bundesliga) ---
    "Bayer Leverkusen (GER)": {"rank": 1, "form": "🔥 3 Victoires", "g1": 1.3, "g2": 1.7},
    "Bayern Munich (GER)": {"rank": 2, "form": "🔥 3 Victoires", "g1": 1.5, "g2": 1.9},
    "Stuttgart (GER)": {"rank": 3, "form": "🔥 3 Victoires", "g1": 1.2, "g2": 1.6},
    "Leipzig (GER)": {"rank": 4, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.4},
    "Borussia Dortmund (GER)": {"rank": 5, "form": "⚖️ 2V - 1N", "g1": 1.2, "g2": 1.5},
    "Eintracht Frankfurt (GER)": {"rank": 6, "form": "⚖️ 1V - 2D", "g1": 1.0, "g2": 1.3},

    # --- FRANCE (Ligue 1) ---
    "PSG (FRA)": {"rank": 1, "form": "🔥 3 Victoires", "g1": 1.4, "g2": 1.8},
    "Monaco (FRA)": {"rank": 2, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.4},
    "Brest (FRA)": {"rank": 3, "form": "🔥 3 Victoires", "g1": 0.9, "g2": 1.2},
    "Lille (FRA)": {"rank": 4, "form": "⚖️ 2V - 1N", "g1": 1.0, "g2": 1.3},
    "Nice (FRA)": {"rank": 5, "form": "⚖️ 1V - 2D", "g1": 0.8, "g2": 1.1},
    "Marseille (FRA)": {"rank": 6, "form": "⚖️ 1V - 2D", "g1": 1.0, "g2": 1.3},
    "Lyon (FRA)": {"rank": 7, "form": "🔥 3 Victoires", "g1": 1.1, "g2": 1.4},
    "Lens (FRA)": {"rank": 8, "form": "⚖️ 1V - 2D", "g1": 0.9, "g2": 1.2},

    # --- RÉPUBLIQUE TCHÈQUE (Chance Liga) ---
    "Sparta Prague (CZE)": {"rank": 1, "form": "🔥 3 Victoires", "g1": 1.2, "g2": 1.6},
    "Slavia Prague (CZE)": {"rank": 2, "form": "🔥 3 Victoires", "g1": 1.2, "g2": 1.5},
    "Viktoria Plzeň (CZE)": {"rank": 3, "form": "⚖️ 2V - 1N", "g1": 1.1, "g2": 1.4},
    "Baník Ostrava (CZE)": {"rank": 4, "form": "⚖️ 2V - 1N", "g1": 0.9, "g2": 1.2},
    "Mladá Boleslav (CZE)": {"rank": 5, "form": "⚖️ 1V - 2D", "g1": 1.0, "g2": 1.3},
    "Slovácko (CZE)": {"rank": 6, "form": "⚖️ 1V - 2D", "g1": 0.8, "g2": 1.1}
}

teams_list = sorted(list(db_teams.keys()))

# Disposition Horizontale : Domicile vs Extérieur
col_home, col_vs, col_away = st.columns([5, 1, 5])

with col_home:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🏠 Équipe Domicile")
    sel_home = st.selectbox("Choisir l'équipe Domicile", teams_list, index=teams_list.index("Barcelone (ESP)"), key="h_sel")
    
    h_data = db_teams[sel_home]
    st.write(f"• **Classement officiel :** {h_data['rank']}e")
    st.write(f"• **Forme (3 derniers matchs) :** {h_data['form']}")
    st.write(f"• **Moy. Buts (1MT / 2MT) :** {h_data['g1']} / {h_data['g2']}")
    st.markdown("</div>", unsafe_allow_html=True)

with col_vs:
    st.markdown("<br><br><h2 style='text-align: center; color: #8b949e;'>VS</h2>", unsafe_allow_html=True)

with col_away:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### ✈️ Équipe Extérieure")
    sel_away = st.selectbox("Choisir l'équipe Extérieure", teams_list, index=teams_list.index("Real Madrid (ESP)"), key="a_sel")
    
    a_data = db_teams[sel_away]
    st.write(f"• **Classement officiel :** {a_data['rank']}e")
    st.write(f"• **Forme (3 derniers matchs) :** {a_data['form']}")
    st.write(f"• **Moy. Buts (1MT / 2MT) :** {a_data['g1']} / {a_data['g2']}")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")
st.write("")

# Bouton d'analyse centré
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    run_analysis = st.button("🚀 LANCER L'ANALYSE EUROPÉENNE")

if run_analysis:
    # 1. Calcul des buts par mi-temps
    score_1mt = h_data["g1"] + a_data["g1"]
    score_2mt = h_data["g2"] + a_data["g2"]
    
    # 2. Logique de calcul des probabilités de victoire
    form_pts = {"🔥 3 Victoires": 3, "⚖️ 2V - 1N": 2, "⚖️ 1V - 2D": 1, "❌ 3 Défaites": 0}
    
    h_strength = (21 - h_data["rank"]) * 2 + form_pts[h_data["form"]]
    a_strength = (21 - a_data["rank"]) * 2 + form_pts[a_data["form"]]
    
    total_str = h_strength + a_strength
    if total_str == 0: 
        total_str = 1
        
    p_home = (h_strength / total_str) * 100
    p_away = (a_strength / total_str) * 100
    p_draw = max(12, 100 - (abs(p_home - p_away) + 35))
    
    sum_p = p_home + p_away + p_draw
    p_home = (p_home / sum_p) * 100
    p_away = (p_away / sum_p) * 100
    p_draw = (p_draw / sum_p) * 100

    # Rapport d'analyse professionnel
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #3fb950; text-align: center;'>📊 RAPPORT D'ANALYSE OFFICIEL - BARAKA AI</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.2rem;'><b>{sel_home}</b> vs <b>{sel_away}</b></p>", unsafe_allow_html=True)
    st.write("---")
    
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.markdown("#### 🎯 Probabilités du Match (1N2)")
        st.write(f"• Victoire **{sel_home}** : **{p_home:.1f}%**")
        st.write(f"• Match Nul : **{p_draw:.1f}%**")
        st.write(f"• Victoire **{sel_away}** : **{p_away:.1f}%**")
        
    with res_col2:
        st.markdown("#### ⏱️ Tendances des Mi-Temps")
        st.write(f"• Buts attendus 1MT : **{score_1mt:.2f}**")
        st.write(f"• Buts attendus 2MT : **{score_2mt:.2f}**")
        
    st.write("")
    if score_1mt > score_2mt:
        st.success("🔥 **Avis IA :** La 1ère mi-temps est statistiquement la plus prolifique en buts !")
    elif score_2mt > score_1mt:
        st.success("🔥 **Avis IA :** La 2ème mi-temps est statistiquement la plus prolifique en buts !")
    else:
        st.info("⚖️ **Avis IA :** Activité offensive équilibrée entre les deux mi-temps.")
        
    st.markdown("</div>", unsafe_allow_html=True)










