import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Sayfa ayarları
st.set_page_config(
    page_title="Dreammatch MVP",
    page_icon="💭",
    layout="centered"
)

st.title("Dreammatch 🚀")
st.subheader("Rüya Deneyimlerinizi Toplayın ve Analiz Edin")

# Kullanıcı girişi
isim = st.text_input("Adınız:")
if isim:
    st.success(f"Hoş geldiniz, {isim}!")

# Slider örneği
sayi = st.slider("Bir sayı seçin", 0, 100, 25)
st.write(f"Seçtiğiniz sayı: {sayi}")

# TextArea örneği
ruya = st.text_area("Rüyanızı yazın:")
if ruya:
    st.write("Rüyanız kaydedildi!")

# Örnek veri ve Plotly grafiği
st.subheader("Rüya Kategorileri Grafiği")
df = pd.DataFrame({
    "Kategori": ["Mutlu", "Korkulu", "Garip", "Normal"],
    "Sayı": np.random.randint(1, 20, size=4)
})

fig = px.bar(
    df,
    x="Kategori",
    y="Sayı",
    color="Kategori",
    title="Rüya Kategorileri",
    labels={"Kategori": "Rüya Türü", "Sayı": "Frekans"}
)
st.plotly_chart(fig, use_container_width=True)

# Örnek WordCloud (opsiyonel)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.subheader("Rüya Kelime Bulutu")
if ruya:
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(ruya)
    fig_wc, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig_wc)
else:
    st.info("Rüya kelime bulutu görmek için rüyanızı yukarıya yazın.")
