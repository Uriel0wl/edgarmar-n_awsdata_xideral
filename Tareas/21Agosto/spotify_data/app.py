import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app
st.title("Visualización de Datos de Spotify 🎵")

# Sidebar
st.sidebar.title("Datos")
file = st.sidebar.file_uploader("Sube tu archivo data.csv")
st.sidebar.caption("Este dataset contiene características musicales de las canciones.")

if file is None:
    st.warning("Aquí falta un CSV")
    st.stop()

# Leer archivo
df = pd.read_csv(file)

# KPI principales
total_canciones = len(df)
liked_songs = df["liked"].sum()
avg_danceability = df["danceability"].mean()
avg_energy = df["energy"].mean()
avg_valence = df["valence"].mean()

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.metric("Total de canciones", total_canciones)
with c2:
    st.metric("Canciones favoritas", liked_songs)
with c3:
    st.metric("Promedio bailabilidad", round(avg_danceability, 2))
with c4:
    st.metric("Promedio energía", round(avg_energy, 2))
with c5:
    st.metric("Promedio positividad", round(avg_valence, 2))

st.markdown("----")

# Gráficos
cols = st.columns(2)

# Distribución de Loudness
with cols[0]:
    st.write("Distribución de Loudness")
    fig = plt.figure(figsize=(8,4))
    plt.hist(df["loudness"], bins=30, color="skyblue", edgecolor="black")
    plt.xlabel("Loudness (dB)")
    plt.ylabel("Cantidad de canciones")
    plt.title("Distribución de Loudness en las canciones")
    st.pyplot(fig, clear_figure=True)

# Comparación de Canciones liked vs no liked
with cols[1]:
    st.write("Canciones favoritas vs no favoritas")
    liked_counts = df["liked"].value_counts()
    fig = plt.figure(figsize=(6,4))
    plt.bar(liked_counts.index.astype(str), liked_counts.values, color=["orange","green"])
    plt.xticks([0,1], ["No favoritas","Favoritas"])
    plt.ylabel("Número de canciones")
    plt.title("Distribución de canciones favoritas")
    st.pyplot(fig, clear_figure=True)

st.markdown("---")