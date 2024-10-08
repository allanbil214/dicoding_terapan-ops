# -*- coding: utf-8 -*-
"""dicoding_predictive-analytics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gGbqDL0gQB3mVCzUi_-1XudnZ6YAKCS7

# Proyek Pertama : Predictive Analytics
- **Nama:** Allan Bil Faqih
- **ID Dicoding:** allanbil214

Sauce: https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing/data



Data Description:
Dataset ini berisi informasi cuaca (Suhu, Kelembaban, Kecepatan Angin, Jarak Pandang, Titik Embun, Radiasi Matahari, Curah Salju, Curah Hujan), jumlah sepeda yang disewa per jam, dan informasi tanggal.

Attribute Information:

    Date : year-month-day
    Rented Bike Count - Jumlah sepeda yang disewa setiap jamnya
    Hour - Jam dalam sehari
    Temperature - Suhu dalam Celcius
    Humidity - %
    Windspeed - m/s
    Visibility - 10m
    Dew point temperature - Celsius
    Solar radiation - MJ/m2
    Rainfall - mm
    Snowfall - cm
    Seasons - Winter, Spring, Summer, Autumn
    Holiday - Holiday/No holiday
    Functional Day - NoFunc(Jam Non Fungsional), Fun(Jam fungsional)

## Import Semua Packages/Library yang Digunakan

Kode berikut digunakan untuk mengimpor _library_ yang diperlukan untuk analisis data dan _predictive model_, termasuk pengolahan data dengan pandas dan numpy, visualisasi dengan matplotlib dan seaborn, serta pemodelan regresi menggunakan RandomForestRegressor dari scikit-learn.
"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

"""# 1. Data Loading

Kode berikut memuat data dari file CSV yang disimpan di GitHub ke dalam DataFrame menggunakan pandas, menyimpan salinan aslinya, dan menampilkan beberapa baris pertama dari data tersebut untuk pemeriksaan awal.
"""

# Load data csv dari github
df = pd.read_csv("https://raw.githubusercontent.com/allanbil214/dicoding_terapan-ops/main/terapan/predictiv-analytics/dataset/SeoulBikeData.csv", encoding='unicode_escape')
ori_df = df

# Menampilkan beberapa Row pertama
df.head()

"""Menampilkan semua kolom yang ada pada dataframe sebagai proses pemeriksaan awal."""

# Menampilkan semua kolom
print(df.columns)

"""# 2. Data Preprocessing

Menampilkan semua tipe data kolom untuk memastikan tipe data kolom tersebut.
"""

# Menampilkan semua tipe data kolom
df.info()

"""Kode berikut digunakan mengecek missing values pada setiap kolom."""

# Mengecek missing values
print(df.isnull().sum())

"""Menampilkan jumlah baris yang duplikat serta baris-baris yang terdeteksi sebagai duplikat"""

# Mengecek jumlah baris duplikat
duplikat = df.duplicated().sum()
print(f'Jumlah baris duplikat: {duplikat}')

# Menampilkan baris duplikat
duplikat_baris = df[df.duplicated()]
print(duplikat_baris)

"""Kode berikut digunakan untuk mengonversi kolom 'Date' menjadi format tanggal valid, kemudian mengekstrak tahun, bulan, dan hari ke dalam kolom terpisah, sebelum akhirnya menghapus kolom 'Date' yang sudah tidak diperlukan."""

# Mengkonversi dan mengekstrak tanggal
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Membuang kolom Date, karena sudah diekstrak
df.drop(columns="Date", axis =1,inplace =True)

"""Lalu kode dibawah ini digunakan untuk mengonversi kolom kategorikal 'Seasons', 'Holiday', dan 'Functioning Day' menjadi representasi numerik menggunakan teknik one-hot encoding, sehingga setiap kategori diwakili oleh kolom biner terpisah."""

# Mengencode ketigal kolom tersebut
df = pd.get_dummies(df, columns=['Seasons', 'Holiday', 'Functioning Day'], drop_first=False)

"""Kode di dibawah berfungsi untuk menampilkan beberapa baris pertama dari DataFrame, mencetak daftar nama kolom yang ada, serta memberikan informasi ringkas tentang tipe data dan jumlah entri pada setiap kolom dalam DataFrame, untuk memastikan hasil dari data preprocessing."""

df.head()

print(df.columns)

df.info()

"""# 3. Melakukan EDA

