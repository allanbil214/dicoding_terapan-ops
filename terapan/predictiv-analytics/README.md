# Laporan Proyek Machine Learning - Allan Bil Faqih

## Domain Proyek

## Latar Belakang

_Bike_ _Sharing_ merupakan salah satu solusi transportasi perkotaan yang banyak diminati, khususnya di kota-kota besar seperti Seoul, Korea Selatan. Program _Bike_ _Sharing_ ini tidak hanya membantu mengurangi kemacetan lalu lintas, tetapi juga mendorong gaya hidup sehat dan mengurangi emisi karbon. Namun, pengelolaan sistem _Bike_ _Sharing_ memerlukan perencanaan yang baik agar penyediaan sepeda yang cukup di setiap lokasi dapat memenuhi permintaan pengguna secara efektif.

Seiring dengan perkembangan teknologi, prediksi permintaan pengguna sepeda berdasarkan faktor-faktor seperti kondisi cuaca, waktu dalam sehari, serta musim dapat memberikan wawasan penting untuk mengoptimalkan operasional sistem _Bike_ _Sharing_ tersebut. Dalam konteks ini, penggunaan _Predictive_ _Analytics_ yang didukung oleh algoritma _machine_ _learning_ dapat membantu membuat keputusan yang lebih cerdas dan berbasis data.

Dengan dataset _Bike_ _Sharing_ Seoul ini, yang mencakup informasi tentang jumlah sepeda yang disewa setiap jam, kondisi cuaca, serta variabel waktu, proyek ini bertujuan untuk membangun model prediksi yang dapat memperkirakan jumlah sepeda yang akan disewa di masa depan. Prediksi ini diharapkan dapat membantu pengelola sistem _Bike_ _Sharing_ dalam memastikan ketersediaan sepeda yang memadai di seluruh stasiun selama periode permintaan tinggi, sehingga meningkatkan efisiensi operasional dan kepuasan pengguna.

## Business Understanding

Dalam proyek ini, tujuan utamanya adalah memprediksi jumlah sepeda yang akan disewa di Seoul berdasarkan berbagai faktor seperti waktu, cuaca, dan musim. Pemahaman yang mendalam tentang permasalahan ini sangat penting agar sistem berbagi sepeda dapat dikelola dengan efisien dan memastikan ketersediaan sepeda yang sesuai dengan permintaan pengguna.

### Problem Statements

1. **Bagaimana kondisi cuaca memengaruhi permintaan sewa sepeda di Seoul?**  

2. **Apakah waktu dalam sehari dan musim memengaruhi permintaan sepeda?**  

3. **Bagaimana kita dapat memanfaatkan data historis untuk memprediksi permintaan sewa sepeda di masa mendatang?**  

### Goals

1. **Memahami pengaruh variabel cuaca terhadap permintaan sepeda.**  

2. **Mengidentifikasi pola permintaan berdasarkan waktu dan musim.**  

3. **Mengembangkan model prediksi yang akurat untuk memperkirakan jumlah sepeda yang disewa.**  

### Solution Statements

1. **Menggunakan Random Forest sebagai algoritma utama.**  

2. **Mengukur kinerja model dengan evaluasi berbasis MAE dan R2 Score.**  

## Data Understanding

Dataset yang digunakan dalam proyek ini berisi informasi cuaca dan detail terkait waktu yang berhubungan dengan jumlah sepeda yang disewa setiap jam di Seoul. Dataset ini diperoleh dari [Kaggle - Seoul Bike Sharing Dataset](https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing/data), yang berisi total 8760 baris data. Setiap baris mewakili satu jam dalam setahun.

Dataset ini terdiri dari berbagai variabel yang memberikan gambaran lengkap tentang kondisi cuaca dan faktor temporal yang dapat memengaruhi permintaan sewa sepeda.

### Variabel-variabel pada dataset Seoul Bike Sharing adalah sebagai berikut:

