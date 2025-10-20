# Program Koperasi - Menentukan Kategori Setoran Mingguan

a = int(input("Masukkan setoran 1: "))
b = int(input("Masukkan setoran 2: "))
c = int(input("Masukkan setoran 3: "))
#Program meminta pengguna memasukkan tiga jumlah setoran mingguan.

if a <= 0 or b <= 0 or c <= 0:
    print("Input tidak valid!") #Mengecek validasi input.
else:
    total = a + b + c
    print("Total setoran:", total) #Kalau semua input valid, maka dihitung total setoran mingguannya.

    if total < 300000:
        print("Kategori: Rendah")
    elif total < 600000:
        print("Kategori: Sedang")
    else:
        print("Kategori: Tinggi")