Kode berikut menghasilkan statistik deskriptif dasar untuk DataFrame, termasuk nilai rata-rata, median, standar deviasi, serta nilai minimum dan maksimum untuk setiap kolom numerik, yang berguna untuk memahami distribusi data.
"""

# Basic statistics
print(df.describe())

"""Membuat visualisasi histogram untuk distribusi jumlah sepeda yang disewa, menggunakan seaborn untuk menampilkan frekuensi dan kurva distribusi (KDE) pada data."""

# Distribusi Rental Sepeda
plt.figure(figsize=(10, 5))
sns.histplot(df['Rented Bike Count'], bins=30, kde=True)
plt.title('Distribution of Rented Bike Count')
plt.xlabel('Rented Bike Count')
plt.ylabel('Frequency')
plt.show()

"""Membuat heatmap untuk menunjukkan matriks korelasi antara fitur-fitur dalam DataFrame, dengan anotasi untuk setiap nilai korelasi yang membantu mengidentifikasi hubungan antar variabel secara visual."""

# Korelasi heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

"""Kode ini digunakan untuk membuat pairplot menggunakan seaborn untuk memvisualisasikan hubungan antar fitur yang dipilih, yaitu 'Rented Bike Count', 'Temperature(°C)', 'Humidity(%)', dan 'Wind speed (m/s)'."""

# Pairplot untuk memvisualkan hubungan antar fitur
sns.pairplot(df, vars=['Rented Bike Count', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)'])
plt.suptitle('Pairplot of Selected Features', y=1.02)
plt.show()

"""Kode tersebut bertujuan untuk memvisualisasikan outlier dari variabel numerik dalam dataframe `df` dengan menghasilkan boxplot horizontal untuk setiap kolom yang terdaftar dalam `numerical_var`, sehingga memudahkan analisis distribusi dan identifikasi nilai-nilai ekstrim."""

numerical_var = ['Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)', 'Dew point temperature(°C)',
            'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Seasons_Spring', 'Seasons_Summer',
            'Seasons_Autumn', 'Holiday_No Holiday', 'Functioning Day_Yes']

plt.figure(figsize = (12,50))
counter = 1
for var in numerical_var:
    if counter < 20:
        plt.subplot(14,1,counter)
        sns.boxplot(x = var, orient = "h", data =df)
        plt.title(var)
    counter += 1
plt.tight_layout()

"""Kode ini menghasilkan boxplot untuk jumlah sepeda yang disewa berdasarkan setiap musim (Musim Semi, Musim Panas, Musim Gugur, dan Musim Dingin), yang membantu mengidentifikasi distribusi dan outlier dari data 'Rented Bike Count' di setiap musim secara terpisah."""

# Boxplot untuk setiap musim
plt.figure(figsize=(10, 5))
sns.boxplot(x='Seasons_Spring', y='Rented Bike Count', data=df)
plt.title('Bike Rentals by Season (Spring)')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x='Seasons_Summer', y='Rented Bike Count', data=df)
plt.title('Bike Rentals by Season (Summer)')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x='Seasons_Autumn', y='Rented Bike Count', data=df)
plt.title('Bike Rentals by Season (Autumn)')
plt.show()

plt.figure(figsize=(10, 5))
sns.boxplot(x='Seasons_Winter', y='Rented Bike Count', data=df)
plt.title('Bike Rentals by Season (Winter)')
plt.show()

"""Kode ini membuat boxplot untuk membandingkan jumlah sepeda yang disewa antara hari libur dan hari non-libur, yang membantu mengidentifikasi perbedaan distribusi dan outlier dalam data 'Rented Bike Count' berdasarkan status hari tersebut."""

plt.figure(figsize=(10, 5))
sns.boxplot(x='Holiday_No Holiday', y='Rented Bike Count', data=df)
plt.title('Bike Rentals on Holidays vs. Non-Holidays')
plt.show()

"""Kode ini membuat scatter plot untuk menunjukkan hubungan antara suhu (dalam derajat Celsius) dan jumlah sepeda yang disewa, yang membantu dalam mengidentifikasi pola atau tren dalam data 'Rented Bike Count' seiring perubahan temperatur."""

# Plot rental vs temperatur
plt.figure(figsize=(10, 5))
sns.scatterplot(x='Temperature(°C)', y='Rented Bike Count', data=df)
plt.title('Bike Rentals vs Temperature')
plt.show()

"""Kode ini digunakan untuk menganalisis tren sewa sepeda dengan menghitung rata-rata jumlah sepeda yang disewa per bulan untuk setiap tahun, kemudian memvisualisasikannya dalam bentuk line plot untuk menunjukkan perbandingan tren bulanan sewa sepeda dari tahun ke tahun."""

# Menganalisa tren rental
monthly_rentals = df.groupby(['Year', 'Month'])['Rented Bike Count'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_rentals, x='Month', y='Rented Bike Count', hue='Year', marker='o')
plt.title('Monthly Average Bike Rentals Over Years')
plt.xlabel('Month')
plt.ylabel('Average Rented Bike Count')
plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.show()

"""# 4. Menentukan Fitur dan Target

