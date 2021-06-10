# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F11 - Melihat Kritik Saran digunakan untuk melihat kritik dan saran yang masuk

# Kamus

# Algoritma
def lihat_laporan():
    for i in range(1,1000):
        if (kritiksaran[i] == None):
            if (i == 1): # jika tidak ada data di baris pertama atau file kosong
                print("Tidak ada kritik dan saran")
            break
        else:
            print("Kritik dan saran: ")
            print(kritiksaran[i][2]+" | "+kritiksaran[i][1]+" | "+kritiksaran[i][0]+" | "+kritiksaran[i][3])
        
