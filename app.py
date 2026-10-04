import pandas as pd
import streamlit as st

# Konfigurasi dasar halaman dashboard
st.set_page_config(
    page_title="Mine Fleet Forecasting Dashboard",
    page_icon="⛏️",
    layout="wide",
)

st.title("⛏️ Dashboard Perencanaan Produksi Tambang")
st.markdown("---")


# Fungsi untuk mengambil data dari Google Sheet secara publik
@st.cache_data(ttl=600)
def load_data():
  # ID Google Sheet Anda
  sheet_id = "1WvnPCrEo3J-GoeZb0pYZAsX9D9uCqGMorQaiwbngGtg"
  # Menggunakan format ekspor CSV publik langsung berdasarkan nama sheet
  url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&sheet=BEP_Loader"
  df = pd.read_csv(url)
  return df


# Menjalankan aplikasi dan menampilkan data
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
      "Pastikan Google Sheet sudah dibagikan dengan akses 'Siapa saja yang"
      " memiliki link'."
  )
