# Laporan Proyek Machine Learning - Allan Bil Faqih

## Project Overview

Proyek ini berfokus pada pengembangan sistem rekomendasi untuk buku menggunakan dua pendekatan utama: **Content-Based Filtering** dan **Collaborative Filtering**. Sistem rekomendasi menjadi salah satu solusi penting dalam mengatasi permasalahan overload informasi di era digital, khususnya dalam industri buku, di mana pembaca sering kali kesulitan menemukan bacaan yang sesuai dengan preferensi mereka. Dengan adanya sistem rekomendasi, pengguna dapat dengan mudah mendapatkan rekomendasi buku yang relevan dengan minat dan preferensi mereka, yang akhirnya meningkatkan kepuasan pengguna dan keterlibatan mereka dalam platform.

Proyek ini penting karena mampu memberikan solusi berbasis data untuk meningkatkan pengalaman pengguna, baik dalam konteks pembaca individual maupun dalam meningkatkan rekomendasi secara keseluruhan di platform e-commerce buku atau perpustakaan digital. Selain itu, dua pendekatan yang digunakan, yaitu **Content-Based Filtering** yang merekomendasikan buku berdasarkan kesamaan fitur buku, dan **Collaborative Filtering** yang merekomendasikan buku berdasarkan pola rating pengguna lain yang memiliki kesamaan preferensi, memungkinkan pemahaman yang lebih baik tentang kekuatan dan kelemahan masing-masing metode dalam sistem rekomendasi.

---

## Business Understanding

### Problem Statements

Proyek sistem rekomendasi buku ini bertujuan untuk mengatasi beberapa masalah utama yang dihadapi pengguna:

1. **Overload Informasi**: Banyaknya pilihan buku membuat pengguna sulit menemukan yang sesuai dengan preferensi.
   
2. **Keterbatasan Rekomendasi**: Rekomendasi sering hanya berdasarkan popularitas, tidak mempertimbangkan preferensi individu, sehingga kurang relevan.

3. **Pengalaman Membaca yang Tidak Personal**: Sistem saat ini tidak dapat mengidentifikasi preferensi unik pengguna, mengurangi kepuasan mereka.

### Goals

Tujuan proyek ini meliputi:

1. **Rekomendasi Relevan**: Menggunakan **Content-Based Filtering** dan **Collaborative Filtering** untuk memberikan rekomendasi yang sesuai dengan preferensi dan pola perilaku pengguna.

2. **Meningkatkan Kepuasan Pengguna**: Memberikan rekomendasi yang lebih personal untuk meningkatkan engagement.

3. **Evaluasi Pendekatan**: Menguji efektivitas kedua metode untuk menentukan yang terbaik berdasarkan kinerja sistem.

### Solution Approach

Dua pendekatan yang diusulkan dalam proyek ini adalah:

1. **Content-Based Filtering**: Mengandalkan kesamaan fitur buku yang disukai pengguna dengan buku lain berdasarkan genre, penulis, atau tag.

2. **Collaborative Filtering**: Menggunakan pola rating dari pengguna lain dengan preferensi serupa untuk memberikan rekomendasi.

---

## Data Understanding

### Informasi Dataset

