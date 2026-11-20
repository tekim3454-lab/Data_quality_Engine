import streamlit as st

from analyzer import (
    charger_donnees,
    valeurs_manquantes,
    doublons,
    valeurs_uniques,
    verifier_types,
)

st.title("Data Quality Analyzer")

# 4.1 Upload du fichier
fichier = st.file_uploader("Choisis un fichier CSV", type=["csv"])

# 4.2 On analyse seulement si un fichier a été donné
if fichier is not None:
    data = charger_donnees(fichier)

    # 4.3 Aperçu
    st.subheader("1. Aperçu")
    st.write("Dimensions :", data.shape)
    st.dataframe(data.head())
    st.write("Statistiques :")
    st.dataframe(data.describe(include="all"))

    # 4.4 Types
    st.subheader("2. Types des colonnes")
    st.dataframe(verifier_types(data).astype(str))

    # 4.5 Valeurs manquantes
    st.subheader("3. Valeurs manquantes")
    st.dataframe(valeurs_manquantes(data))

    # 4.6 Doublons
    st.subheader("4. Doublons")
    nb, lignes = doublons(data)
    st.write("Nombre de doublons :", nb)
    st.dataframe(lignes)

    # 4.7 Valeurs uniques
    st.subheader("5. Valeurs uniques par colonne")
    st.dataframe(valeurs_uniques(data))

  