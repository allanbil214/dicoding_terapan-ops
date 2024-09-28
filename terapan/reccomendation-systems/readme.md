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

### 1. Cosine Similarity (Content-Based Filtering)

Pada pendekatan **Content-Based Filtering**, algoritma yang digunakan untuk menghitung kemiripan antar buku adalah **Cosine Similarity**. Cosine similarity mengukur sudut kosinus antara dua vektor, di mana vektor tersebut adalah representasi dari setiap buku dalam bentuk deskripsi fitur setelah dilakukan **TF-IDF (Term Frequency-Inverse Document Frequency)**. Semakin kecil sudut antara dua vektor (semakin dekat ke 1 nilai cosine similarity), maka semakin mirip kedua buku tersebut.

#### Cara Kerja Cosine Similarity:
Cosine similarity dihitung dengan rumus sebagai berikut:

![Cosine Similarity](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{{cosine\_similarity}(A,B)=\frac{{A\cdot&space;B}}{{\|A\|\times\|B\|}}})

- $A$ dan $B$ adalah dua vektor yang mewakili dua buku dalam ruang fitur.
- $A \cdot B$ adalah hasil kali dot product dari kedua vektor.
- $\|A\|$ dan $\|B\|$ adalah norma (magnitudo) dari vektor $A$ dan $B$.

Nilai Cosine Similarity berkisar antara 0 hingga 1:
- 1 berarti kedua vektor (buku) sangat mirip.
- 0 berarti tidak ada kemiripan.

#### Parameter Cosine Similarity:
Model **Cosine Similarity** mengunakan vektor yang sudah dihasilkan dari **TF-IDF**. Proses ini bertumpu pada representasi deskriptif (kolom **tags**) dari setiap buku yang telah melalui transformasi teks menjadi vektor.

#### Hasil dari Cosine Similarity

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

#### Kelebihan:
- **Sederhana dan Efektif**: Algoritma ini sederhana untuk diimplementasikan dan sangat cocok ketika kita memiliki fitur deskriptif yang baik dari setiap item (seperti **tags** pada buku). Cosine similarity bisa menghitung kemiripan dengan cepat dan langsung memberikan rekomendasi berdasarkan atribut item yang telah ada.
- **Tidak Memerlukan Data Pengguna**: Tidak bergantung pada data interaksi pengguna-buku, sehingga model tetap dapat memberikan rekomendasi bahkan kepada pengguna baru (cold start untuk pengguna).
  
#### Kekurangan:
- **Cenderung Overfit ke Preferensi Item yang Serupa**: Karena hanya memperhitungkan atribut yang sudah ada pada item, model ini mungkin hanya merekomendasikan buku yang sangat mirip dengan buku yang sudah dipilih atau dibaca pengguna. Ini dapat menyebabkan kurangnya keragaman dalam rekomendasi.
- **Keterbatasan dalam Menangkap Preferensi Pengguna yang Kompleks**: Model ini hanya berfokus pada fitur item dan tidak mempertimbangkan preferensi pengguna secara lebih luas. Jadi, jika preferensi pengguna tidak jelas dari atribut buku, model ini bisa kurang akurat.


### 2. Singular Value Decomposition (Collaborative Filtering)

Pada pendekatan **Collaborative Filtering**, model yang digunakan adalah **SVD (Singular Value Decomposition)**, yang merupakan salah satu teknik paling populer dalam sistem rekomendasi berbasis matrix factorization. Model ini memfaktorkan matriks interaksi pengguna-buku (misalnya, matriks rating) menjadi tiga matriks yang lebih kecil, yang mempermudah prediksi rating buku yang belum pernah diulas oleh pengguna.

#### Cara Kerja SVD:
SVD memecah matriks pengguna-buku ($R$) menjadi tiga matriks:

![Matrix Decomposition](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{R=U\Sigma&space;V^T})

