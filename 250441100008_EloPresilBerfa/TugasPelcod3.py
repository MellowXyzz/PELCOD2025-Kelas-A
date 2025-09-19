print("="*50)
print("Nama : Elo Presil Berfa")
print("NIM  : 250441100008")
print("="*50)

# Soalnya
# 3. Kamu ingin pergi liburan dg sepeda motor, total jarak perjalanan XXX KM (ganti XXX dg 3 angka terakhir NIM), konsumsi BBM sepeda motor 2.7 KM per Liter, kapasitas tangki sepeda motor X Liter (ganti X dg 1 angka terakhir NIM), harga bensin per liter Rp.1XXXO (ganti XXX dg 3 angka terakhir NIM)

# jika total bensin yg dibutuhkan > 3 liter, maka dapat diskon Rp.500 per liter, berapa total bensin yg dibutuhkan, harga bensin per liter setelah diskon (jika ada), total biaya bensin, dan prakiraan berapa kali kamu harus mengisi bensin (dengan asumsi tangki penuh setiap kali isi)?

# NB: HARUS PAKAI INPUT !!!!!

# Jawabannya

bensinnya = 2.7

jarak = int(input("Masukkan jarak perjalanan yang ditempuh (KM): "))
tangki = int(input("Masukkan kapasitas tangki motor (Liter): "))
harga = int(input("Masukkan harga bensin per liter (Rp): "))

total_bensin = jarak / bensinnya  # pembagian biasa
print("Total bensin yang dibutuhkan adalah", round(total_bensin, 2), "liter")

if total_bensin > 3:
    diskon = 500
else:
    diskon = 0

harga_diskon = harga - diskon

biaya_perjalanan = total_bensin * harga_diskon
print("Harga bensin per liter setelah diskon: Rp", harga_diskon)
print("Total biaya bensin: Rp", round(biaya_perjalanan, 2))

# Pembulatan ke atas tanpa math.ceil
if total_bensin % tangki == 0:
    isi_ulang = int(total_bensin / tangki)
else:
    isi_ulang = int(total_bensin / tangki) + 1

print("Jumlah isi ulang bensin yang dibutuhkan:", isi_ulang, "kali")