# NIM/NamA Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F14 - Melihat Riwayat Penggunaan Wahana. Program berfungsi menampilkan riwayat penggunaan wahana

# Kamus
# ID adalah ID wahana yang ingin dilihat riwayat penggunaannya

# Algoritma
def riwayat_wahana():
    if (logged_in[5] == "Admin"):
        ID = input("Masukkan ID Wahana: ") # asumsi ID wahana valid
        print("Riwayat: ")
        for i in range(1,1000):
            if (penggunaan[i] == None):
                break
            elif (ID == penggunaan[i][2]):
                print(penggunaan[i][1] + " | " + penggunaan[i][0] + " | " + penggunaan[i][3])
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
