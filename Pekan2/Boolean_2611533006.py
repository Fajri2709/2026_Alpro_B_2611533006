# Buat file dengan nama Boolean_NIM.py
# Nama variable ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_3006 = True
is_cumlaude_3006 = True

# Menggunakan Boolean
nilai_3006 = 85
batas_lulus_3006 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_3006 = nilai_3006 >= batas_lulus_3006 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai:", nilai_3006)
print("Apakah Lulus?:", status_kelulusan_3006)
if is_lulus_3006 and is_cumlaude_3006:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")