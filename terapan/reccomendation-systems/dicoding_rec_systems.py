# -*- coding: utf-8 -*-
"""dicoding_rec_systems.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LDBM4LVps-q6-b_OXmoWh1Z_xBms9-eM

Perintah `!pip install scikit-surprise` digunakan untuk menginstal pustaka Python bernama "scikit-surprise", yang dirancang untuk membangun dan menganalisis sistem rekomendasi.
"""

!pip install scikit-surprise

"""Kode berikut mengimpor pustaka untuk manipulasi data, transformasi teks, pengukuran kesamaan, dan pembangunan sistem rekomendasi."""

# Importing necessary libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

"""Kode berikut memuat dataset contoh tentang buku dari URL (GoodReads) yang diberikan dan menyimpannya dalam variabel `data` menggunakan pustaka pandas."""

# Project Overview
# Loading a sample dataset (Movies dataset)
url = 'https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv'
data = pd.read_csv(url)

"""Kode berikut mencetak jumlah total baris dan kolom dalam dataset serta daftar nama kolom yang ada."""

# Data Understanding
print(f"Total Rows: {data.shape[0]}, Total Columns: {data.shape[1]}")
print(f"Dataset Columns: {data.columns.tolist()}")

"""Perintah `data.head()` menampilkan lima baris pertama dari dataset, memberikan gambaran awal tentang struktur dan konten data."""

data.head()

"""Perintah `print(data.isna().sum())` menghitung dan menampilkan jumlah nilai kosong (NaN) untuk setiap kolom dalam dataset, membantu mengidentifikasi masalah data yang perlu ditangani."""

print(data.isna().sum())

"""Perintah berikut menggantikan nilai kosong di kolom `original_title` dengan nilai dari kolom `title`, memastikan tidak ada nilai hilang dalam kolom `original_title`."""

data['original_title'] = data['original_title'].fillna(data['title'])

"""Kode berikut membuat kolom baru bernama `tags` yang menggabungkan informasi dari kolom `authors`, `original_title`, dan `average_rating` (dikonversi ke string) untuk digunakan dalam pemfilteran berbasis konten."""

# Data Preparation
# Selecting relevant columns for the content-based filtering
data['tags'] = data['authors'] + " " + data['original_title'] + " " + data['average_rating'].astype(str)

"""Menampilkan atau melakukan pengecekan hasil dari kode sebelumnya."""

data['tags'].head()

"""Memastikan tidak ada null value, atau missing value pada kolom tags."""

print(data['tags'].isna().sum())

"""Kode berikut menggunakan `TfidfVectorizer` untuk mengubah kolom `tags` menjadi matriks TF-IDF, yang merepresentasikan teks secara numerik dan mengabaikan kata-kata umum (stop words) dalam bahasa Inggris."""

# Content-Based Filtering
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(data['tags'])

"""Kode berikut menghitung matriks kesamaan kosinus antara semua item dalam matriks TF-IDF, yang digunakan untuk mengukur seberapa mirip satu item dengan item lainnya berdasarkan konten."""

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

"""Fungsi `content_based_recommendations` merekomendasikan buku berdasarkan kesamaan konten dengan cara mencari indeks buku yang diberikan, menghitung skor kesamaan, mengurutkannya, dan mengembalikan sepuluh judul buku teratas yang paling mirip."""

