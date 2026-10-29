#Tugas Latihan Soal M9 Algoritma dan Pemrograman Jax Christian NRP : 2043261049
#Nomor 1
nilai_kuis = [80, 75, 90, 65]
for nilai in nilai_kuis:
    nilai_baru= nilai+5
    print(f"Selamat nilai anda bertambah sebanyak {nilai_baru}")

#Nomor 2
for i in range(3,31,3):
    print(i, end=" ")

#Nomor 3
teks = "STATISTIKA BISNIS"
teks_baru=teks.lower()
for a in teks_baru:
    print(a)

#Nomor 4
peserta = ["Ijul", "Chlea", "Reza", "Citra", "Budi"]
for n in peserta:
    if n=="Reza": #Continue akan tidak melanjutkan Reza
        continue
    print(n)

#Nomor 5
departemen = ["Statbis", "Statistika", "Matematika"]
angkatan = [2025, 2026]
for x in departemen:
    for y in angkatan:
        print(f" Departemen : {x}, Angkatan : {y}")

#Nomor 6
pelamar = [("Budi", 3.2, 5), ("Siti", 3.6, 3), ("Dodi", 3.8, 1)]
for joko in pelamar:
    if joko[1]>=3.5 and joko[2]>2:
        print("Selamat anda diterima", joko[0])
    else:
        print("Anda ditolak", joko[0])

#Nomor 7
karyawan = [("Joko", "IT", 7000), ("Rina", "HR", 5000), ("Toni", "Data", 8000), ("Lia", "IT", 6500)]
total_gaji=0

for wowo,joko,mbg in karyawan:
    if joko=="IT" or joko=="Data":
        total_gaji +=mbg
    
print(f"Total gaji karyawan IT dan Data adalah ${total_gaji:,.2f}")

#Soal baru
for i in range(1,5):
    for j in range(1,5):
        print("*",end=" ")
    print("*")

#Nomor 8
penjualan = [("Kopi", 60, False), ("Teh", 30, False), ("Boba", 80, True)]
batas_laris=50
for minuman, jumlah, promo in penjualan:
    if jumlah > batas_laris and not promo:
        print(f"Selamat produk {minuman} laku keras dengan jumlah minuman sebanyak {jumlah}")
    elif promo and batas_laris < jumlah:
        print(f"Maaf produk {minuman}, belum laris tanpa adanya promo, silakan jual lagi!")
    else:
        print(f"Produk {minuman} masih belum laris, silakan buat inovasi lagi!") 


