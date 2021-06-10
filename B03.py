# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : program mencari wahana terbaik berdasarkan hasil penjualan tiket

# Kamus
# best_wahana adalah array of array of string
# jumlah_tiket adalah jumlah tiket terjual per wahana

# Algoritma
def best_wahana():
    best_wahana = [None for i in range(1000)]
    jumlah_tiket = 0
    for i in range(1000): # loop dari file wahana
        if (wahana[i] == None):
            break
        else:
            for j in range(1,1000): # loop dari file pembelian
                if (pembelian[j][2] == wahana[i][0]): # jika ID wahana sama
                    jumlah_tiket += int(pembelian[j][3]) # menambah jumlah tiket terjual untuk setiap wahana
                elif (pembelian[j] == None):
                    break
        best_wahana[i] = [wahana[i][0], wahana[i][1], jumlah_tiket]
        jumlah_tiket = 0 
    # proses selanjutnya adalah mengurutkan best_wahana berdasarkan jumlah tiket terjual
    for i in range(1000):
        if (best_wahana[i] == None):
            break
        else:
            terlaku = best_wahana[i]
            index_maks = i
            for j in range(i+1,1000):
                if (best_wahana[j] == None):
                    break
                else:
                    (int(terlaku[2]) < int(best_wahana[j][2])):
                    terlaku = best_wahana[j]
                    index_maks = j
            if (index_maks != i):
                x = best_wahana[i]
                best_wahana[i] = best_wahana[index_maks]
                best_wahana[index_maks] = x
    # proses selanjutnya adalah menampilkan hasilnya ke layar
    for i in range(1000):
        print(str(i+1) + " | " + best_wahana[i][0] + " | " + best_wahana[i][1] + " | " + best_wahana[i][2])
        if (i == 2):
            break
