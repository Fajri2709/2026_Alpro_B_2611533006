# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_3006 = int(input("Input angka-1: "))
angka2_3006 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3006)
print("Nilai angka2 =", angka2_3006)

# Assignment biasa
hasil_3006 = angka1_3006
print("\nAssignment biasa (=)")
print("Hasil =", hasil_3006)

# Assignment penambahan
hasil_3006 = angka1_3006
hasil_3006 += angka2_3006
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_3006)

# Assignment pengurangan
hasil_3006 = angka1_3006
hasil_3006 -= angka2_3006
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_3006)

# Assignment perkalian
hasil_3006 = angka1_3006
hasil_3006 *= angka2_3006
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_3006)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3006 != 0:
    hasil_3006 = angka1_3006
    hasil_3006 /= angka2_3006
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_3006)
    
    # Operator tambahan
    hasil_3006 = angka1_3006
    hasil_3006 //= angka2_3006
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_3006)
    
    hasil_3006 = angka1_3006
    hasil_3006 %= angka2_3006
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_3006)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_3006 = angka1_3006
hasil_3006 **= angka2_3006
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_3006)