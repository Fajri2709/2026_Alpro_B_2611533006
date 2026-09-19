print("=== SISTEM TRANSAKSI TOKO ===")

nama_3006 = input("Masukkan Nama Pelanggan : ")
status_3006 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_3006 = float(input("Masukkan Total Belanja : Rp"))
jumlah_barang_3006 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3006 = input("Masukkan Kode Promo : ").upper()

syarat_belanja_3006 = total_belanja_3006 >= 200000
syarat_barang_3006 = jumlah_barang_3006 >= 3
status_member_3006 = status_3006 == "member"

daftar_promo_3006 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

promo_tersedia_3006 = kode_promo_3006 in daftar_promo_3006
promo_tidak_tersedia_3006 = kode_promo_3006 not in daftar_promo_3006

diskon_member_3006 = status_member_3006 and syarat_belanja_3006

promo_didapatkan_3006 = promo_tersedia_3006 and (syarat_belanja_3006 or syarat_barang_3006)

bukan_member_3006 = not status_member_3006

if diskon_member_3006:
    persentase_diskon_3006 = 0.10
else:
    persentase_diskon_3006 = 0.05 if syarat_belanja_3006 else 0

besar_diskon_3006 = total_belanja_3006 * persentase_diskon_3006

total_pembayaran_3006 = total_belanja_3006 - besar_diskon_3006

if jumlah_barang_3006 > 0:
    rata_rata_barang_3006 = total_belanja_3006 / jumlah_barang_3006
else:
    rata_rata_barang_3006 = 0

sisa_pembagian_3006 = int(total_belanja_3006) % jumlah_barang_3006 if jumlah_barang_3006 > 0 else 0


poin_3006 = 0
if status_member_3006:
    poin_3006 += int(total_pembayaran_3006 // 10000)

jumlah_barang_tersisa_3006 = jumlah_barang_3006
if promo_didapatkan_3006:
    jumlah_barang_tersisa_3006 -= 1

kode_1_3006 = ["HEMAT10"]
kode_2_3006 = ["HEMAT10"]

nilai_sama_3006 = kode_1_3006 == kode_2_3006
objek_sama_3006 = kode_1_3006 is kode_2_3006
objek_berbeda_3006 = kode_1_3006 is not kode_2_3006


kode_member_3006 = 1 if status_member_3006 else 0
kode_belanja_3006 = 2 if syarat_belanja_3006 else 0
kode_barang_3006 = 4 if syarat_barang_3006 else 0
kode_promo_3006 = 8 if promo_tersedia_3006 else 0

# Operator OR (|)
kode_status_3006 = (
    kode_member_3006
    | kode_belanja_3006
    | kode_barang_3006
    | kode_promo_3006
)

cek_member_3006 = kode_status_3006 & 1
cek_belanja_3006 = kode_status_3006 & 2
cek_barang_3006 = kode_status_3006 & 4
cek_promo_3006 = kode_status_3006 & 8

kode_referensi_3006 = 11
perbandingan_status_3006 = kode_status_3006 ^ kode_referensi_3006

kode_shift_3006 = kode_status_3006 << 1


member_access_3006 = bool(cek_member_3006)
promo_access_3006 = bool(cek_promo_3006)
free_shipping_access_3006 = syarat_belanja_3006 and syarat_barang_3006


print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_3006)
print("Status Pelanggan     :", status_3006)
print("Total Belanja        : Rp", total_belanja_3006)
print("Jumlah Barang        :", jumlah_barang_3006)
print("Kode Promo           :", kode_promo_3006)


print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_3006)
print("Jumlah Barang >= 3   :", syarat_barang_3006)
print("Status Member        :", status_member_3006)
print("Kode Promo Tersedia  :", promo_tersedia_3006)
print("Mendapatkan Diskon   :", diskon_member_3006)
print("Mendapatkan Promo    :", promo_didapatkan_3006)


print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon      : Rp", besar_diskon_3006)
print("Total Pembayaran     : Rp", total_pembayaran_3006)
print("Rata-rata Harga      : Rp", rata_rata_barang_3006)
print("Sisa Pembagian       :", sisa_pembagian_3006)


print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", format(kode_status_3006, "04b"))
print("Member Access        :", member_access_3006)
print("Promo Access         :", promo_access_3006)
print("Free Shipping Access :", free_shipping_access_3006)
print("Poin Pelanggan       :", poin_3006)


print("\n=== OPERATOR IDENTITAS ===")
print("kode_1 == kode_2     :", nilai_sama_3006)
print("kode_1 is kode_2     :", objek_sama_3006)
print("kode_1 is not kode_2 :", objek_berbeda_3006)


print("\n=== OPERASI BITWISE ===")
print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner           :", format(kode_status_3006, "04b"))
print("Kode Desimal         :", kode_status_3006)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_3006, "04b"), "& 0001")
print("Hasil Biner         :", format(cek_member_3006, "04b"))
print("Hasil Desimal       :", cek_member_3006)

print("\nCek Belanja")
print(format(kode_status_3006, "04b"), "& 0010")
print("Hasil Biner         :", format(cek_belanja_3006, "04b"))
print("Hasil Desimal       :", cek_belanja_3006)

print("\nCek Jumlah Barang")
print(format(kode_status_3006, "04b"), "& 0100")
print("Hasil Biner         :", format(cek_barang_3006, "04b"))
print("Hasil Desimal       :", cek_barang_3006)

print("\nCek Promo")
print(format(kode_status_3006, "04b"), "& 1000")
print("Hasil Biner         :", format(cek_promo_3006, "04b"))
print("Hasil Desimal       :", cek_promo_3006)

print("\n=== PERBANDINGAN STATUS (XOR) ===")
print("Kode Transaksi      :", format(kode_status_3006, "04b"))
print("Kode Referensi      :", format(kode_referensi_3006, "04b"))
print(format(kode_status_3006, "04b"), "^",
      format(kode_referensi_3006, "04b"))
print("Hasil Biner         :", format(perbandingan_status_3006, "04b"))
print("Hasil Desimal       :", perbandingan_status_3006)

print("\n=== SHIFT ===")
print(format(kode_status_3006, "04b"), "<< 1")
print("Hasil Biner         :", format(kode_shift_3006, "b"))
print("Hasil Desimal       :", kode_shift_3006)

print("\n=== SELESAI ===")