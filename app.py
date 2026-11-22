import streamlit as st
from utils.loader import load_data

st.set_page_config(page_title="Asisten Rekomendasi Gadget", page_icon="📱", layout="wide")

st.title("📱 Asisten Rekomendasi Gadget")
st.caption("Cari, bandingkan, dan tanya rekomendasi HP berdasarkan spesifikasi dan budget.")

df = load_data()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Jumlah HP", f"{len(df):,}")
c2.metric("Jumlah merek", df["brand"].nunique())
c3.metric("Harga median", f"Rp {df['price_idr'].median():,.0f}")
c4.metric("Median RAM", f"{df['ram'].median():g} GB")

st.subheader("Pratinjau data")
st.dataframe(df.head(50), use_container_width=True)

st.info("Gunakan menu di sidebar untuk membuka halaman lain.")