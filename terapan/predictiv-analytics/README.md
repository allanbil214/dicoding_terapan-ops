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

Dataset yang digunakan dalam proyek ini berisi informasi cuaca dan detail waktu yang berkaitan dengan jumlah sepeda yang disewa per jam di Seoul. Dataset ini diperoleh dari [Kaggle - Seoul Bike Sharing Dataset](https://www.kaggle.com/datasets/joebeachcapital/seoul-bike-sharing/data), yang berisi total 8760 baris data dengan 14 kolom sebelum dilakukan one-hot encoding. Setiap baris mewakili satu jam dalam setahun.

### Kondisi Dataset:
- **Jumlah Baris**: 8760
- **Jumlah Kolom**: 14 (sebelum one-hot encoding)
- **Missing Values**: Tidak ada missing value dalam dataset ini.
- **Duplikat Data**: Tidak ditemukan duplikasi data.
- **Outlier**: Ditemukan outlier pada beberapa variabel:
  - **Windspeed** dan **Solar Radiation** memiliki outlier yang terdeteksi pada visualisasi boxplot.
  - Variabel lain seperti **Rainfall**, **Snowfall**, **Seasons**, **Holiday**, dan **Functioning Day** tidak memiliki outlier yang terlihat, ditunjukkan oleh boxplot kosong atau penuh tanpa tail.
  - **Hour**, **Temperature**, **Humidity**, **Visibility**, dan **Dew Point Temperature** tidak menunjukkan adanya outlier.

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

1. **Statistik Deskriptif**  
   Dari perhitungan statistik dasar, terlihat bahwa rentang nilai pada beberapa variabel seperti suhu, kelembaban, dan kecepatan angin cukup bervariasi, yang mengindikasikan adanya fluktuasi cuaca yang signifikan sepanjang tahun. Selain itu, jumlah sepeda yang disewa per jam memiliki distribusi yang tidak merata, dengan beberapa jam tertentu menunjukkan permintaan yang lebih tinggi.

2. **Distribusi Sepeda yang Disewa**  
   Histogram distribusi jumlah sepeda yang disewa menunjukkan bahwa permintaan sewa sepeda cenderung terkonsentrasi di kisaran jumlah yang rendah hingga menengah. Permintaan yang sangat tinggi lebih jarang terjadi, yang menunjukkan pola penggunaan sepeda yang mungkin terkait dengan jam-jam tertentu atau kondisi cuaca tertentu.

3. **Korelasi antar Variabel**  
   Dari heatmap korelasi, terlihat bahwa suhu memiliki korelasi positif yang cukup kuat dengan jumlah sepeda yang disewa, sedangkan curah hujan dan salju menunjukkan korelasi negatif yang signifikan. Ini menandakan bahwa cuaca panas meningkatkan permintaan sewa, sementara curah hujan dan salju cenderung mengurangi jumlah sepeda yang disewa.

4. **Visualisasi berdasarkan Waktu dan Musim**  
   Boxplot menunjukkan bahwa permintaan sepeda bervariasi berdasarkan musim. Musim panas menunjukkan jumlah sepeda yang disewa lebih tinggi dibandingkan dengan musim lainnya. Scatterplot antara suhu dan jumlah sepeda juga memperkuat temuan bahwa permintaan cenderung meningkat seiring dengan kenaikan suhu.

5. **Tren Bulanan**  
   Dari tren bulanan, terlihat bahwa jumlah sewa sepeda mencapai puncaknya di bulan-bulan musim panas (Juli dan Agustus), sementara bulan-bulan musim dingin menunjukkan penurunan drastis dalam permintaan. Ini konsisten dengan pola cuaca yang lebih hangat meningkatkan aktivitas luar ruangan seperti bersepeda.

## Data Preparation

Dalam tahap ini, dilakukan beberapa langkah persiapan data untuk memastikan data siap digunakan dalam proses modeling. Langkah-langkah ini mencakup pembersihan data, pengubahan format, dan transformasi fitur yang diperlukan untuk meningkatkan kualitas data dalam rangka meningkatkan kinerja model.

### 1. Memeriksa dan Menangani Missing Values
Pada bagian **Data Understanding**, pengecekan terhadap **missing values** telah dilakukan dan ditemukan bahwa dataset ini **tidak mengandung missing values**. Oleh karena itu, tidak diperlukan penanganan lebih lanjut seperti imputasi atau penghapusan data. Hal ini memastikan bahwa data lengkap dan siap digunakan untuk proses pemodelan.

### 2. Memeriksa dan Menangani Duplikasi Data
Pada bagian **Data Understanding**, pengecekan terhadap **duplicated data** telah dilakukan dan ditemukan bahwa dataset ini **tidak mengandung duplicated data**. Oleh karena itu, tidak diperlukan penanganan lebih lanjut seperti penghapusan baris data duplikat. Hal ini memastikan bahwa setiap baris dalam dataset unik dan siap digunakan untuk proses pemodelan tanpa risiko adanya bias akibat duplikasi data.

### 3. Konversi dan Ekstraksi Tanggal
Kolom **Date** yang awalnya dalam format string dikonversi menjadi format tanggal menggunakan `pd.to_datetime()`. Setelah konversi, komponen-komponen waktu seperti **Year**, **Month**, dan **Day** diekstraksi dari kolom tanggal. Kolom **Date** asli kemudian dihapus karena informasi temporal yang relevan sudah terekstraksi.

**Alasan:** Komponen tanggal seperti tahun, bulan, dan hari dapat memengaruhi pola permintaan sepeda dan memberikan informasi penting yang tidak dapat ditangkap jika hanya menggunakan format string.

### 4. One-Hot Encoding
Variabel kategori seperti **Seasons** (musim), **Holiday** (hari libur), dan **Functioning Day** (hari kerja fungsional/non-fungsional) dikonversi menjadi format numerik menggunakan **one-hot encoding**. Teknik ini mengubah setiap kategori unik menjadi kolom biner terpisah, di mana 1 menunjukkan kehadiran kategori tersebut dan 0 sebaliknya.

**Alasan:** One-hot encoding penting agar model machine learning dapat memahami variabel kategori sebagai numerik tanpa memberikan bobot berlebihan pada urutan kategori.

### 5. Memilih Fitur dan Target
Setelah data diubah, dipilih beberapa fitur yang relevan untuk digunakan dalam model. Fitur yang dipilih mencakup variabel cuaca, waktu, dan variabel kategori yang telah diubah. Variabel target yang diprediksi adalah **Rented Bike Count** (jumlah sepeda yang disewa).

**Fitur yang dipilih:**
- Hour
- Temperature(°C)
- Humidity(%)
- Wind speed (m/s)
- Visibility (10m)
- Dew point temperature(°C)
- Solar Radiation (MJ/m2)
- Rainfall(mm)
- Snowfall (cm)
- Seasons (hasil one-hot encoding)
- Holiday (hasil one-hot encoding)
- Functioning Day (hasil one-hot encoding)

**Alasan:** Fitur-fitur ini dipilih berdasarkan hasil EDA yang menunjukkan korelasi mereka dengan jumlah sepeda yang disewa.

### 6. Split Data menjadi Train dan Test
Data dipisahkan menjadi **training set** dan **testing set** dengan rasio 80:20 menggunakan fungsi `train_test_split`. Ini dilakukan untuk memastikan bahwa model dapat diuji menggunakan data yang belum pernah dilihat sebelumnya, sehingga hasil evaluasi akan lebih akurat dan model tidak overfitting.

**Alasan:** Pembagian data sangat penting untuk mengukur kinerja model pada data yang tidak digunakan dalam pelatihan, memastikan generalisasi yang lebih baik.

### 7. Standarisasi Fitur
Fitur numerik seperti suhu, kelembaban, kecepatan angin, dan variabel cuaca lainnya distandarisasi menggunakan **StandardScaler**. Proses standarisasi ini memastikan bahwa setiap fitur memiliki skala yang sama, sehingga model tidak memberikan bobot lebih pada fitur dengan skala yang lebih besar, seperti suhu dan radiasi matahari.

**Alasan:** Standarisasi sangat penting dalam banyak model machine learning, terutama model seperti Random Forest, untuk menghindari dominasi fitur dengan rentang nilai lebih besar.

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
  ![MAE Formula](https://latex.codecogs.com/gif.image?\dpi{110}\text{MAE}=\frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|)

	Di mana:
	- $y_i$ adalah nilai aktual,
	- $\hat{y}_i$ adalah nilai prediksi,
	- $\bar{y}$ adalah rata-rata dari nilai aktual.
	
- **R2 Score (Koefisien Determinasi)**:
  R2 Score mengukur proporsi variansi dalam variabel dependen yang dapat dijelaskan oleh model. Nilai R2 berkisar antara 0 hingga 1, di mana nilai 1 menunjukkan bahwa model dapat menjelaskan semua variasi data. R2 Score yang lebih tinggi menunjukkan model yang lebih baik.

  Formula R2 Score dapat dinyatakan sebagai:

  $$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
  ![R-Squared Formula](https://latex.codecogs.com/gif.image?\dpi{110}$$R^2=1-\frac{\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}{\sum_{i=1}^{n}(y_i-\bar{y})^2}$$)
  
  di mana $bar{y}$ adalah rata-rata dari nilai aktual.

### 2. Hasil Proyek Berdasarkan Metrik Evaluasi

Setelah model dilatih dan diuji, hasil evaluasi menunjukkan:

- **Mean Absolute Error: 144.45**
- **R2 Score: 0.86**

**Interpretasi Hasil**:
- Dengan nilai **MAE sebesar 144.45**, ini berarti rata-rata kesalahan prediksi model adalah sekitar 144 sepeda. Ini menunjukkan bahwa dalam banyak kasus, model memprediksi jumlah sepeda yang disewa dengan akurasi yang cukup baik, meskipun masih terdapat kesalahan yang dapat diperbaiki.
  
- **R2 Score sebesar 0.86** menunjukkan bahwa model dapat menjelaskan sekitar 86% dari variansi dalam jumlah sepeda yang disewa berdasarkan fitur-fitur yang digunakan. Nilai ini menunjukkan bahwa model memiliki performa yang sangat baik dan dapat diandalkan untuk melakukan prediksi dalam konteks ini.

### 3. Dampak Model terhadap Business Understanding

#### Apakah model menjawab **problem statement**?
Untuk menjawab pertanyaan apakah **problem statements** telah berhasil dijawab, berikut adalah analisis berdasarkan hasil evaluasi model:

### 1. **Bagaimana kondisi cuaca memengaruhi permintaan sewa sepeda di Seoul?**

**Jawaban:**
Ya, **problem statement ini berhasil dijawab**. Hasil **exploratory data analysis (EDA)** menunjukkan bahwa variabel-variabel cuaca seperti suhu, kelembaban, kecepatan angin, dan radiasi matahari memiliki korelasi signifikan dengan jumlah sepeda yang disewa. Selain itu, model prediksi menggunakan Random Forest menunjukkan bahwa variabel-variabel cuaca memainkan peran penting dalam memprediksi permintaan sepeda. **R2 Score sebesar 0.86** menunjukkan bahwa model mampu menangkap sebagian besar variabilitas dalam data, termasuk dampak dari kondisi cuaca.

---

### 2. **Apakah waktu dalam sehari dan musim memengaruhi permintaan sepeda?**

**Jawaban:**
Ya, **problem statement ini juga berhasil dijawab**. Variabel waktu, seperti jam dalam sehari dan musim, jelas memengaruhi pola permintaan sepeda. Berdasarkan analisis visual dari data, terlihat adanya tren bahwa **jam sibuk di pagi dan sore hari** serta **musim panas** memiliki permintaan yang lebih tinggi untuk sepeda. Model prediksi dapat mengenali pola ini dengan baik, yang ditunjukkan dengan performa prediksi yang akurat pada data waktu dan musim.

---

### 3. **Bagaimana kita dapat memanfaatkan data historis untuk memprediksi permintaan sewa sepeda di masa mendatang?**

**Jawaban:**
Ya, **problem statement ini dijawab melalui pengembangan model prediksi**. Data historis yang mencakup berbagai fitur seperti cuaca, waktu, dan hari libur berhasil digunakan untuk melatih model Random Forest, yang kemudian dapat memprediksi permintaan sepeda dengan akurasi yang memadai. Dengan **MAE sebesar 144.45**, model ini menunjukkan bahwa data historis dapat dimanfaatkan untuk membuat prediksi yang cukup akurat terkait jumlah sepeda yang akan disewa di masa mendatang.

---

Dengan demikian, semua **problem statements** telah berhasil dijawab oleh model yang dikembangkan. Hasilnya mendukung pemahaman terhadap faktor-faktor yang memengaruhi permintaan sepeda, serta kemampuan memprediksi pola permintaan di masa mendatang dengan tingkat kesalahan yang rendah.

#### Apakah model berhasil mencapai **goals** yang diharapkan?
Secara keseluruhan, model ini berhasil mencapai goals yang ditetapkan, yaitu:

1. **Memahami pengaruh variabel cuaca terhadap permintaan sepeda**:  
   Korelasi antara variabel cuaca seperti suhu dan kelembaban dengan jumlah sepeda yang disewa terlihat jelas dalam hasil EDA, dan model ini mampu menangkap pola tersebut dengan baik.

2. **Mengidentifikasi pola permintaan berdasarkan waktu dan musim**:  
   Model juga berhasil memanfaatkan variabel waktu, seperti jam dalam sehari dan musim, yang terbukti relevan dalam memprediksi jumlah sepeda yang disewa. Variasi permintaan yang terjadi pada musim panas dan jam sibuk dapat diprediksi dengan akurasi yang baik.

3. **Mengembangkan model prediksi yang akurat**:  
   Dengan nilai MAE sebesar 144.45, model ini menunjukkan **rata-rata kesalahan prediksi yang cukup rendah**, menjadikan prediksinya berguna untuk membantu perencanaan operasional sistem _bike sharing_ di Seoul.

#### Apakah solusi statement yang direncanakan berdampak?
Solusi yang diusulkan, yaitu menggunakan algoritma **Random Forest** untuk memprediksi permintaan sepeda, telah terbukti efektif. Model ini menunjukkan performa yang baik dalam mengatasi masalah prediksi, dengan penanganan yang cukup baik terhadap fitur-fitur yang digunakan. Metrik evaluasi menunjukkan bahwa model ini dapat digunakan oleh pengelola sistem _bike sharing_ untuk memprediksi permintaan sepeda dengan cukup akurat, sehingga dapat mendukung keputusan operasional seperti distribusi sepeda di berbagai stasiun.

### Kesimpulan

Metrik evaluasi yang digunakan menunjukkan bahwa model Random Forest Regressor yang dibangun cukup efektif dalam memprediksi jumlah sepeda yang disewa di Seoul. Dengan MAE yang relatif rendah dan R2 Score yang tinggi, model ini dapat memberikan wawasan yang bermanfaat untuk perencanaan dan pengelolaan sistem berbagi sepeda di kota tersebut.

**---Ini adalah bagian akhir laporan---**