- $U$ adalah matriks pengguna (mengandung preferensi pengguna terhadap fitur tersembunyi).
- $\Sigma$ adalah matriks diagonal yang berisi singular values.
- $V^T$ adalah matriks fitur buku (mengandung informasi tentang hubungan antar fitur buku).

Prediksi rating dihitung dengan merekonstruksi matriks $R$ dari hasil perkalian ketiga matriks tersebut. 

#### Parameter pada SVD:
Model **SVD** memiliki beberapa parameter utama yang dapat disesuaikan:
- **n_factors**: Jumlah faktor tersembunyi yang digunakan untuk merepresentasikan setiap pengguna dan buku. Default biasanya 100.
- **n_epochs**: Jumlah iterasi pelatihan model untuk memastikan konvergensi.
- **lr_all**: Learning rate untuk pembaruan nilai faktor.
- **reg_all**: Faktor regulasi untuk mencegah overfitting dengan membatasi bobot model.

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

#### Kelebihan:
- **Memanfaatkan Data Interaksi Pengguna**: SVD mampu menangkap preferensi laten pengguna berdasarkan pola interaksi (seperti rating atau perilaku eksplisit lainnya), sehingga dapat memberikan rekomendasi yang lebih personal dan akurat.
- **Mengatasi Masalah Sparsity**: Dengan melakukan factorization, SVD bisa menangani masalah **sparsity** (kelangkaan data) yang umum dalam data interaksi pengguna-item. Algoritma ini bisa memberikan prediksi yang baik bahkan dengan sedikit interaksi yang tersedia.
  
#### Kekurangan:
- **Cold Start untuk Pengguna dan Item Baru**: SVD membutuhkan data interaksi pengguna-buku. Jika tidak ada data interaksi (misalnya untuk pengguna atau item baru), model ini kesulitan untuk memberikan rekomendasi yang relevan.
- **Lebih Rumit dan Memakan Waktu Pelatihan**: Dibandingkan dengan metode seperti Cosine Similarity, SVD lebih kompleks dalam perhitungannya. Selain itu, model ini juga membutuhkan waktu pelatihan yang lebih lama, terutama ketika bekerja dengan dataset yang besar.

---

## Evaluation

### 1. Evaluasi pada Content-Based Filtering

#### Precision

Precision mengukur proporsi rekomendasi yang benar-benar relevan dibandingkan dengan total rekomendasi yang diberikan. Rumus untuk menghitung precision adalah:

![Precision](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{Precision=\frac{Jumlah&space;True&space;Positives}{Jumlah&space;Rekomendasi&space;yang&space;Diberikan}})

Dalam konteks ini:
- **True Positives** adalah jumlah buku yang direkomendasikan dan juga benar-benar sudah dibaca atau disukai oleh pengguna.
- **Jumlah Rekomendasi yang Diberikan** adalah total buku yang direkomendasikan oleh sistem.

Evaluasi precision dilakukan dalam dua versi:

1. **Precision berdasarkan variabel _actual_**: Dalam versi ini, precision dihitung dengan membandingkan buku yang direkomendasikan dengan daftar buku _actual_. Hasil evaluasi ini menunjukkan precision sebesar **1.0**, yang berarti bahwa semua buku yang direkomendasikan adalah bagian dari seri **Harry Potter**, sesuai dengan variabel _actual_.

2. **Precision berdasarkan perhitungan dari user 2**: Untuk mengevaluasi model menggunakan data pengguna lain, precision dihitung berdasarkan relevansi rekomendasi terhadap preferensi pengguna dengan ID **user 2**. Pada kasus ini, precision adalah **0.7**, yang menunjukkan bahwa 70% dari buku yang direkomendasikan sesuai dengan apa yang sudah diberi rating tinggi oleh pengguna tersebut.

#### Recall

Selain precision, saya juga menghitung **Recall**, yang mengukur sejauh mana model dapat menemukan semua buku relevan dalam koleksi pengguna. Rumus recall adalah:

![Recall](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{Recall=\frac{Jumlah&space;True&space;Positives}{Jumlah&space;Total&space;Buku&space;Relevan&space;yang&space;Ada}})