- **Date**: Tanggal dalam format year-month-day.
- **Rented Bike Count**: Jumlah sepeda yang disewa per jam.
- **Hour**: Jam dalam sehari (0-23).
- **Temperature(°C)**: Suhu dalam derajat Celsius.
- **Humidity(%)**: Kelembaban udara dalam persen.
- **Wind speed (m/s)**: Kecepatan angin dalam meter per detik.
- **Visibility (10m)**: Jarak pandang dalam satuan 10 meter.
- **Dew point temperature(°C)**: Titik embun dalam derajat Celsius.
- **Solar Radiation (MJ/m2)**: Radiasi matahari dalam megajoule per meter persegi.
- **Rainfall(mm)**: Curah hujan dalam milimeter.
- **Snowfall (cm)**: Curah salju dalam sentimeter.
- **Seasons**: Musim (Winter, Spring, Summer, Autumn).
- **Holiday**: Menyatakan apakah hari tersebut adalah hari libur atau bukan (Holiday/No Holiday).
- **Functioning Day**: Menyatakan apakah hari tersebut adalah hari kerja fungsional atau non-fungsional (Fun/NoFun).

### Exploratory Data Analysis (EDA)

Untuk memahami pola dan hubungan antar variabel dalam data, dilakukan beberapa tahap analisis eksploratif (EDA):

1. **Statistik Deskriptif**  
   Dilakukan perhitungan statistik dasar (mean, median, minimum, maksimum, dll.) untuk semua variabel dalam dataset untuk mendapatkan gambaran umum mengenai data.

2. **Distribusi Sepeda yang Disewa**  
   Visualisasi distribusi dari jumlah sepeda yang disewa per jam menggunakan histogram untuk melihat pola frekuensi dari permintaan sepeda.

3. **Korelasi antar variabel**  
   Heatmap korelasi digunakan untuk menganalisis hubungan antara variabel cuaca dan jumlah sepeda yang disewa. Ini membantu mengidentifikasi variabel mana yang memiliki hubungan paling kuat dengan permintaan sepeda.

4. **Visualisasi berdasarkan waktu dan musim**  
   Boxplot digunakan untuk memvisualisasikan bagaimana permintaan sepeda bervariasi menurut musim, sementara scatterplot menunjukkan hubungan antara suhu dan jumlah sepeda yang disewa.

5. **Tren bulanan**  
   Tren bulanan rata-rata sewa sepeda diperiksa menggunakan line plot, yang membantu memahami fluktuasi permintaan sepanjang tahun.

## Data Preparation

Dalam tahap ini, dilakukan beberapa langkah persiapan data untuk memastikan data siap digunakan dalam proses modeling. Langkah-langkah ini mencakup pembersihan data, pengubahan format, dan transformasi fitur yang diperlukan untuk meningkatkan kualitas data dalam rangka meningkatkan kinerja model.

### 1. Memeriksa Missing Values
Tahap pertama dalam persiapan data adalah memeriksa apakah ada data yang hilang (missing values) dalam dataset. Dengan menggunakan fungsi `.isnull().sum()`, dapat dipastikan bahwa tidak ada missing values dalam dataset. Ini memastikan bahwa data lengkap dan siap digunakan tanpa perlu melakukan imputasi atau pembuangan data.

### 2. Konversi dan Ekstraksi Tanggal
Kolom **Date** yang awalnya dalam format string dikonversi menjadi format tanggal dengan fungsi `pd.to_datetime()`. Setelah itu, komponen-komponen waktu seperti **Year**, **Month**, dan **Day** diekstraksi dari kolom tanggal untuk memberikan informasi temporal yang lebih kaya kepada model. Kolom **Date** asli kemudian dihapus karena informasi waktu yang relevan telah diekstrak.

Alasan: Ekstraksi komponen tanggal diperlukan karena tahun, bulan, dan hari dapat mempengaruhi pola permintaan sepeda yang tidak ditangkap dalam format string.

### 3. One-Hot Encoding
Variabel kategori seperti **Seasons** (musim), **Holiday** (hari libur), dan **Functioning Day** (hari kerja fungsional atau non-fungsional) dikonversi menggunakan teknik **one-hot encoding**. Ini dilakukan dengan memecah setiap kategori menjadi beberapa kolom biner untuk setiap kategori unik. Teknik ini penting untuk memastikan bahwa model machine learning dapat memahami variabel kategori sebagai numerik tanpa memberikan bobot berlebihan pada urutan kategori tertentu.

Alasan: One-hot encoding penting untuk model seperti Random Forest yang tidak dapat langsung menangani variabel kategori.

