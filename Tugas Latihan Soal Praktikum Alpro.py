#Latihan soal M9 Praktikum Algoritma dan Pemrograman
#Nomor 1
waktu=10
while waktu > 0 :
    print(f"Perulangan ke - {waktu}")
    waktu -=1
print("Selesai")

#Nomor 2
bilangan=2
while bilangan <=10:
    print(bilangan, end=" ")
    bilangan +=2

#Nomor 3
total_berat = 0  

while True:
    total_berat += 5  
    print(f"Total berat: {total_berat} kg")

    if total_berat >= 25:  
        break

#Nomor 4
password_rahasia = "statbis2026"

while True:
    tebakan = input("Masukkan password: ")

    if tebakan == password_rahasia:
        print("Login Berhasil, Selamat Datang!")
        break
    else:
        print("Password salah, silakan coba lagi!")
