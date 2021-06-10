# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F02 – Save file berfungsi untuk menyimpan array ke dalam file

def save_user():
    file = input("Masukkan nama File User: ")
    file_user = open(file, 'w', newline='')
    write_user = csv.writer(file_user, delimiter=',')
    i = 0
    while (user[i] != None):
        write_user.writerow(user[i])
        i += 1
    return file_user

def save_wahana():
    file = input("Masukkan nama File Daftar Wahana: ")
    file_wahana = open(file, 'w', newline='')
    write_wahana = csv.reader(file_wahana, delimiter=',')
    i = 0
    while (wahana[i] != None):
        write_wahana.writerow(wahana[i])
        i += 1
    return file_wahana

def save_pembelian():
    file = input("Masukkan nama File Pembelian Tiket: ")
    file_pembelian = open(file, 'w', newline='')
    write_pembelian = csv.reader(file_pembelian, delimiter=',')
    i = 0
    while (pembelian[i] != None):
        write_pembelian.writerow(pembelian[i])
        i += 1
    return file_pembelian

def save_penggunaan():
    file = input("Masukkan nama File Penggunaan Tiket: ")
    file_penggunaan = open(file, 'w', newline='')
    write_penggunaan = csv.reader(file_penggunaan, delimiter=',')
    i = 0
    while (penggunaan[i] != None):
        write_penggunaan.writerow(penggunaan[i])
        i += 1
    return file_penggunaan

def save_tiket():
    file = input("Masukkan nama File Kepemilikan Tiket: ")
    file_tiket = open(file, 'w', newline='')
    write_tiket = csv.writer(file_tiket, delimiter=',')
    i = 0
    while (tiket[i] != None):
        write_tiket.writerow(tiket[i])
        i += 1
    return file_tiket

def save_refund():
    file = input("Masukkan nama File Refund Tiket: ")
    file_refund = open(file, 'w', newline='')
    write_refund = csv.writer(file_refund, delimiter=',')
    i = 0
    while (refund[i] != None):
        write_refund.writerow(refund[i])
        i += 1
    return file_refund

def save_kritiksaran():
    file = input("Masukkan nama File Kritik dan Saran: ")
    file_kritiksaran = open(file, 'w', newline='')
    write_kritiksaran = csv.reader(file_kritiksaran, delimiter=',')
    i = 0
    while (kritiksaran[i] != None):
        write_kritiksaran.writerow(kritiksaran[i])
        i += 1
    return file_kritiksaran

def save_hilang():
    file = input("Masukkan nama File Laporan Kehilangan Tiket: ")
    file_hilang = open(file, 'w', newline='')
    write_hilang = csv.reader(file_hilang, delimiter=',')
    i = 0
    while (hilang[i] != None):
        write_hilang.writerow(hilang[i])
        i += 1
    return file_kritiksaran

file_user = save_user()
file_wahana = save_wahana()
file_pembelian = save_pembelian()
file_penggunaan = save_penggunaan()
file_tiket = save_tiket()
file_refund = save_refund()
file_kritiksaran = save_kritiksaran()
file_hilang = save_hilang()
print ("Data berhasil disimpan!")