# Function to recommend books based on content
def content_based_recommendations(title, cosine_sim=cosine_sim):
    idx = data.index[data['original_title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]
    return data['original_title'].iloc[book_indices]

"""Kode tersebut mencetak rekomendasi buku berdasarkan konten untuk judul "Harry Potter and the Order of the Phoenix" dengan menggunakan fungsi `content_based_recommendations`."""

# Example of content-based recommendation
print("Content-Based Recommendations for 'Harry Potter':")
print(content_based_recommendations('Harry Potter and the Order of the Phoenix'))

"""Kode untuk menghitung presisi melalui variable yang berisi semua buku Harry Potter yang ada pada dataset."""

def calculate_precision(recommendations, actual_books_read):
  true_positives = len(set(recommendations) & set(actual_books_read))
  precision = true_positives / len(recommendations) if len(recommendations) > 0 else 0
  return precision

# Example usage:
recommended_books = content_based_recommendations('Harry Potter and the Order of the Phoenix').tolist()
# Let's assume the user actually read these books (replace with actual user data)
actual_books_read = ['Harry Potter and the Order of the Phoenix (Harry Potter, #5, Part 1)', 'Harry Potter Boxed Set, Books 1-5 (Harry Potter, #1-5)', 'Harry Potter and the Goblet of Fire', 'Harry Potter and the Chamber of Secrets', "Harry Potter and the Philosopher's Stone", 'Harry Potter and the Half-Blood Prince', 'Harry Potter Boxed Set Books 1-4', 'Harry Potter and the Deathly Hallows', 'Harry Potter Collection (Harry Potter, #1-6)', 'Harry Potter and the Prisoner of Azkaban']

precision = calculate_precision(recommended_books, actual_books_read)
print(f"Precision: {precision}")

"""Kode ini memiliki fungsi untuk menghitung presisi dan recall dari model, dengan membandingkan buku buku yang ada pada user 2 (dimana user 2 ini telah membaca buku yang banyak pada dataset tersebut) ke buku yang direkomendasikan oleh model."""

# Mengambil buku-buku relevan berdasarkan rating
def get_relevant_books(user_id, threshold=4):
    relevant_books = ratings[(ratings['user_id'] == user_id) & (ratings['rating'] >= threshold)]['book_id'].tolist()
    return relevant_books

# Menghitung Precision dari rekomendasi berbasis konten
def calculate_precision(user_id, recommended_books):
    relevant_books = get_relevant_books(user_id)
    relevant_and_recommended = [book for book in recommended_books if book in relevant_books]
    precision = len(relevant_and_recommended) / len(recommended_books) if recommended_books else 0
    return precision

# Menghitung Recall dari rekomendasi berbasis konten
def calculate_recall(user_id, recommended_books):
    relevant_books = get_relevant_books(user_id)
    relevant_and_recommended = [book for book in recommended_books if book in relevant_books]
    recall = len(relevant_and_recommended) / len(relevant_books) if relevant_books else 0
    return recall

# Memperbarui fungsi rekomendasi berbasis konten untuk menghitung precision dan recall
def content_based_recommendations_with_precision_recall(title, user_id, cosine_sim=cosine_sim):
    # Mendapatkan rekomendasi berbasis konten
    idx = data.index[data['original_title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    book_indices = [i[0] for i in sim_scores]
    recommended_books = data['book_id'].iloc[book_indices].tolist()

    # Menghitung precision dan recall
    precision = calculate_precision(user_id, recommended_books)
    recall = calculate_recall(user_id, recommended_books)

    return data['original_title'].iloc[book_indices], precision, recall

# Contoh penggunaan fungsi dengan precision dan recall
title = 'Harry Potter and the Order of the Phoenix'
user_id = 2  # ID pengguna untuk evaluasi
recommended_books, precision, recall = content_based_recommendations_with_precision_recall(title, user_id)

print(f"Rekomendasi berbasis konten untuk '{title}':")
print(recommended_books)
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

"""Kode berikut memuat dataset rating dari URL yang diberikan dan menyimpannya dalam variabel `ratings` menggunakan pustaka pandas."""

# Collaborative Filtering
# Loading ratings dataset
url_ratings = 'https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/ratings.csv'
ratings = pd.read_csv(url_ratings)

"""Melihat 5 baris pertama pada dataframe ratings."""

ratings.head()

"""Kode berikut mempersiapkan dataset untuk pemfilteran kolaboratif dengan menggunakan `Reader` untuk mendefinisikan skala rating, dan memuat data dari DataFrame `ratings` ke dalam format yang dapat digunakan oleh pustaka Surprise."""

# Preparing the dataset for collaborative filtering
reader = Reader(rating_scale=(1, 5))
data_collab = Dataset.load_from_df(ratings[['user_id', 'book_id', 'rating']], reader)

"""Kode berikut membagi dataset menjadi set pelatihan dan pengujian, dengan 80% data digunakan untuk pelatihan dan 20% untuk pengujian, menggunakan fungsi `train_test_split` dari pustaka Surprise."""

# Train-test split
trainset, testset = train_test_split(data_collab, test_size=0.2)

"""Kode berikut menggunakan algoritma SVD (Singular Value Decomposition) untuk pelatihan model pemfilteran kolaboratif, kemudian menguji model tersebut pada set pengujian untuk menghasilkan prediksi rating."""

# Using SVD for collaborative filtering
model = SVD()
model.fit(trainset)
predictions = model.test(testset)

"""Perintah `accuracy.rmse(predictions)` menghitung dan menampilkan root mean square error (RMSE) dari prediksi yang dihasilkan oleh model, yang digunakan untuk mengevaluasi akurasi model pemfilteran kolaboratif."""

# Evaluation
accuracy.rmse(predictions)

"""Fungsi `collaborative_filtering_recommendations` merekomendasikan buku untuk pengguna tertentu dengan memprediksi rating untuk setiap buku, mengurutkan hasilnya, dan mengembalikan judul serta penulis dari buku-buku dengan rating tertinggi."""

# Function to recommend books for a user based on collaborative filtering
def collaborative_filtering_recommendations(user_id, n_recommendations=10):
    book_ids = ratings['book_id'].unique()
    predicted_ratings = []

    for book_id in book_ids:
        predicted_ratings.append((book_id, model.predict(user_id, book_id).est))

    predicted_ratings.sort(key=lambda x: x[1], reverse=True)
    top_books = predicted_ratings[:n_recommendations]
    book_titles = data[data['book_id'].isin([book[0] for book in top_books])]

    return book_titles[['original_title', 'authors']]

"""Kode berikut mencetak rekomendasi buku berdasarkan pemfilteran kolaboratif untuk pengguna dengan ID 1, menggunakan fungsi `collaborative_filtering_recommendations`."""

# Example of collaborative filtering recommendation
print("Collaborative Filtering Recommendations for User 1:")
print(collaborative_filtering_recommendations(1))