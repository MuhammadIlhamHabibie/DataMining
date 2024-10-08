# -*- coding: utf-8 -*-
"""4101421128_Tugas Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z98b3WofLs1kL6JS2jl6SXqxEcMFGHvn
"""

# 4101421128_Muhammad Ilham Habibie

import pandas as pd
# memuat data dari file csv
df = pd.read_csv('movie_sample_dataset.csv')
# membaca dataset
df.head()
# menampilkan 5 baris pertama dari dataset

# menampilkan banyaknya baris dan kolom
df.shape

import numpy as np
# mengganti "?" dengan NaN
df.replace ("?", np.nan, inplace=True)
# memeriksa jumlah missing values di setiap kolom
print(df.isnull().sum())

# mengkoreksi data type tiap kolom
df.dtypes

# menghapus baris yang memiliki nilai NaN di kolom gross dan budget
bersih = df.dropna(subset=['gross', 'budget'])
# mengatasi kesalahan penulisan pada perbedaan antara "Color" dan "color"
bersih['color'] = bersih['color'].str.capitalize()

# mengganti missing value dengan rata-rata pada kolom gross dan budget
cols_to_replace = ["gross", "budget"]
for col in cols_to_replace:
  avg_value = df[col].astype(float).mean()
  df[col].replace(np.nan, avg_value, inplace=True)
  print(f"Average of {col}: {avg_value}")

# mencari modus (nilai yang sering muncul) pada kolom director_name, color, genres
koreksimodusdirector=df["director_name"].value_counts().idxmax()
koreksimoduscolor=df["color"].value_counts().idxmax()
koreksimodusgenres=df["genres"].value_counts().idxmax()
# mengisi sel kosong nilai modus
df["director_name"].replace(np.nan,koreksimodusdirector , inplace=True)
df["color"].replace(np.nan,koreksimoduscolor , inplace=True)
df["genres"].replace(np.nan,koreksimodusgenres , inplace=True)
# mengecek modus director, color, dan genres
print(f"Nilai yang sering muncul di kolom director = {koreksimodusdirector}")
print(f"Nilai yang sering muncul di kolom color = {koreksimoduscolor}")
print(f"Nilai yang sering muncul di kolom genres = {koreksimodusgenres}")

# membuat bersih sebagai salinan data asli
bersih = df.copy()
# menghapus baris yang memiliki nilai NaN di kolom gross dan budget
bersih = bersih.dropna(subset=['gross', 'budget'])
# filter baris dengan nilai budget dan gross yang bernilai negatif
bersih = bersih[(bersih['budget'] >= 0) & (bersih['gross'] >= 0)]
print(df.isnull().sum())

# mengubah tipe data kolom yang diperlukan
df[["color", "director_name", "genres"]]=df[["color", "director_name", "genres"]].astype(str)
df[["budget", "gross"]]=df[["budget", "gross"]].astype(float)

# normalisasi teks ke huruf kecil
bersih['color'] = bersih['color'].str.lower()
bersih['director_name'] = bersih['director_name'].str.lower()
bersih['genres'] = bersih['genres'].str.lower()
bersih['language'] = bersih['language'].str.lower()
bersih['country'] = bersih['country'].str.lower()
bersih['actors'] = bersih['actors'].str.lower()

# cek data huruf kecil atau belum
print(bersih['actors'].head())

# menyimpan data yang telah diproses ke dalam file csv baru
bersih.to_csv('ilham_movie_dataset_cleaned.csv', index=False)