### 4. Memilih Fitur dan Target
Setelah data diubah, dipilih beberapa fitur yang relevan untuk digunakan dalam model. Fitur yang dipilih mencakup variabel cuaca, waktu, dan variabel kategori yang sudah diubah. Variabel target yang diprediksi adalah **Rented Bike Count** (jumlah sepeda yang disewa).

Fitur yang dipilih:
- Hour
- Temperature(°C)
- Humidity(%)
- Wind speed (m/s)
- Visibility (10m)
- Dew point temperature(°C)
- Solar Radiation (MJ/m2)
- Rainfall(mm)
- Snowfall (cm)
- Seasons_Spring, Seasons_Summer, Seasons_Autumn (hasil one-hot encoding)
- Holiday_No Holiday
- Functioning Day_Yes

Alasan: Fitur-fitur ini dipilih berdasarkan korelasi mereka dengan jumlah sepeda yang disewa, yang diperoleh dari hasil EDA.

### 5. Split Data menjadi Train dan Test
Data dipisahkan menjadi data **training** dan **testing** dengan rasio 80:20. Hal ini dilakukan untuk memastikan bahwa model dapat diuji dengan data yang belum pernah dilihat sebelumnya, sehingga hasil evaluasi akan lebih realistis dan tidak overfitting.

Alasan: Membagi data adalah langkah penting dalam pengembangan model untuk menilai kinerja model pada data yang tidak digunakan dalam proses pelatihan.

### 6. Standarisasi Fitur
Beberapa fitur numerik seperti suhu, kelembaban, kecepatan angin, dan variabel cuaca lainnya distandarisasi menggunakan **StandardScaler**. Ini dilakukan agar semua fitur berada pada skala yang sama, terutama karena fitur seperti suhu dan radiasi matahari memiliki rentang nilai yang berbeda-beda. Standarisasi membantu meningkatkan kinerja model, terutama pada algoritma seperti Random Forest yang sensitif terhadap perbedaan skala antar fitur.

Alasan: Standarisasi diperlukan untuk memastikan bahwa model tidak memberikan bobot lebih pada fitur dengan skala yang lebih besar secara tidak proporsional.

## Modeling

Tahap **modeling** bertujuan untuk membangun model machine learning yang dapat memprediksi jumlah sepeda yang disewa berdasarkan variabel-variabel cuaca dan waktu. Pada proyek ini, digunakan algoritma **Random Forest Regressor**, yang merupakan model ensemble berbasis pohon keputusan dan sering digunakan untuk masalah regresi karena kemampuannya menangani data dengan berbagai jenis fitur.

### 1. Algoritma yang Digunakan: Random Forest Regressor

Random Forest adalah algoritma yang membangun banyak pohon keputusan secara acak dan menggabungkan hasilnya untuk membuat prediksi yang lebih akurat dan stabil. Dalam proyek ini, digunakan **RandomForestRegressor** dari library Scikit-learn. Algoritma ini dipilih karena keandalannya dalam menangani dataset yang memiliki banyak fitur dan tidak terlalu sensitif terhadap outlier atau noise pada data.

**Parameter yang digunakan dalam Random Forest**:
- **n_estimators=100**: Menentukan jumlah pohon yang akan dibuat oleh model. Semakin banyak pohon, semakin baik prediksi yang dihasilkan, namun juga membutuhkan lebih banyak waktu komputasi.
- **random_state=42**: Parameter ini memastikan bahwa hasil yang didapat akan konsisten setiap kali model dijalankan dengan dataset yang sama, karena proses randomisasi dikendalikan oleh seed yang tetap.

### 2. Proses Pelatihan Model

Setelah data dibagi menjadi data training dan testing, fitur numerik distandarisasi agar memiliki skala yang seragam. Fitur yang telah distandarisasi kemudian digunakan untuk melatih model Random Forest. Proses pelatihan dilakukan dengan memanggil metode `.fit()` dari RandomForestRegressor, yang akan membuat banyak pohon keputusan berdasarkan fitur-fitur yang telah disediakan.

```python
# Melatih model Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
```

### 3. Alasan Pemilihan Model

Random Forest dipilih karena keunggulannya dalam menangani dataset yang besar dan kompleks. Model ini juga dapat secara otomatis menangani interaksi antar fitur dan cukup fleksibel dalam menangani variabel dengan skala yang berbeda, meskipun pada kasus ini kita sudah melakukan standarisasi fitur. Selain itu, Random Forest memiliki kemampuan untuk mengurangi risiko overfitting melalui mekanisme averaging prediksi dari beberapa pohon.

