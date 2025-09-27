# Judul : Menghitung Determinan dan Invers Matriks
# Repo : Matriks-dan-Ruang-Vektor
# Oleh : hafizhhasyhari
# Tanggal : 14 September 2023

import numpy as np

# Membuat matriks 2x2
A = np.array([[3, 2],
              [1, 4]])

print("Matriks A:\n", A)

# Menghitung determinan matriks A
det_A = np.linalg.det(A)
print("Determinan A:", det_A)

# Mengecek apakah matriks invertible dan menghitung inversnya
if det_A != 0:
    A_inv = np.linalg.inv(A)
    print("Invers dari A:\n", A_inv)
else:
    print("Matriks A tidak invertible karena determinan = 0.")

# END
