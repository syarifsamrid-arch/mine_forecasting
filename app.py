import pandas as pd
import streamlit as st

# Konfigurasi dasar halaman dashboard agar optimal di tablet
st.set_page_config(
    page_title="Mine Fleet Forecasting Dashboard",
    page_icon="⛏️️",
    layout="wide",
)

st.title("⛏️ Dashboard Perencanaan Produksi Tambang")
st.markdown("---")


# Fungsi untuk memuat data dari link Publish to web Google Sheet
@st.cache_data(ttl=600)
def load_data():
  # Ganti teks di dalam tanda kutip ini dengan link Publish to web CSV Anda
  url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vShY03UVBEsn81UsGjW9lopvv-LFKiITDQPPjsoakZyAsQmxlYly6o-kU17C-q8XwP9V-yl3bBhOrVg/pub?output=csv"
  df = pd.read_csv(url)
  return df


# Menjalankan aplikasi dan menampilkan data ke dashboard
try:
  with st.spinner("Memuat data dari Google Sheet..."):
    df_loader = load_data()

  st.success("Data berhasil dimuat!")

  # Menampilkan tabel data di dashboard
  st.subheader("📋 Data Unit Class & Kapasitas Alat (BEP Loader)")
  st.dataframe(df_loader, use_container_width=True)

  st.markdown("---")
  st.info(
      "Aplikasi terhubung secara real-time dengan Google Sheet database Anda."
  )

except Exception as e:
  st.error(f"Terjadi kesalahan saat memuat data: {e}")
  st.write(
      "Pastikan tautan 'Publish to web' berformat CSV sudah dimasukkan dengan"
      " benar di dalam kode."
  )
