import os

#Color Warna
P_Putih = '\x1b[1;97m'
H_Hijau = '\x1b[1;92m'

# Variabel untuk menyimpan total jumlah data
total = 0

# Minta pengguna untuk memasukkan nama file
os.system("clear")
print(f"{P_Putih} * contoh /sdcard/file.txt")
file_name = input("[?] masukkan lokasi file: ")

# Buka file yang dimasukkan pengguna dan baca setiap baris
with open(file_name, 'r') as file:
    lines = file.readlines()

# Tampilkan pilihan menu
print("\npilih opsi:")
print("1. sortir id")
print("2. sortir password")
print("3. sortir cookies")
print("4. sortir uid dan password")
print("5. sortir uid, password, dan cookies")

# Minta pengguna untuk memilih opsi
option = input("\n[?] masukkan nomor opsi: ")
print("")

# Sortir data sesuai dengan opsi yang dipilih dan tambahkan ke total
for idx, line in enumerate(lines):
    data = line.split('|')
    user_id = data[0].strip()
    password = data[1].strip()
    cookies = data[2].strip()

    if option == "1":
        print(f" - {H_Hijau}{user_id}{P_Putih}")
    elif option == "2":
        print(f" - {H_Hijau}{password}{P_Putih}")
    elif option == "3":
        print(f" - {H_Hijau}{cookies}{P_Putih}")
    elif option == "4":
        print(f" - {H_Hijau}{user_id}|{password}{P_Putih}")
    elif option == "5":
        print(f" - {H_Hijau}{user_id}|{password}|{cookies}{P_Putih}")

    # Tambahkan ke total setelah membaca setiap baris
    total += 1

# Tampilkan total jumlah data
print(f"\nTotal Jumlah Data: {total}\n")
