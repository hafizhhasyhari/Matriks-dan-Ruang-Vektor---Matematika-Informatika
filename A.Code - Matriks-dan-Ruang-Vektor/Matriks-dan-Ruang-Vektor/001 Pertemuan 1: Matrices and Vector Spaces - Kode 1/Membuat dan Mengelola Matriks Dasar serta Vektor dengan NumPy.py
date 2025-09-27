# Pertemuan 1: Matrices and Vector Spaces - Kode 1/9
import numpy as np

# 1. Membuat matriks 2x2
A = np.array([[1, 2],
              [3, 4]])
print("Matriks A:\n", A)

# 2. Menghitung determinan matriks 2x2
det_A = np.linalg.det(A)
print("Determinan A:", det_A)

# 3. Membalik matriks jika invertible
if det_A != 0:
    A_inv = np.linalg.inv(A)
    print("Invers A:\n", A_inv)
else:
    print("Matriks A tidak invertible.")

# 4. Menjumlahkan dua matriks
B = np.array([[5, 6],
              [7, 8]])
sum_AB = A + B
print("Jumlah A + B:\n", sum_AB)

# 5. Mengalikan matriks
product_AB = np.dot(A, B)
print("Perkalian A * B:\n", product_AB)

# 6. Membuat vektor kolom
v = np.array([[1],
              [2]])
print("Vektor v:\n", v)

# 7. Menghitung panjang vektor (norm)
norm_v = np.linalg.norm(v)
print("Norm vektor v:", norm_v)

# 8. Menambahkan vektor ke matriks (menjadi kolom baru)
A_with_v = np.column_stack((A, v))
print("Matriks A dengan vektor v sebagai kolom baru:\n", A_with_v)

# 9. Menguji apakah vektor termasuk dalam ruang span matriks (apakah v bisa ditulis sebagai kombinasi linear dari kolom matriks A)
# Misalnya, apakah v dalam span dari kolom A
try:
    coeffs, residuals, rank, s = np.linalg.lstsq(A, v, rcond=None)
    print("Koefisien kombinasi linear v:\n", coeffs)
    print("Residuals:\n", residuals)
except np.linalg.LinAlgError:
    print("Tidak dapat menyelesaikan persamaan.")
