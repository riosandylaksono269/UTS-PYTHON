def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung total ongkir berdasarkan kota, berat, dan opsi asuransi.
    """
    tarif_dasar = {
        "Solo": 10000,
        "Jakarta": 15000,
        "Surabaya": 12000
    }

    if kota not in tarif_dasar:
        return None  # menandakan kota tidak tersedia

    total = tarif_dasar[kota] + 2000 * berat_kg
    if asuransi:
        total += 3000
    return total


# ===============================
# Program utama
# ===============================
print("=== PROGRAM PERHITUNGAN ONGKIR ===")
print("Daftar kota: Solo, Jakarta, Surabaya")

# Input data pengguna
kota = input("Masukkan kota tujuan: ")
berat = float(input("Masukkan berat paket (kg): "))

# Pilihan asuransi
pilihan = input("Apakah ingin menggunakan asuransi? (y/n): ").lower()
pakai_asuransi = True if pilihan == "y" else False

# Hitung total
total_ongkir = hitung_ongkir(berat, kota, pakai_asuransi)

# Tampilkan hasil
print("\n=== STRUK ONGKIR ===")
if total_ongkir is None:
    print("Kota tidak tersedia dalam daftar.")
else:
    print(f"Kota Tujuan   : {kota}")
    print(f"Berat Paket   : {berat} kg")
    print(f"Asuransi      : {'Ya' if pakai_asuransi else 'Tidak'}")
    print(f"Total Ongkir  : Rp {total_ongkir:,.0f}")
print("=====================")
print("Terima kasih telah menggunakan layanan kami!")
