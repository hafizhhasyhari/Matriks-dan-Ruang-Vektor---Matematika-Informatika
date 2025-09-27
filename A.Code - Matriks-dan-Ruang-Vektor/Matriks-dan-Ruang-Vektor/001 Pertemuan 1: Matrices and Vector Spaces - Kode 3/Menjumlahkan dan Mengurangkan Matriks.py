# Judul : Menjumlahkan dan Mengurangkan Matriks
# Repo : Matriks-dan-Ruang-Vektor
# Oleh : hafizhhasyhari
# Tanggal : 14 September 2023

import numpy as np

# Mendefinisikan dua matriks 2x2
A = np.array([[2, 5],
              [1, 3]])

B = np.array([[4, 2],
              [7, 1]])

print("Matriks A:\n", A)
print("Matriks B:\n", B)

# Menjumlahkan matriks A dan B
jumlah = A + B
print("Hasil Penjumlahan A + B:\n", jumlah)

# Mengurangkan matriks A dan B
kurang = A - B
print("Hasil Pengurangan A - B:\n", kurang)

# END