Memilih fitur-fitur yang akan digunakan untuk prediksi jumlah sepeda yang disewa, serta menetapkan 'Rented Bike Count' sebagai variabel target yang akan diprediksi dalam model analisis atau pembelajaran mesin.
"""

# Memilih fitur untuk prediksi
features = ['Hour', 'Temperature(°C)', 'Humidity(%)', 'Wind speed (m/s)', 'Visibility (10m)', 'Dew point temperature(°C)',
            'Solar Radiation (MJ/m2)', 'Rainfall(mm)', 'Snowfall (cm)', 'Seasons_Spring', 'Seasons_Summer', 'Seasons_Winter',
            'Seasons_Autumn', 'Holiday_No Holiday', 'Functioning Day_Yes']

# Variabel target
target = 'Rented Bike Count'

"""# 5. Memisah Data menjadi Train dan Test

Memisahkan data menjadi fitur (X) dan target (y), lalu membagi dataset menjadi set pelatihan dan set pengujian dengan rasio 80:20 menggunakan `train_test_split`, sehingga hasil pembagian dapat direproduksi dengan mengatur `random_state` ke 42.
"""

X = df[features]
y = df[target]

# Memisah 8:2 Train dan Test, dengan random_state 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# 6. Standarisasi fitur

Menstandarisasi fitur dengan StandardScaler mengubah data sehingga setiap fitur memiliki rata-rata 0 dan deviasi standar 1, dilakukan pada data pelatihan dan kemudian diterapkan pada data pengujian.
"""

# Menstandarisasi fitur
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""# 7. Membuat model dengan Random Forest

Modeling menggunakan RandomForestRegressor dengan 100 estimator untuk memprediksi target y_train berdasarkan fitur yang telah distandarisasi pada data pelatihan.
"""

# 7. Modeling dengan Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

"""# 8. Melakukan Prediksi

Membuat prediksi terhadap data pengujian dengan menggunakan model Random Forest yang telah dilatih, menghasilkan output y_pred berdasarkan fitur yang distandarisasi.
"""

# 8. Membuat prediksi
y_pred = model.predict(X_test_scaled)

"""# 9. Melakukan Evaluasi

Mengevaluasi model dengan menghitung Mean Absolute Error (MAE) dan R² Score untuk mengukur akurasi prediksi y_pred terhadap data pengujian y_test, kemudian mencetak hasilnya.
"""

# 9. Mengevaluasi Model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae}")
print(f"R2 Score: {r2}")

"""Memvisualisasikan perbandingan antara nilai asli (`y_test`) dan nilai prediksi (`y_pred`) untuk penyewaan sepeda, dengan grafik yang menampilkan kedua kurva dan legenda untuk memudahkan interpretasi."""

# Memvisualkan nilai prediksi vs asli
plt.figure(figsize=(10,5))
plt.plot(y_test.values, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.legend()
plt.title('Actual vs Predicted Bike Rentals')
plt.show()