# Buat file dengan nama arimatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_3006 = int(input("input angka-1: "))
angka2_3006 = int(input("input angka-2: "))

# Penjumlahan
hasil_3006 = angka1_3006 + angka2_3006
print("\nOperator Penjumlahan")
print("Hasil =", hasil_3006)

# Pengurangan
hasil_3006 = angka1_3006 - angka2_3006
print("\nOperator Pengurangan")
print("Hasil =", hasil_3006)

# Perkalian
hasil_3006 = angka1_3006 * angka2_3006
print("\nOperator Perkalian")
print("Hasil =", hasil_3006)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_3006 != 0:
    hasil_3006 = angka1_3006 / angka2_3006
    print("\nOperator Pembagian")
    print("Hasil =", hasil_3006)

    hasil_3006 = angka1_3006 // angka2_3006
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_3006)

    hasil_3006 = angka1_3006 % angka2_3006
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_3006)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_3006 = angka1_3006 ** angka2_3006
print("\nOperator Pangkat")
print("Hasil =", hasil_3006)