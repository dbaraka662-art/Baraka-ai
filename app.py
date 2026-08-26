import streamlit as st
import random

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="BARAKA AI - Match Analyzer Pro",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

.stApp {
    background: #0d1117;
    color: #f0f6fc;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, sans-serif;
}

/* Header */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 25px;
    background: #111820;
    border-bottom: 1px solid #26303a;
    border-radius: 12px;
    margin-bottom: 25px;
}

.logo {
    font-size: 25px;
    font-weight: 800;
    color: #ffffff;
}

.logo span {
    color: #19c37d;
}

.status {
    background: #10251d;
    color: #19c37d;
    padding: 8px 14px;
    border-radius: 20px;
    font-size: 13px;
    font-weight: 600;
}

/* Cards */
.card {
    background: #151b23;
    border: 1px solid #27313b;
    border-radius: 14px;
    padding: 20px;
    margin-bottom: 18px;
}

.card-title {
    font-size: 17px;
    font-weight: 700;
    margin-bottom: 12px;
}

.big-number {
    font-size: 32px;
    font-weight: 800;
    color: #19c37d;
}

.small-text {
    color: #8b949e;
    font-size: 13px;
}

/* Verdict */
.verdict {
    background: linear-gradient(135deg, #10251d, #151b23);
    border: 1px solid #19c37d;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
}

.verdict-title {
    color: #8b949e;
    font-size: 14px;
}

.verdict-main {
    font-size: 30px;
    font-weight: 800;
    color: #19c37d;
    margin: 8px 0;
}

.confidence {
    font-size: 18px;
    font-weight: 700;
}

/* Team */
.team {
    text-align: center;
    background: #151b23;
    border: 1px solid #27313b;
    border-radius: 14px;
    padding: 25px;
}

.team-icon {
    font-size: 45px;
}

.team-name {
    font-size: 20px;
    font-weight: 800;
}

/* Progress */
.progress-container {
    background: #252c35;
    height: 10px;
    border-radius: 10px;
    overflow: hidden;
}

.progress-bar {
    height: 100%;
    background: #19c37d;
}

/* Hide Streamlit menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================

st.markdown("""
<div class="navbar">
    <div class="logo">⚽ BARAKA <span>AI</span></div>
    <div class="status">● ANALYSEUR PRO ACTIF</div>
</div>
""", unsafe_allow_html=True)

st.title("Match Analyzer Pro")
st.caption(
    "Analyse statistique avancée des buts par mi-temps"
)

# ============================================================
# SELECTION DES EQUIPES
# ============================================================

col1, col2, col3 = st.columns([1, 0.3, 1])

with col1:
    team_a = st.text_input(
        "Équipe à domicile",
        value="Équipe A"
    )

with col2:
    st.markdown(
        "<h2 style='text-align:center;margin-top:25px;'>VS</h2>",
        unsafe_allow_html=True
    )

with col3:
    team_b = st.text_input(
        "Équipe à l'extérieur",
        value="Équipe B"
    )

st.divider()

# ============================================================
# DONNEES
# ============================================================

st.subheader("📊 Données statistiques")

col1, col2, col3, col4 = st.columns(4)

with col1:
    buts_1_a = st.number_input(
        f"{team_a} — buts 1re MT",
        min_value=0.0,
        max_value=10.0,
        value=0.8,
        step=0.1
    )

with col2:
    buts_2_a = st.number_input(
        f"{team_a} — buts 2e MT",
        min_value=0.0,
        max_value=10.0,
        value=1.2,
        step=0.1
    )

with col3:
    buts_1_b = st.number_input(
        f"{team_b} — buts 1re MT",
        min_value=0.0,
        max_value=10.0,
        value=0.7,
        step=0.1
    )

with col4:
    buts_2_b = st.number_input(
        f"{team_b} — buts 2e MT",
        min_value=0.0,
        max_value=10.0,
        value=1.1,
        step=0.1
    )

# ============================================================
# CALCUL
# ============================================================

total_1 = buts_1_a + buts_1_b
total_2 = buts_2_a + buts_2_b

total = total_1 + total_2

if total > 0:
    proba_1 = (total_1 / total) * 100
    proba_2 = (total_2 / total) * 100
else:
    proba_1 = 50
    proba_2 = 50

if proba_1 > proba_2:
    meilleure_mi_temps = "1RE MI-TEMPS"
    confiance = proba_1
else:
    meilleure_mi_temps = "2E MI-TEMPS"
    confiance = proba_2

# ============================================================
# INDICATEURS
# ============================================================

st.subheader("🔥 Indicateurs principaux")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">1re mi-temps</div>
        <div class="big-number">{proba_1:.1f}%</div>
        <div class="small-text">Potentiel de buts</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">2e mi-temps</div>
        <div class="big-number">{proba_2:.1f}%</div>
        <div class="small-text">Potentiel de buts</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Total attendu</div>
        <div class="big-number">{total:.2f}</div>
        <div class="small-text">Buts statistiques</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Confiance</div>
        <div class="big-number">{confiance:.0f}%</div>
        <div class="small-text">Indice statistique</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# COMPARAISON
# ============================================================

st.subheader("📈 Comparaison des mi-temps")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">1re mi-temps</div>
        <p>Moyenne combinée : <b>{total_1:.2f}</b> buts</p>

        <div class="progress-container">
            <div class="progress-bar"
                 style="width:{proba_1}%"></div>
        </div>

        <p class="small-text">
            {proba_1:.1f}% du potentiel total
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">2e mi-temps</div>
        <p>Moyenne combinée : <b>{total_2:.2f}</b> buts</p>

        <div class="progress-container">
            <div class="progress-bar"
                 style="width:{proba_2}%"></div>
        </div>

        <p class="small-text">
            {proba_2:.1f}% du potentiel total
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# VERDICT
# ============================================================

st.subheader("🧠 Verdict BARAKA AI")

st.markdown(f"""
<div class="verdict">

<div class="verdict-title">
MI-TEMPS AVEC LE PLUS FORT POTENTIEL DE BUTS
</div>

<div class="verdict-main">
{meilleure_mi_temps}
</div>

<div class="confidence">
Indice de confiance : {confiance:.1f} / 100
</div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# ANALYSE AUTOMATIQUE
# ============================================================

st.subheader("🔎 Analyse automatique")

if proba_2 > proba_1:

    analyse = f"""
    **{team_a} vs {team_b}**

    Les données fournies indiquent une activité offensive plus importante
    en deuxième période.

    La moyenne combinée est de **{total_2:.2f} buts en deuxième mi-temps**
    contre **{total_1:.2f} en première mi-temps**.

    Plusieurs facteurs peuvent expliquer cette tendance : fatigue défensive,
    changements tactiques après la pause, espaces plus importants et
    nécessité pour une équipe menée au score de prendre davantage de risques.

    **Conclusion statistique : la deuxième mi-temps présente actuellement
    le potentiel de buts le plus élevé.**
    """

else:

    analyse = f"""
    **{team_a} vs {team_b}**

    Les données fournies indiquent une activité offensive plus importante
    en première période.

    La moyenne combinée est de **{total_1:.2f} buts en première mi-temps**
    contre **{total_2:.2f} en deuxième mi-temps**.

    Cela peut indiquer un début de match plus agressif, un pressing élevé
    ou une tendance des équipes à chercher rapidement l'ouverture du score.

    **Conclusion statistique : la première mi-temps présente actuellement
    le potentiel de buts le plus élevé.**
    """

st.markdown(
    f'<div class="card">{analyse}</div>',
    unsafe_allow_html=True
)

# ============================================================
# PERIODES DU MATCH
# ============================================================

st.subheader("⏱️ Zones potentielles de buts")

periods = [
    "0–15 min",
    "16–30 min",
    "31–45+ min",
    "46–60 min",
    "61–75 min",
    "76–90+ min"
]

# Simulation indicative basée sur la tendance des mi-temps
base = [
    0.10,
    0.14,
    0.16,
    0.15,
    0.20,
    0.25
]

for period, value in zip(periods, base):

    st.write(
        f"**{period} — potentiel indicatif : {value*100:.0f}%**"
    )

    st.progress(value)

# ============================================================
# AVERTISSEMENT
# ============================================================

st.warning(
    "⚠️ Cette analyse est statistique et ne garantit pas le résultat "
    "d'un match. Plus les données historiques sont fiables et nombreuses, "
    "plus l'analyse peut être pertinente."
)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "BARAKA AI © 2026 — Match Analyzer Pro | "
    "Analyse statistique football"
)













