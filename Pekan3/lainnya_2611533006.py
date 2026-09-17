# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan Identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_3006 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_3006 = [int(angka.strip()) for angka in input_data_3006.split(",")]

nilai_dicari_3006 = int(input("Masukkan angka yang ingin dicari: "))

# Operator In
hasil_3006 = nilai_dicari_3006 in data_3006
print("\nOperator keanggotaan IN")
print(nilai_dicari_3006, "in", data_3006, "=", hasil_3006)

# Operator Not In
hasil_3006 = nilai_dicari_3006 not in data_3006
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_3006, "not in", data_3006, "=", hasil_3006)

print("\n==================================")
print("2. OPERATOR IDENTITAS")
print("==================================")

# objek1 menggunakan list dari input pengguna
objek1_3006 = data_3006

# objek2 menggunakan list dari input pengguna
objek2_3006 = objek1_3006

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3006 = data_3006.copy()

print("objek1_3006 =", objek1_3006)
print("objek2_3006 =", objek2_3006)
print("objek3_3006 =", objek3_3006)

# Operator Is
hasil_3006 = objek1_3006 is objek2_3006
print("\nOperator identitas IS")
print("objek1_3006 is objek2_3006 =", hasil_3006)

# Operator Is Not
hasil_3006 = objek1_3006 is not objek3_3006
print("\nOperator identitas IS NOT")
print("objek1_3006 is not objek3_3006 =", hasil_3006)

# Membandingkan identitas dan nilai
print("\nMembandingkan identitas dan nilai:")
print("objek1_3006 is objek3_3006 =", objek1_3006 is objek3_3006)
print("objek1_3006 == objek3_3006 =", objek1_3006 == objek3_3006)