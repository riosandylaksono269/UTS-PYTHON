# Program Jadwal Kuliah Harian

def jadwal_hari(hari):
    jadwal = {
        "Senin": ["Algoritma", "Struktur Data"],
        "Selasa": ["Basis Data", "Jaringan Komputer"],
        "Rabu": ["Kewirausahaan", "Pemrograman Web"],
        "Kamis": ["Pemrograman Python", "Praktikum"],
        "Jumat": ["Sistem Operasi", "Etika Profesi"]
    }

    # Mengubah input menjadi format huruf besar di awal (misal: senin -> Senin)
    hari = hari.capitalize()

    # Mengecek apakah hari ada dalam jadwal
    if hari in jadwal:
        print(f"\n📅 Jadwal hari {hari}:")
        for mata_kuliah in jadwal[hari]:
            print(f"- {mata_kuliah}")
    else:
        print("\n❌ Tidak ada jadwal pada hari tersebut.")

# Program utama
print("=== Program Jadwal Kuliah Harian ===")
input_hari = input("Masukkan nama hari: ")
jadwal_hari(input_hari)
