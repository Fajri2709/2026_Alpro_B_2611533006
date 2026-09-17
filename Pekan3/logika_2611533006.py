# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memasukkan nilai booleam
# Input tidak peka terhadap huruf besar dan kecil
a1_3006 = input("Input nilai boolean-1 (true/false):").strip().lower() == "true"
a2_3006 = input("Input nilai boolean-2 (true/false):").strip().lower() == "true"

print("\nA1 =", a1_3006)
print("A2 =", a2_3006)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_3006 and a2_3006
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi: bernilai True jika salah satunya True
hasil_3006 = a1_3006 or a2_3006
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_3006)

# Negasi A1: membalik nilai A1
hasil_3006 = not a1_3006
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_3006)

# Negasi A2: membalik nilai A2
hasil_3006 = not a2_3006
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_3006)

# XOR: bernilai True jika kedua nilai berbeda
hasil_3006 = a1_3006 != a2_3006
print("\nDisjungsi EKsklusif (XOR)")
print("A1 XOR A2 =", hasil_3006)