### 4. Prediksi dengan Model

Setelah model dilatih, dilakukan prediksi terhadap data testing menggunakan fitur yang sudah distandarisasi. Proses prediksi dilakukan dengan metode `.predict()`, dan hasil prediksi ini akan dibandingkan dengan nilai asli untuk mengukur kinerja model.

```python
# Melakukan prediksi pada data test
y_pred = model.predict(X_test_scaled)
```

### 5. Model yang Digunakan dan Perbaikan

Dalam proyek ini, hanya satu model yang digunakan, yaitu **Random Forest Regressor**. Tidak ada penerapan hyperparameter tuning atau penggunaan algoritma lain dalam upaya meningkatkan performa. Random Forest dipilih karena kinerjanya yang sudah cukup baik dalam mengatasi masalah regresi dengan data seperti ini, dan model tersebut memberikan hasil yang memadai untuk skala proyek ini.

Jika diperlukan peningkatan lebih lanjut pada proyek di masa mendatang, proses **hyperparameter tuning** seperti mencari nilai optimal untuk `n_estimators` atau `max_depth` dapat dilakukan untuk lebih mengoptimalkan kinerja model.

## Evaluation

Pada tahap evaluasi ini, model yang dibangun untuk memprediksi jumlah sepeda yang disewa dievaluasi menggunakan dua metrik utama: **Mean Absolute Error (MAE)** dan **R2 Score**. Kedua metrik ini dipilih karena relevansinya dalam konteks masalah regresi yang dihadapi.

### 1. Metrik yang Digunakan

- **Mean Absolute Error (MAE)**:
  MAE mengukur rata-rata kesalahan absolut antara nilai yang diprediksi oleh model dan nilai sebenarnya. Metrik ini memberikan gambaran seberapa jauh prediksi model dari nilai aktual, dalam hal satuan yang sama dengan variabel target (jumlah sepeda yang disewa). Semakin rendah nilai MAE, semakin baik performa model.

  Formula MAE dapat dinyatakan sebagai:
  \[
  \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
  \]
  di mana \(y_i\) adalah nilai aktual, \(\hat{y}_i\) adalah nilai prediksi, dan \(n\) adalah jumlah total observasi.

- **R2 Score (Koefisien Determinasi)**:
  R2 Score mengukur proporsi variansi dalam variabel dependen yang dapat dijelaskan oleh model. Nilai R2 berkisar antara 0 hingga 1, di mana nilai 1 menunjukkan bahwa model dapat menjelaskan semua variasi data. R2 Score yang lebih tinggi menunjukkan model yang lebih baik.

  Formula R2 Score dapat dinyatakan sebagai:
  \[
  R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}
  \]
  di mana \(\bar{y}\) adalah rata-rata dari nilai aktual.

### 2. Hasil Proyek Berdasarkan Metrik Evaluasi

Setelah model dilatih dan diuji, hasil evaluasi menunjukkan:

- **Mean Absolute Error: 144.45**
- **R2 Score: 0.86**

**Interpretasi Hasil**:
- Dengan nilai **MAE sebesar 144.45**, ini berarti rata-rata kesalahan prediksi model adalah sekitar 144 sepeda. Ini menunjukkan bahwa dalam banyak kasus, model memprediksi jumlah sepeda yang disewa dengan akurasi yang cukup baik, meskipun masih terdapat kesalahan yang dapat diperbaiki.
  
- **R2 Score sebesar 0.86** menunjukkan bahwa model dapat menjelaskan sekitar 86% dari variansi dalam jumlah sepeda yang disewa berdasarkan fitur-fitur yang digunakan. Nilai ini menunjukkan bahwa model memiliki performa yang sangat baik dan dapat diandalkan untuk melakukan prediksi dalam konteks ini.

### Kesimpulan

Metrik evaluasi yang digunakan menunjukkan bahwa model Random Forest Regressor yang dibangun cukup efektif dalam memprediksi jumlah sepeda yang disewa di Seoul. Dengan MAE yang relatif rendah dan R2 Score yang tinggi, model ini dapat memberikan wawasan yang bermanfaat untuk perencanaan dan pengelolaan sistem berbagi sepeda di kota tersebut.

**---Ini adalah bagian akhir laporan---**