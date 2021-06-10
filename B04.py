# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : program berfungsi membuat laporan kehilangan tiket

# Kamus
# username adalah username pemain yang kehilangan tiket
# tanggal adalah tanggal pemain kehilangan tiket
# ID adalah ID wahana yang tercantum dalam tiket pemain yang hilang
# tiket adalah jumlah tiket yang hilang

# Algoritma
def tiket_hilang():
    # asumsi masukan username, ID dan jumlah tiket valid
    username = input("Masukkan username: ")
    tanggal = input("Tanggal kehilangan tiket (DD/MM/YYYY): ")
    ID = input("ID Wahana: ")
    tiket_hilang = input("Jumlah tiket yang dihilangkan: ")
    data_hilang = [username, tanggal, ID, tiket_hilang]
    # data_hilang dimasukkan ke array hilang
    for i in range(1000):
        if (hilang[i] == None):
            hilang[i] = data_hilang
            break
    print("Laporan kehilangan tiket Anda telah direkam")
    # proses selanjutnya adalah mengurangi jumlah tiket pemain
    for i in range(1,1000):
        if (tiket[i][0] == username) and (tiket[i][1] == ID):
            tiket = int(tiket[i][2])
            tiket -= tiket_hilang
            tiket[i][2] = str(tiket)
            break
    
