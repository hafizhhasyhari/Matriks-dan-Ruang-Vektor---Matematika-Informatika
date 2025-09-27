# Judul : Studi Kasus Masyarakat Sekitar Kampus - Analisis Matriks
# Repo : Matriks-dan-Ruang-Vektor
# Oleh : hafizhhasyhari
# Tanggal : 14 September 2023

import numpy as np

# Data jumlah penduduk dan rumah tangga di 3 wilayah sekitar kampus
# Baris 1: Jumlah penduduk
# Baris 2: Jumlah rumah tangga
# Kolom 1: Wilayah 1
# Kolom 2: Wilayah 2
# Kolom 3: Wilayah 3

data = np.array([[5000, 3000, 4500],   # Penduduk
                 [1200, 800, 950]])     # Rumah tangga

print("Data Masyarakat Sekitar Kampus:\n", data)

# Asumsikan kita ingin menghitung total penduduk dan rumah tangga
total = np.sum(data, axis=1)
print("Total Penduduk di Ketiga Wilayah:", total[0])
print("Total Rumah Tangga di Ketiga Wilayah:", total[1])

# Misalnya, kita ingin mengetahui proporsi penduduk dan rumah tangga di setiap wilayah
proporsi = data / total.reshape(2,1)
print("Proporsi Penduduk dan Rumah Tangga di Setiap Wilayah:\n", proporsi)

# Operasi lain: Menghitung rasio penduduk terhadap rumah tangga di setiap wilayah
rasio = data[0] / data[1]
print("Rasio Penduduk terhadap Rumah Tangga di Setiap Wilayah:", rasio)

# END
