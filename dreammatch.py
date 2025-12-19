# app.py
import streamlit as st
import pandas as pd
from collections import Counter
import plotly.express as px

# Sayfa ayarları
st.set_page_config(page_title="Dreammatch MVP", layout="centered")
st.title("Dreammatch - Rüya Analiz MVP")

st.write("Lütfen rüyanızı girin ve 'Analiz Et' butonuna tıklayın:")

# Kullanıcıdan rüya girişi
user_input = st.text_area("Rüya metni", height=150)

if st.button("Analiz Et") and user_input.strip() != "":
    # Metni küçük harfe çevir ve kelimeleri ayır
    words = [word.strip(".,!?").lower() for word in user_input.split()]
    
    # En sık geçen kelimeleri say
    word_counts = Counter(words)
    
    # En sık 10 kelimeyi seç
    most_common = word_counts.most_common(10)
    df = pd.DataFrame(most_common, columns=["Kelime", "Frekans"])
    
    # Bar chart ile görselleştir
    fig = px.bar(
        df, x="Kelime", y="Frekans", text="Frekans",
        title="Rüyanızdaki Kelime Frekansları"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(yaxis=dict(title="Frekans"), xaxis=dict(title="Kelime"))
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Rüyanızı girdikten sonra 'Analiz Et' butonuna basın.")
