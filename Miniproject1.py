#Nama = Muhammad Ilyasa' 'Izzuddin
#Kelas = A
#NIM = 2409116033
#Mini Project 1 (NIM Ganjil)

print("Masukkan Nama, NIM, Kelas: ")

#Masukkan Nama
Nama = str(input("Masukkan Nama = ")) 

#Masukkan Kelas
Kelas = str(input("Masukkan Kelas = ")) 

#Masukkan NIM
while True:
    NIM = (input("Masukkan NIM = ")) 
    if NIM.isdigit():
        break
    else:
        print("Masukkan angka yang benar")

print("\nSelamat datang", Nama)

def hitung_gaji(): #Mendefinisikan sebuah fungsi
    tarif_kerja = int(input(" Masukkan tarif kerja = ")) #Masukkan Tarif kerja
    jam_kerja = int(input(" Masukkan jam kerja = ")) #Masukkan Jam kerja

    total_gaji = jam_kerja * tarif_kerja

    if jam_kerja > 160: #Jika jam kerja lebih dari 160 jam
        print("mendapatkan bonus 10%") #Maka mendapatkan bonus
        bonus_gaji = total_gaji * 0.1 #Tarif kerja dikali dengan 10%
        bonus_gaji += total_gaji 
        print(bonus_gaji)
    else: #Sebuah pengecualian jika jam kerja dibawah 160 jam
        print("Tidak ada bonus.")

while True: #Ketika memilih Benar atau Ya
    hitung_gaji() #Menghitung ke awal yaitu menghitung bonus gaji
    # Tanya pengguna apakah ingin menghitung lagi
    lagi = input("Apakah Anda ingin menghitung gaji lagi? (ya/tidak): ").strip().lower()
    if lagi != 'ya': #Jika menjawab selain ya atau menjawab tidak 
        print("Terima kasih! Program selesai.")
        break #Program akan langsung selesai