Pada evaluasi untuk **user 2**, recall menghasilkan nilai sebesar **0.13**, menunjukkan bahwa hanya sebagian kecil dari total buku relevan yang berhasil ditemukan oleh model.
### 2. Evaluasi pada Collaborative Filtering

#### RMSE

Untuk **Collaborative Filtering**, model dievaluasi secara kuantitatif dengan menggunakan **RMSE (Root Mean Squared Error)**. Metrik ini mengukur seberapa baik model memprediksi rating buku yang diberikan oleh pengguna dibandingkan dengan rating asli. Semakin kecil nilai RMSE, semakin baik model dalam melakukan prediksi.

Berikut adalah hasil evaluasi RMSE untuk model Collaborative Filtering:

```plaintext
RMSE: 0.8306
```

Nilai **RMSE** sebesar **0.8306** menunjukkan bahwa model memiliki kinerja yang cukup baik dalam memprediksi rating pengguna terhadap buku. Model ini mampu menghasilkan prediksi dengan kesalahan rata-rata yang cukup kecil, sehingga rekomendasi yang diberikan lebih akurat.

**Root Mean Squared Error (RMSE)** adalah metrik yang menghitung akar kuadrat dari rata-rata kesalahan kuadrat antara rating yang diprediksi dan rating asli. Rumusnya adalah sebagai berikut:

![RMSE](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}})

Di mana:
- $n$ adalah jumlah prediksi
- $y_i$ adalah nilai asli (rating yang diberikan oleh pengguna)
- $\hat{y}_i$ adalah nilai prediksi (rating yang diprediksi oleh model)

RMSE memberikan ukuran absolut dari seberapa jauh prediksi model dari nilai asli, sehingga semakin kecil nilai RMSE, semakin baik model dalam melakukan prediksi.

#### Precision at K

Untuk lebih memahami relevansi dari rekomendasi yang diberikan, digunakan juga metrik **Precision at K (P@K)**. Precision at K mengukur proporsi item relevan (dalam hal ini buku-buku yang disukai pengguna) di antara rekomendasi teratas yang diberikan model.

Precision dihitung sebagai berikut:

![Precision@K](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{Precision@K=\frac{{jumlah&space;item&space;yang&space;relevan&space;dalam&space;top-K}}{{jumlah&space;item&space;yang&space;direkomendasikan&space;dalam&space;top-K}}})


Implementasi Precision at K dilakukan dengan cara menghitung seberapa banyak buku yang direkomendasikan sesuai dengan preferensi pengguna. Contoh, jika di antara 10 rekomendasi teratas, 7 buku dianggap relevan oleh pengguna, maka Precision@10 adalah:

![Precision@10](https://latex.codecogs.com/png.image?\dpi{150}\bg{white}\mathbf{Precision@10=\frac{7}{10}=0.7})

Dengan demikian, metrik ini memberikan informasi lebih rinci tentang kinerja model dalam memberikan rekomendasi yang relevan dan berguna bagi pengguna.

#### Kesimpulan Evaluasi

- **Content-Based Filtering**: Metrik precision menunjukkan bahwa model mampu merekomendasikan buku dengan akurasi tinggi dalam hal relevansi dengan apa yang sudah dibaca oleh pengguna. Namun, rendahnya nilai recall menunjukkan bahwa masih banyak buku relevan yang belum direkomendasikan oleh model. Kombinasi precision dan recall ini membantu memberikan gambaran lebih jelas tentang kinerja model dalam merekomendasikan konten yang sesuai dengan preferensi pengguna.
  
- **Collaborative Filtering**: Berdasarkan nilai **RMSE** sebesar **0.8306**, model ini mampu memprediksi rating dengan akurasi yang baik. Precision at K juga menunjukkan kinerja yang baik dalam merekomendasikan buku yang relevan kepada pengguna.

---

**---Ini adalah bagian akhir laporan---**