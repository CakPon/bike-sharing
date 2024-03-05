import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data
df_day = pd.read_csv('dashboard/day.csv')
df_hour = pd.read_csv('dashboard/hour.csv')

# Mengubah format kolom 'dteday' menjadi datetime
df_day['dteday'] = pd.to_datetime(df_day['dteday'])
df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

# Sidebar
st.sidebar.title("Analisis Data Bike Sharing")

# Pertanyaan Bisnis
st.sidebar.markdown("**Pertanyaan Bisnis:**")
st.sidebar.markdown("Bagaimana Persebaran Jumlah User per Jam-nya?")
st.sidebar.markdown("Dalam Kondisi/Cuaca Apa yang Memiliki User Terbanyak?")

# Informasi Sekilas
st.title("Informasi Sekilas")

# Menampilkan statistik penting
st.metric("Jumlah Pengguna", df_day['cnt'].sum())
st.metric("Rata-rata Penggunaan Harian", df_day['cnt'].mean())

# Waktu Penggunaan berdasarkan jam
st.markdown("## Waktu Penggunaan")

# Visualisasi Waktu penggunaan berdasarkan jam
fig_hourly = plt.figure()
plt.bar(df_hour['hr'], df_hour['cnt'])
plt.xlabel('Hour')
plt.ylabel('Average User')
plt.title('Distribution of Users per Hour')
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig_hourly)

# Visualisasi Jumlah User sesuai cuacanya
fig_weather = plt.figure()
plt.bar(df_day['weathersit'], df_day['cnt'], color=['green'])  
plt.xlabel('Weather Situation')
plt.ylabel('Total User')
plt.title('Total Users by Weather Situation')
plt.grid(axis='y', alpha=0.7)
st.pyplot(fig_weather)  

# Analisis Faktor
st.markdown("## Analisis Faktor")

# Memilih faktor
faktor = st.selectbox("Pilih Faktor", ['Temperatur', 'Waktu'])

if faktor == 'Temperatur':
    # Visualisasi pengaruh temperatur
    fig_temp = plt.figure()
    sns.lmplot(x='temp', y='cnt', data=df_day)
    st.pyplot(fig_temp)

elif faktor == 'Waktu (Per Jam)':
    # Pastikan 'dteday' bertipe datetime
    if not pd.api.types.is_datetime64_dtype(df_hour['dteday']):
        df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

    # Plot jumlah pengguna terdaftar vs. jam
    fig_hourly_registered = plt.figure()
    plt.plot(df_hour['dteday'].dt.hour, df_hour['cnt'])
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Pengguna Terdaftar')
    st.pyplot(fig_hourly_registered)

# Kesimpulan
st.markdown("## Kesimpulan")

# Menampilkan kesimpulan berdasarkan hasil analisis
st.markdown("Dapat disimpulkan kalau pada malam hari hingga fajar (23.00-05.00) memiliki rata-rata user yang paling sedikit dibanding jam lainnya, dan pada jam 17.00-18.00 merupakan jam dengan jumlah user terbanyak.")
st.markdown("Kondisi/cuaca dengan user terbanyak adalah di saat cuaca bersih/clear, diikuti cuaca dengan sedikit kabut dan berawan, serta cuaca dengan user paling sedikit adalah di saat cuaca bersalju.")
