# Buat file dengan nama Konstanta_NIM.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit terakhir nim contoh: jari_1234

from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3006 = float(input('Masukkan nilai jari-jari: '))
luas_3006 = PI * jari_3006 * jari_3006
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3006, luas_3006))