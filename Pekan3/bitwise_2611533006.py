# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("\n==================================")
print("3. OPERATOR BITWISE")
print("==================================")

angka1_3006 = int(input("Masukkan angka bitwise-1: "))
angka2_3006 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner:")
print("Angka 1:", angka1_3006, "-| biner", bin(angka1_3006))
print("Angka 2:", angka2_3006, "-| biner", bin(angka2_3006))

# Bitwise AND
hasil_3006 = angka1_3006 & angka2_3006
print("\nBitwise AND (&)")
print(angka1_3006, "&", angka2_3006, "=", hasil_3006)
print("Biner hasil =", bin(hasil_3006))
print("Biner hasil (8 bit) =", format(hasil_3006, '08b'))

# Bitwise OR
hasil_3006 = angka1_3006 | angka2_3006
print("\nBitwise OR (|)")
print(angka1_3006, "|", angka2_3006, "=", hasil_3006)
print("Biner hasil =", bin(hasil_3006))
print("Biner hasil (8 bit) =", format(hasil_3006, '08b'))

# Bitwise XOR
hasil_3006 = angka1_3006 ^ angka2_3006
print("\nBitwise XOR (^)")
print(angka1_3006, "^", angka2_3006, "=", hasil_3006)
print("Biner hasil =", bin(hasil_3006))
print("Biner hasil (8 bit) =", format(hasil_3006, '08b'))

# Bitwise NOT
hasil_3006 = ~angka1_3006
print("\nBitwise NOT (~)")
print("~", angka1_3006, "=", hasil_3006)
print("Biner hasil =", bin(hasil_3006))
print("Biner hasil (8 bit) =", format(hasil_3006, '08b'))

# Bitwise geser kiri
jumlah_geser_3006 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_3006 = angka1_3006 << jumlah_geser_3006
print("\nBitwise Geser Kiri (<<)")
print(angka1_3006, "<<", jumlah_geser_3006, "=", hasil_3006)
print("Biner hasil =", bin(hasil_3006))
print("Biner hasil (8 bit) =", format(hasil_3006, '08b'))

# Bitwise geser kanan
hasil_3006 = angka1_3006 >> jumlah_geser_3006
print("\nBitwise Geser Kanan (>>)")
print(angka1_3006, ">>", jumlah_geser_3006, "=", hasil_3006)
print("Biner hasil =", bin(hasil_3006))
print("Biner hasil (8 bit) =", format(hasil_3006, '08b'))