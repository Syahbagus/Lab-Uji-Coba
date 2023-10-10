from faker import Faker
from faker_airtravel import AirTravelProvider
import random
import pandas as pd

# Inisialisasi objek Faker
fake = Faker()
fake.add_provider(AirTravelProvider)

# Data untuk Tabel DEPARTEMEN
departemen_data = []
for _ in range(20):
    departemen_data.append((
        fake.unique.random_int(min=1, max=9999),
        fake.job(),
        fake.unique.city(),
        fake.random_int(min=10, max=100)
    ))

# Data untuk Tabel MASKAPAI
maskapai_data = []
for _ in range(20):
    maskapai_data.append((
        fake.unique.random_int(min=1000, max=9999),
        fake.airline(),
        fake.random_int(min=10000000, max=99999999),
        fake.company_suffix()
    ))

# Data untuk Tabel PEGAWAI
pegawai_data = []
for _ in range(20):
    pegawai_data.append((
        fake.unique.random_int(min=1000, max=9999),
        fake.name(),
        fake.job(),
        fake.date_time_between(
            start_date='-5y', end_date='now').strftime('%Y-%m-%d %H:%M:%S'),
        fake.random_int(min=4000000, max=9000000)
    ))

# Data untuk Tabel PESAWAT
pesawat_data = []
for _ in range(20):
    pesawat_data.append((
        fake.unique.random_int(min=1000, max=9999),
        fake.airline(),
        fake.random_int(min=1990, max=2023),
        random.choice(['Operasional', 'Perbaikan', 'Tidak Aktif']),
        fake.random_int(min=100, max=500),
        fake.unique.company()
    ))

# Membuat DataFrames Pandas
df_departemen = pd.DataFrame(departemen_data, columns=[
                             'IDDEPARTEMEN', 'NAMADEPARTEMEN', 'LOKASIDEPARTEMEN', 'JUMLAHPEKERJA'])
df_maskapai = pd.DataFrame(maskapai_data, columns=[
                           'KODEMASKAPAI', 'NAMAMASKAPAI', 'KONTAKMASKAPAI', 'BASISOPERASI'])
df_pegawai = pd.DataFrame(pegawai_data, columns=[
                          'NOMORPEGAWAI', 'NAMA', 'JABATAN', 'JADWALKERJA', 'GAJI'])
df_pesawat = pd.DataFrame(pesawat_data, columns=[
                          'NOMORREGISTASI', 'MASKAPAIOPERASIONAL', 'TAHUNPEMBUATAN', 'STATUSOPERASIONAL', 'KAPASITASPENUMPANG', 'TIPEPESAWAT'])

# Tampilkan DataFrames
print("Data untuk Tabel DEPARTEMEN:")
print(df_departemen)

print("\nData untuk Tabel MASKAPAI:")
print(df_maskapai)

print("\nData untuk Tabel PEGAWAI:")
print(df_pegawai)

print("\nData untuk Tabel PESAWAT:")
print(df_pesawat)
