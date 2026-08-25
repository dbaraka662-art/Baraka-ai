import streamlit as st

# Configuration de la page (Propre et professionnelle)
st.set_page_config(
    page_title="Baraka AI - Match Analyzer PRO",
    page_icon="📊",
    layout="wide", # Utilise plus d'espace pour aérer
    initial_sidebar_state="collapsed"
)

# Style CSS personnalisé pour un design Épuré & Premium
st.markdown("""
    <style>
    /* --- Fond Global et Typographie --- */
    .stApp {
        background-color: #121212; /* Fond noir profond */
        color: #e0e0e0; /* Texte gris très clair pour le confort */
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* --- Titres --- */
    h1 {
        color: #2ecc71; /* Vert émeraude professionnel */
        font-weight: 800;
        text-align: center;
        letter-spacing: -1.5px; /* Espacement des lettres réduit pour un effet moderne */
        margin-bottom: 10px;
    }
    
    h3 {
        color: #ffffff;
        border-bottom: 1px solid #333; /* Ligne de séparation discrète */
        padding-bottom: 10px;
        margin-top: 25px;
        font-size: 1.2rem;
    }

    /* --- Conteneurs (Cartes) --- */
    .main .block-container {
        padding-top: 2rem;
    }
    
    .css-1r6slhn.e1tzin5v0 { /* Conteneur principal de Streamlit */
        background-color: #1e1e1e; /* Couleur de fond des cartes */
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }

    /* --- Sliders (Curseurs) --- */
    .stSlider > div > div > div > div {
        background-color: #2ecc71; /* Couleur de la barre active du curseur */
    }
    .stSlider > div > label {
        color: #b0bec5; /* Couleur des étiquettes des sliders */
        font-size: 0.9rem;
    }
    
    /* --- Boutons --- */
    .stButton > button {
        background: linear-gradient(90deg, #2ecc71 0%, #27ae60 100%);
        color: white;
        border: none;
        padding: 12px 28px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(46, 204, 113, 0.3);
        text-transform: uppercase; /* Effet majuscules sur le bouton */
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #27ae60 0%, #219150 100%);
        box-shadow: 0 6px 16px rgba(46, 204, 113, 0.4);
        transform: translateY(-1px); /* Léger effet de soulèvement au survol */
    }

    /* --- Boîte de Résultat (Le cœur du pronostic) --- */
    .result-box {
        background: linear-gradient(135deg, #1e1e1e 0%, #2c2c2c 100%);
        border-left: 6px solid #2ecc71; /* Barre verticale verte premium */
        padding: 25px;
        border-radius: 12px;
        margin-top: 30px;
        text-align: left; /* Alignement à gauche plus formel */
    }
    
    .result-title {
        color: #2ecc71;
        font-weight: 700;
        font-size: 1.5rem;
        margin-bottom: 10px;
    }
    
    .result-details {
        color: #e0e0e0;
        font-size: 1.1rem;
        line-height: 1.6;
        margin-top: 10px;
    }
    
    /* --- Éléments divers --- */
    .stTextInput > label {
        color: #b0bec5;
    }
    .stTextInput > div > div > input {
        background-color: #2c2c2c;
        color: white;
        border-radius: 8px;
        border: 1px solid #424242;
    }
    </style>
""", unsafe_allow_html=True)

# En-tête de l'application (Utilisation de colonnes pour centrer proprement)
header_col1, header_col2, header_col3 = st.columns([1, 2, 1])
with header_col2:
    st.markdown("<h1>⚽ Baraka AI - Match Analyzer</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #90a4ae; font-size: 18px; font-weight: 300;'>Analyse prédictive avancée des moments forts en buts</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid #333;'>", unsafe_allow_html=True)
    st.write("")

# Disposition en 2 grandes colonnes pour aérer
col_left, col_right = st.columns(2)

