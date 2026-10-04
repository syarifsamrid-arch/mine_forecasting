import pandas as pd
import streamlit as st

# Konfigurasi dasar halaman dashboard agar optimal di tablet
st.set_page_config(
    page_title="Mine Fleet Forecasting Dashboard",
    page_icon="⛏️",
    layout="wide",
)

st.title("⛏️ Dashboard Perencanaan Produksi Tambang")
st.markdown("---")

# ID Google Sheet Anda
SHEET_ID = "1WvnPCrEo3J-GoeZb0pYZAsX9D9uCqGMorQaiwbngGtg"

# Daftar lengkap seluruh sheet berdasarkan struktur database Anda
daftar_sheet = [
    "Calendar_Setup",
    "National_Holidays",
    "Fasting_Schedule",
    "BEP_Loader",
    "BEP_Hauler",
    "BEP_Mining_Services",
    "BEP_General_Services",
    "BEP_STD_CT_Loader",
    "BOP_Time_Efficiency",
    "BOP_Work_Efficiency",
    "BOP_Efficiency_Factors",
    "BOP_Operating_Condition",
    "BOP_Operator_Skills",
    "BOP_Bucket_Factors",
    "BMP_Material_List",
    "Data_PA",
    "MFS_Distance_Plan",
    "MFS_Dynamic_Fleet",
    "MFS_Dynamic_Utilization_Board",
]


# Fungsi untuk mengambil data menggunakan metode ekspor CSV publik langsung dari Google
@st.cache_data(ttl=600)
def load_sheet_data(sheet_name):
  # Menggunakan format ekspor GID alternatif yang lebih stabil
  url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
  df = pd.read_csv(url)
  return df


# Membuat navigasi pilihan sheet di bagian Sidebar (Menu Samping)
st.sidebar.header("📂 Navigasi Database Tambang")
selected_sheet = st.sidebar.selectbox("Pilih Modul / Sheet:", daftar_sheet)

st.sidebar.markdown("---")
st.sidebar.info(
    "Aplikasi terhubung langsung dengan Google Sheet database perencanaan"
    " produksi."
)

# Catatan Penting untuk memastikan Google Sheet terbaca publik
st.sidebar.warning(
    "⚠️ **Catatan Penting Akses:**\nPastikan Google Sheet Anda sudah melalui"
    " menu **File > Share > Publish to web** (Publikasikan ke web), lalu"
    " pilih *Entire Document* dan klik **Publish** agar server luar bisa"
    " membaca seluruh sheet."
)

# Menjalankan aplikasi dan menampilkan data dari sheet yang dipilih
try:
  with st.spinner(f"Memuat data dari sheet '{selected_sheet}'..."):
    df_data = load_sheet_data(selected_sheet)

  st.success(f"Berhasil memuat data: **{selected_sheet}**")

  # Menampilkan ringkasan jumlah baris dan kolom
  col1, col2 = st.columns(2)
  with col1:
    st.metric("Total Baris Data", df_data.shape[0])
  with col2:
    st.metric("Total Kolom", df_data.shape[1])

  # Menampilkan tabel data interaktif
  st.subheader(f"📋 Tabel Data: {selected_sheet}")
  st.dataframe(df_data, use_container_width=True)

except Exception as e:
  st.error(f"Gagal memuat sheet '{selected_sheet}'.")
  st.info(
      "**Solusi Cepat 404:**\nBuka Google Sheet Anda -> Klik menu **File** ->"
      " **Share** -> **Publish to web** -> Klik tombol **Publish**. Hal ini"
      " wajib dilakukan agar Google mengizinkan aplikasi luar mengunduh datanya"
      " secara publik."
  )
  with st.expander("Lihat detail teknis error"):
    st.write(e)