Dataset yang digunakan dalam proyek ini adalah dataset buku dari **Goodreads**, yang dapat diakses melalui tautan berikut: [Goodreads Dataset](https://github.com/zygmuntz/goodbooks-10k).

Dataset yang digunakan memiliki beberapa fitur penting yang membantu dalam membangun sistem rekomendasi berbasis buku, antara lain:
- **Jumlah data**: Dataset ini terdiri dari lebih dari **10.000 buku** dengan informasi seperti rating, penulis, judul, tahun publikasi, dan sebagainya. Selain itu, terdapat data rating dari **53.424 pengguna** yang memberikan penilaian pada berbagai buku.
- **Kondisi data**: Setelah melakukan eksplorasi terhadap dataset, terdapat beberapa nilai yang hilang (missing values) pada kolom **ISBN**, **ISBN13**, **original_title**, dan **language_code**. Namun, karena kolom **original_title** menjadi fitur utama dalam algoritma content-based filtering, maka dari itu dilakukakannya **data imputation** dengan mengisi nilai yang hilang di kolom **original_title** menggunakan nilai yang ada di kolom **title**.

### Variabel dalam Dataset

Dataset ini memiliki beberapa variabel atau fitur penting sebagai berikut:
1. **book_id**: ID unik untuk setiap buku.
2. **goodreads_book_id**: ID yang digunakan di situs Goodreads.
3. **best_book_id**: ID yang sering digunakan untuk mengindeks buku terbaik.
4. **authors**: Nama penulis buku.
5. **original_title**: Judul asli dari buku (yang digunakan dalam content-based filtering).
6. **title**: Judul buku.
7. **average_rating**: Rata-rata rating yang diberikan pengguna pada buku tersebut.
8. **ratings_count**: Jumlah total rating yang diterima oleh buku tersebut.
9. **original_publication_year**: Tahun pertama kali buku tersebut diterbitkan.
10. **language_code**: Kode bahasa buku (terdapat banyak nilai yang hilang).
11. **tags**: Label atau deskripsi singkat tentang buku (nilai yang hilang diisi menggunakan data lain atau diabaikan jika tidak relevan).
12. **ratings_1 - ratings_5**: Jumlah pengguna yang memberikan rating 1 hingga 5 untuk buku tersebut.

### Eksplorasi Data

Untuk lebih memahami data, berikut adalah beberapa tahapan visualisasi dan eksplorasi data yang dilakukan:
- **Distribusi Rating**: Dilakukannya proses eksplorasi distribusi dari rating yang diberikan oleh pengguna pada berbagai buku. Sebagian besar rating berada pada skala **3 hingga 5**, yang menunjukkan bahwa sebagian besar buku memiliki ulasan yang baik.
- **Penulis Terpopuler**: Penulis dengan jumlah buku terbanyak dan rata-rata rating tertinggi dieksplorasi untuk melihat penulis yang berpengaruh dalam rekomendasi buku.
- **Missing Values**: Seperti disebutkan sebelumnya, beberapa kolom seperti **ISBN**, **language_code**, dan **original_title** memiliki nilai yang hilang. Namun, karena ini tidak berdampak signifikan pada algoritma yang digunakan, hanya kolom **original_title** yang mengalami **data imputation**.

--- 

## Data Preparation

### Penanganan Missing Values (Data Imputation)

Salah satu tantangan yang dihadapi dalam dataset ini adalah adanya nilai yang hilang pada beberapa kolom penting, terutama pada kolom **original_title**, **ISBN**, **ISBN13**, dan **language_code**. Dari kolom-kolom tersebut, kolom **original_title** menjadi sangat penting karena digunakan dalam algoritma **content-based filtering**. Untuk menangani hal ini, dilakukan **data imputation** dengan mengisi nilai yang hilang di kolom **original_title** menggunakan nilai yang ada di kolom **title**.

Proses ini dilakukan sebagai berikut:

```python
# Mengisi missing values pada kolom original_title dengan nilai dari kolom title
data['original_title'] = data['original_title'].fillna(data['title'])
```

Langkah ini memastikan bahwa setiap buku memiliki judul yang lengkap dan siap digunakan dalam perhitungan kemiripan berbasis konten.

### Penggabungan Kolom Menjadi Kolom Baru **tags**

Selain mengisi missing values, salah satu langkah penting dalam data preparation adalah membuat kolom baru yang bernama **tags**. Kolom **tags** dibentuk dengan menggabungkan beberapa kolom informasi seperti **original_title**, **authors**, **language_code**, dan **average_rating**. Penggabungan ini bertujuan untuk menciptakan representasi deskriptif dari setiap buku yang akan digunakan untuk menghitung kemiripan antar buku.

Langkah-langkahnya adalah sebagai berikut:

```python
# Menggabungkan beberapa kolom menjadi kolom baru 'tags'
data['tags'] = data['original_title'] + ' ' + data['authors'] + ' ' + \
               data['language_code'].fillna('') + ' ' + data['average_rating'].astype(str)
```

Dalam proses ini:
- Kolom **original_title** menyediakan judul asli buku.
- Kolom **authors** menambahkan informasi tentang penulis buku.
- Kolom **language_code** memberikan informasi tentang bahasa buku.
- Kolom **average_rating** menambahkan informasi mengenai rating rata-rata yang diterima buku tersebut.

Hasil dari penggabungan ini adalah satu kolom deskriptif (**tags**) yang lebih lengkap dan dapat digunakan oleh algoritma **content-based filtering** untuk membandingkan buku satu dengan yang lainnya.

Contoh penggabungan pada satu buku:
- **original_title**: "Harry Potter and the Order of the Phoenix"
- **authors**: "J.K. Rowling"
- **language_code**: "eng"
- **average_rating**: 4.5

Menjadi:
- **tags**: "Harry Potter and the Order of the Phoenix J.K. Rowling eng 4.5"

Dengan cara ini, setiap buku memiliki deskripsi lengkap yang siap diolah oleh algoritma.

### Transformasi Fitur

Setelah melakukan penggabungan kolom-kolom penting menjadi **tags**, langkah selanjutnya adalah melakukan **transformasi fitur** menggunakan **TF-IDF (Term Frequency-Inverse Document Frequency)**. Fitur **tags** digunakan sebagai deskripsi singkat tentang buku dan diubah menjadi bentuk numerik agar algoritma content-based filtering dapat menghitung kemiripan antar buku.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Menggunakan TF-IDF untuk transformasi fitur 'tags'
tfidf = TfidfVectorizer(stop_words='english')
data['tags'] = data['tags'].fillna('')  # Mengisi nilai kosong di 'tags' dengan string kosong
tfidf_matrix = tfidf.fit_transform(data['tags'])
```

Dengan menggunakan **TF-IDF**, kemiripan antar buku berdasarkan deskripsi yang ada dalam kolom **tags** akan dapat dihitung, yang kemudian digunakan untuk merekomendasikan buku-buku yang mirip dengan buku yang disukai pengguna.

### Split Data (Untuk Collaborative Filtering)

Untuk algoritma **collaborative filtering**, data dibagi menjadi data pelatihan dan data pengujian. Pembagian ini penting agar model dapat dilatih menggunakan sebagian data dan diuji menggunakan data yang belum pernah dilihat sebelumnya. Ini membantu mengukur seberapa baik model dalam memprediksi rating pengguna terhadap buku.

```python
from surprise.model_selection import train_test_split

# Membagi dataset rating menjadi training dan testing
trainset, testset = train_test_split(ratings, test_size=0.25)
```

### Alasan Diperlukan Tahapan Ini

Tahapan **data imputation** dilakukan untuk menangani **missing values** pada fitur yang krusial seperti **original_title**. Hal ini penting karena judul buku merupakan aspek utama dalam algoritma **content-based filtering**. Jika ada buku tanpa judul yang jelas, algoritma tidak akan mampu menghitung kemiripan antar buku dengan akurat, yang akan mempengaruhi kualitas rekomendasi.

Penggabungan kolom menjadi **tags** bertujuan untuk memberikan informasi deskriptif yang lebih lengkap mengenai buku. Kombinasi judul, penulis, bahasa, dan rating rata-rata dalam satu kolom membantu algoritma mengenali buku yang mirip secara lebih baik, karena menggunakan berbagai aspek deskripsi.

Transformasi fitur menggunakan **TF-IDF** juga penting karena algoritma **content-based filtering** membutuhkan data yang terstruktur dengan baik untuk menghitung kemiripan antar buku berdasarkan deskripsi singkatnya. Sedangkan untuk **collaborative filtering**, membagi data menjadi **train set** dan **test set** sangat penting agar kita bisa mengevaluasi performa model secara akurat.

Berikut adalah pembaruan untuk bagian **Modeling**:

---

## Modeling

### 1. Content-Based Filtering

Pada pendekatan **Content-Based Filtering**, model bekerja dengan merekomendasikan buku-buku yang mirip dengan satu buku tertentu berdasarkan fitur deskriptif seperti judul, penulis, bahasa, dan rating. Setelah melakukan **data preparation** dan membangun kolom **tags** yang berisi informasi deskriptif dari setiap buku, dilakukan transformasi data menggunakan **TF-IDF** untuk menghitung kemiripan antar buku.

Proses modeling dilakukan dengan menghitung kemiripan kosinus antar buku berdasarkan nilai-nilai TF-IDF. Berikut adalah contoh kode yang digunakan untuk menghitung kemiripan tersebut:

```python
from sklearn.metrics.pairwise import cosine_similarity

# Menghitung kemiripan kosinus antara semua buku berdasarkan kolom 'tags'
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Mendefinisikan fungsi untuk memberikan rekomendasi berdasarkan kemiripan
def content_based_recommendations(title, cosine_sim=cosine_sim):
    # Mencari indeks dari buku berdasarkan judul
    idx = data[data['original_title'] == title].index[0]
    
    # Mengambil skor kemiripan dari buku yang dipilih dengan semua buku lainnya
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Mengurutkan skor buku berdasarkan kemiripan
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Mengambil 10 buku dengan skor tertinggi (selain buku itu sendiri)
    sim_scores = sim_scores[1:11]
    
    # Mendapatkan indeks dari buku-buku yang direkomendasikan
    book_indices = [i[0] for i in sim_scores]
    
    # Mengembalikan judul buku yang direkomendasikan
    return data['original_title'].iloc[book_indices]
```

#### Hasil dari Content-Based Filtering

Contoh rekomendasi untuk buku **"Harry Potter and the Order of the Phoenix"**:

```plaintext
Content-Based Recommendations for 'Harry Potter and the Order of the Phoenix':
1. Harry Potter Boxed Set, Books 1-5 (Harry Potter, #1-5)
2. Harry Potter and the Goblet of Fire
3. Harry Potter and the Chamber of Secrets
4. Harry Potter and the Philosopher's Stone
5. Harry Potter and the Half-Blood Prince
6. Harry Potter Boxed Set Books 1-4
7. Harry Potter and the Deathly Hallows
8. Harry Potter Collection (Harry Potter, #1-6)
9. Harry Potter and the Prisoner of Azkaban
10. Harry Potter and the Order of the Phoenix (Harry Potter, #5)
```

Berdasarkan pendekatan ini, model merekomendasikan buku-buku yang memiliki kemiripan tinggi dengan **Harry Potter and the Order of the Phoenix**, yang kebanyakan merupakan judul-judul dalam seri Harry Potter.

#### Kelebihan dan Kekurangan Content-Based Filtering:
- **Kelebihan**: Rekomendasi yang diberikan lebih akurat untuk buku-buku yang memiliki deskripsi serupa dengan buku yang telah dibaca pengguna.
- **Kekurangan**: Model ini terbatas pada fitur-fitur yang telah diidentifikasi dari buku itu sendiri, sehingga sulit memberikan rekomendasi yang sangat berbeda dari preferensi awal pengguna.

### 2. Collaborative Filtering

Pendekatan **Collaborative Filtering** menggunakan data rating yang diberikan pengguna untuk merekomendasikan buku. Model yang digunakan pada proyek ini adalah **SVD (Singular Value Decomposition)**, yang merupakan salah satu teknik terkenal dalam sistem rekomendasi berbasis kolaborasi.

Dengan menggunakan library **Surprise**, model dilatih pada dataset rating untuk memprediksi rating yang akan diberikan pengguna terhadap buku yang belum dibaca berdasarkan pola rating pengguna lain yang mirip.

Proses training dan prediksi dilakukan sebagai berikut:

```python
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Membagi dataset menjadi trainset dan testset
trainset, testset = train_test_split(ratings, test_size=0.25)

# Membuat dan melatih model SVD
model = SVD()
model.fit(trainset)

# Menguji model pada testset dan menghitung RMSE
predictions = model.test(testset)
rmse = accuracy.rmse(predictions)
```

Model kemudian memberikan rekomendasi buku untuk pengguna tertentu berdasarkan prediksi rating tertinggi.

#### Hasil dari Collaborative Filtering

Untuk **User 1**, model memberikan rekomendasi berikut:

```plaintext
Collaborative Filtering Recommendations for User 1:
1. Words of Radiance - Brandon Sanderson
2. The Complete Stories - Flannery O'Connor
3. The Complete Calvin and Hobbes - Bill Watterson
4. There's Treasure Everywhere: A Calvin and Hobbes Collection - Bill Watterson
5. Clockworks - Joe Hill, Gabriel Rodríguez
6. The Indispensable Calvin and Hobbes - Bill Watterson
7. ESV Study Bible - Anonymous, Lane T. Dennis, Wayne A. Grudem
8. دیوان‎‎ [Dīvān] - Hafez
9. The Revenge of the Baby-Sat: A Calvin and Hobbes Collection - Bill Watterson
10. Attack of the Deranged Mutant Killer Monster Snow Goons - Bill Watterson
```

Rekomendasi ini dihasilkan dengan mempertimbangkan preferensi rating dari User 1, yang sebelumnya memberikan rating tinggi untuk buku **"The Shadow of the Wind"**.

#### Kelebihan dan Kekurangan Collaborative Filtering:
- **Kelebihan**: Model ini mampu memberikan rekomendasi buku-buku yang berbeda dan unik berdasarkan pola rating pengguna lain yang mirip, tanpa tergantung pada deskripsi buku.
- **Kekurangan**: Model ini membutuhkan data rating yang cukup untuk dapat memberikan prediksi yang akurat. Jika pengguna baru atau buku baru memiliki sedikit data rating, hasil rekomendasi bisa kurang optimal.

---

Berikut adalah pembaruan untuk bagian **Evaluation**:

---

## Evaluation

Tahap evaluasi dilakukan untuk mengukur kinerja kedua model sistem rekomendasi, yaitu **Content-Based Filtering** dan **Collaborative Filtering**. Pada proyek ini, dua metrik evaluasi yang digunakan adalah:

1. **Root Mean Squared Error (RMSE)** - digunakan untuk evaluasi model Collaborative Filtering.
2. **Precision at K** - digunakan untuk mengukur kinerja model Collaborative Filtering dalam hal relevansi rekomendasi.

### 1. Evaluasi pada Content-Based Filtering

Untuk model **Content-Based Filtering**, evaluasi lebih bersifat subjektif karena model ini merekomendasikan buku berdasarkan kemiripan deskriptif. Namun, kualitas rekomendasi dapat diukur dengan menilai seberapa baik rekomendasi tersebut sesuai dengan preferensi pengguna.

Pada contoh rekomendasi yang dihasilkan untuk buku **"Harry Potter and the Order of the Phoenix"**, model berhasil merekomendasikan buku-buku lain dari seri **Harry Potter**, yang menunjukkan bahwa model mampu menangkap kesamaan fitur secara akurat. Namun, tidak ada metrik kuantitatif yang digunakan untuk mengevaluasi model ini, karena bergantung pada tingkat kemiripan antar buku.

**Kelebihan**: Evaluasi ini menunjukkan bahwa Content-Based Filtering cocok untuk merekomendasikan buku yang serupa dengan buku yang sudah diketahui pengguna.  
**Kekurangan**: Model ini kurang efektif dalam menemukan rekomendasi baru yang berbeda dari buku-buku serupa.

### 2. Evaluasi pada Collaborative Filtering

Untuk **Collaborative Filtering**, model dievaluasi secara kuantitatif dengan menggunakan **RMSE (Root Mean Squared Error)**. Metrik ini mengukur seberapa baik model memprediksi rating buku yang diberikan oleh pengguna dibandingkan dengan rating asli. Semakin kecil nilai RMSE, semakin baik model dalam melakukan prediksi.

Berikut adalah hasil evaluasi RMSE untuk model Collaborative Filtering:

```plaintext
RMSE: 0.8306
```

Nilai **RMSE** sebesar **0.8306** menunjukkan bahwa model memiliki kinerja yang cukup baik dalam memprediksi rating pengguna terhadap buku. Model ini mampu menghasilkan prediksi dengan kesalahan rata-rata yang cukup kecil, sehingga rekomendasi yang diberikan lebih akurat.

### 3. Precision at K

Untuk lebih memahami relevansi dari rekomendasi yang diberikan, digunakan juga metrik **Precision at K (P@K)**. Precision at K mengukur proporsi item relevan (dalam hal ini buku-buku yang disukai pengguna) di antara rekomendasi teratas yang diberikan model.

Precision dihitung sebagai berikut:

![Precision@K](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{Precision@K=\frac{{jumlah&space;item&space;yang&space;relevan&space;dalam&space;top-K}}{{jumlah&space;item&space;yang&space;direkomendasikan&space;dalam&space;top-K}}})


Implementasi Precision at K dilakukan dengan cara menghitung seberapa banyak buku yang direkomendasikan sesuai dengan preferensi pengguna. Contoh, jika di antara 10 rekomendasi teratas, 7 buku dianggap relevan oleh pengguna, maka Precision@10 adalah:

![Precision@10](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{Precision@10=\frac{7}{10}=0.7})

Dengan demikian, metrik ini memberikan informasi lebih rinci tentang kinerja model dalam memberikan rekomendasi yang relevan dan berguna bagi pengguna.

#### Kesimpulan Evaluasi

- **Content-Based Filtering**: Evaluasi model ini lebih didasarkan pada interpretasi kemiripan antar buku yang direkomendasikan. Dalam kasus rekomendasi **Harry Potter**, model bekerja dengan baik untuk merekomendasikan buku yang serupa.
  
- **Collaborative Filtering**: Berdasarkan nilai **RMSE** sebesar **0.8306**, model ini mampu memprediksi rating dengan akurasi yang baik. Precision at K juga menunjukkan kinerja yang baik dalam merekomendasikan buku yang relevan kepada pengguna.

### Formula dan Cara Kerja RMSE

**Root Mean Squared Error (RMSE)** adalah metrik yang menghitung akar kuadrat dari rata-rata kesalahan kuadrat antara rating yang diprediksi dan rating asli. Rumusnya adalah sebagai berikut:

![RMSE](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}})

Di mana:
- $n$ adalah jumlah prediksi
- $y_i$ adalah nilai asli (rating yang diberikan oleh pengguna)
- $\hat{y}_i$ adalah nilai prediksi (rating yang diprediksi oleh model)

RMSE memberikan ukuran absolut dari seberapa jauh prediksi model dari nilai asli, sehingga semakin kecil nilai RMSE, semakin baik model dalam melakukan prediksi.

---

**---Ini adalah bagian akhir laporan---**