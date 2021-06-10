# NIM/Nama pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F12 - Menambah Wahana Baru.
#                     Program menanmbah wahana baru ke file

# Kamus
# ID_baru adalah ID wahana yang baru
# nama adalah nama wahana yang baru
# harga adalah harga tiket wahana baru
# umur adalah batasan umur wahana baru
# tinggi adalah batasan tinggi wahana baru

# Algoritma
def tambah_wahana():
    if (logged_in[5] == "Admin"):
        print("Masukkan Informasi Wahana yang ditambahkan: ")
        ID_baru = input("Masukkan ID Wahana: ")
        nama = input("Masukkan Nama Wahana: ")
        harga = input("Masukkan Harga Tiket: ")
        umur = input("Batasan umur: ")
        tinggi = input("Batasan tinggi badan: ")
        if (tinggi == "tanpa batasan"):
            tinggi = "2"
        elif (tinggi == "lebih dari 170 cm"):
            tinggi = "1"
        if (umur == "anak-anak"):
            umur = "1"
        elif (umur == "dewasa"):
            umur = "2"
        elif (umur == "semua umur"):
            umur = "3"
        # Asumsi semua input valid
        wahana_baru = [ID_baru, nama, harga, umur, tinggi]
        for i in range(1000):
            if (wahana[i] == None):
                wahana[i] = wahana_baru
                break
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