# Section Équipe Domicile (Colonne de gauche)
with col_left:
    st.markdown("### 🏠 Équipe Domicile")
    team_home = st.text_input("Nom de l'équipe à domicile", "Arsenal", key="home_pro")
    st.write("")
    home_1mt = st.slider(f"Moyenne de buts marqués (1MT) - {team_home}", 0.0, 3.0, 1.5, 0.05, help="Buts marqués en première mi-temps par cette équipe à domicile")
    home_2mt = st.slider(f"Moyenne de buts marqués (2MT) - {team_home}", 0.0, 3.0, 1.4, 0.05, help="Buts marqués en deuxième mi-temps par cette équipe à domicile")

# Section Équipe Extérieure (Colonne de droite)
with col_right:
    st.markdown("### ✈️ Équipe Extérieure")
    team_away = st.text_input("Nom de l'équipe à l'extérieur", "Chelsea", key="away_pro")
    st.write("")
    away_1mt = st.slider(f"Moyenne de buts encaissés (1MT) - {team_away}", 0.0, 3.0, 1.1, 0.05, help="Buts encaissés en première mi-temps par cette équipe à l'extérieur")
    away_2mt = st.slider(f"Moyenne de buts encaissés (2MT) - {team_away}", 0.0, 3.0, 1.6, 0.05, help="Buts encaissés en deuxième mi-temps par cette équipe à l'extérieur")

st.write("")
st.write("---")

# Bouton d'analyse stylé (Centré)
btn_col1, btn_col2, btn_col3 = st.columns([2, 1, 2])
with btn_col2:
    analyze_btn = st.button("🚀 Générer le Pronostic", use_container_width=True)

# Logique de calcul et Affichage du Résultat (En pleine largeur)
if analyze_btn:
    # Calculs (basés sur les moyennes entrées)
    score_1mt = home_1mt + away_1mt
    score_2mt = home_2mt + away_2mt
    
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown("<div class='result-title'>📊 Verdict Baraka AI</div>", unsafe_allow_html=True)
    
    # Affichage des données de comparaison
    st.markdown(f"""
    <div class='result-details'>
    Sur la base de vos statistiques pour le match <strong>{team_home} (Dom.)</strong> vs <strong>{team_away} (Ext.)</strong> :
    <br><br>
    🔹 <strong>Buts attendus (1ère MT) :</strong> {home_1mt:.2f} (Marqués) + {away_1mt:.2f} (Encaissés) = <strong>{score_1mt:.2f}</strong> buts
    <br>
    🔹 <strong>Buts attendus (2ème MT) :</strong> {home_2mt:.2f} (Marqués) + {away_2mt:.2f} (Encaissés) = <strong>{score_2mt:.2f}</strong> buts
    <br><br>
    </div>
    """, unsafe_allow_html=True)
    
    # Analyse du résultat et affichage de la conclusion
    diff = abs(score_1mt - score_2mt)
    
    if score_1mt > score_2mt:
        if diff > 0.3:
            st.success(f"💡 **Conseil Stratégique :** Forte probabilité que la **PREMIÈRE MI-TEMPS (1MT)** soit plus riche en buts (Écart significatif).")
        else:
            st.info(f"💡 **Conseil Stratégique :** Léger avantage statistique pour la **PREMIÈRE MI-TEMPS (1MT)**, mais l'écart est faible.")
            
    elif score_2mt > score_1mt:
        if diff > 0.3:
            st.success(f"💡 **Conseil Stratégique :** Forte probabilité que la **DEUXIÈME MI-TEMPS (2MT)** soit plus riche en buts (Écart significatif).")
        else:
            st.info(f"💡 **Conseil Stratégique :** Léger avantage statistique pour la **DEUXIÈME MI-TEMPS (2MT)**, mais l'écart est faible.")
            
    else:
        st.warning("⚖️ **Conseil Stratégique :** Équilibre parfait. Aucune mi-temps ne se détache statistiquement.")
        
    st.markdown("</div>", unsafe_allow_html=True)



