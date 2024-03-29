#### Cara Menjalankan Dashboard

1. Clone Repository

```git
git clone https://github.com/CakPon/bike-sharing.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Jalankan dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

#### Column Description

- instant: Indeks catatan.
- dteday: Tanggal.
- season: Musim (1: musim semi, 2: musim panas, 3: musim gugur, 4: musim dingin).
- yr: Tahun (0: 2011, 1: 2012).
- mnth: Bulan (1 sampai 12).
- hr: Jam (0 sampai 23) - hanya tersedia di hour.csv.
- holiday: Apakah hari tersebut libur atau tidak (diambil dari http://dchr.dc.gov/page/holiday-schedule).
- weekday: Hari dalam minggu.
- workingday: Jika hari bukan akhir pekan atau libur maka bernilai 1, sebaliknya 0.
- weathersit:
  - 1: Cerah, Sedikit berawan, Sebagian berawan, Sebagian berawan.
  - 2: Kabut + Berawan, Kabut + Awan pecah, Kabut + Sedikit awan, Kabut.
  - 3: Salju ringan, Hujan ringan + Badai petir + Awan berpencar, Hujan ringan + Awan berpencar.
  - 4: Hujan lebat + Butiran es + Badai petir + Kabut, Salju + Kabut.
- temp: Suhu dinormalisasi dalam Celsius. Nilainya dibagi dengan 41 (maks).
- atemp: Suhu terasa dinormalisasi dalam Celsius. Nilainya dibagi dengan 50 (maks).
- hum: Kelembaban dinormalisasi. Nilainya dibagi dengan 100 (maks).
- windspeed: Kecepatan angin dinormalisasi. Nilainya dibagi dengan 67 (maks).
- casual: Jumlah pengguna kasual.
- registered: Jumlah pengguna terdaftar.
- cnt: Jumlah total sepeda yang disewakan termasuk pengguna kasual dan terdaftar.