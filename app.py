import streamlit as st

st.set_page_config(page_title="Baraka AI - Match Analyzer", page_icon="⚽", layout="centered")

st.title("⚽ Baraka AI - Match Analyzer")
st.markdown("### Prédisez la mi-temps la plus prolifique en buts !")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Équipe Domicile")
    equipe_dom = st.text_input("Nom de l'équipe", value="Arsenal")
    moy_1mt_dom = st.slider(f"Moyenne buts 1MT ({equipe_dom})", 0.0, 2.0, 0.7, 0.1)
    moy_2mt_dom = st.slider(f"Moyenne buts 2MT ({equipe_dom})", 0.0, 3.0, 1.4, 0.1)

with col2:
    st.subheader("✈️ Équipe Extérieur")
    equipe_ext = st.text_input("Nom de l'équipe", value="Chelsea")
    moy_1mt_ext = st.slider(f"Moyenne buts 1MT ({equipe_ext})", 0.0, 2.0, 0.5, 0.1)
    moy_2mt_ext = st.slider(f"Moyenne buts 2MT ({equipe_ext})", 0.0, 3.0, 1.1, 0.1)

st.markdown("---")
st.subheader("⚙️ Facteurs Avancés")
boost_h2h = st.checkbox("Historique H2H : Tendance forte aux buts précoces (+15% 1MT)", value=True)

if st.button("Lancer l'analyse Baraka AI 🚀", type="primary"):
    potentiel_1mt = moy_1mt_dom + moy_1mt_ext
    potentiel_2mt = moy_2mt_dom + moy_2mt_ext
    
    if boost_h2h:
        potentiel_1mt *= 1.15
        
    somme_totale = potentiel_1mt + potentiel_2mt
    
    if somme_totale > 0:
        prob_1mt = (potentiel_1mt / somme_totale) * 100
        prob_2mt = (potentiel_2mt / somme_totale) * 100
    else:
        prob_1mt, prob_2mt = 50.0, 50.0
        
    verdict = "1ère Mi-Temps (1MT)" if prob_1mt > prob_2mt else "2ème Mi-Temps (2MT)"
    diff = abs(prob_1mt - prob_2mt)
    
    if diff > 25:
        confiance = "🔥 Forte (Value Bet Recommandé)"
    elif diff > 12:
        confiance = "⚡ Moyenne"
    else:
        confiance = "⚠️ Faible (Match Neutre)"

    st.markdown("---")
    st.subheader(f"📊 Résultats pour : {equipe_dom} vs {equipe_ext}")
    
    col_res1, col_res2 = st.columns(2)
    col_res1.metric(label="Probabilité But 1MT", value=f"{prob_1mt:.1f}%")
    col_res2.metric(label="Probabilité But 2MT", value=f"{prob_2mt:.1f}%")
    
    st.success(f"🎯 **Mi-temps la plus prolifique :** {verdict}")
    st.info(f"⚡ **Indice de Confiance :** {confiance}")
