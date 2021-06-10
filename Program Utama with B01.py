# Source Code Program Utama
# WILLY WANGKY

# Kelompok 11 K-02 IF1210
# Anggota:  Rafidika Samekto (16519092)
#           Dhimas Adi Nur Fauzi (16519222)
#           Muhammad Ichsandro D Noor (16519402)
#           Jason (16519432)

# Deskripsi : Program adalah gabungan fungsi-fungsi yang akan digunakan untuk
#             membuat sebuah sistem permainan wahana

# KAMUS GLOBAL
# variabel user menyimpan data user.csv dalam bentuk array of array of string
# variabel wahana menyimpan data wahana.csv dalam bentuk array of array of string
# variabel pembelian menyimpan data pembelian.csv dalam bentuk array of array of string
# variabel penggunaan menyimpan data penggunaan.csv dalam bentuk array of array of string
# variabel tiket menyimpan data tiket.csv dalam bentuk array of array of string
# variabel refund menyimpan data refund.csv dalam bentuk array of array of string
# variabel kritiksaran menyimpan data kritiksaran.csv dalam bentuk array of array of string
# variabel hilang menyimpan data hilang.csv dalam bentuk array of array of string
# variabel logged_in menyimpan data user yang login saat itu dalam bentuk array of array of string
# fungsi pilihan melakukan penampilan pilihan kode yang bisa user masukkan
# variabel permainan menerima input berupa kode pilihan user

# ALGORITMA PROGRAM UTAMA

# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F01 – Load file berfungsi untuk menginput file dan membaca file serta
# memindahkan isi file kedalam array masing-masing
# Kamus
# user, wahana, pembelian, penggunaan, tiket, refund, kritiksaran, hilang : array of tuple
import csv

def load_user():
    user = [None for i in range(1000)]
    file = input("Masukkan nama File User: ")
    file_user = open(file, 'r')
    read_user = csv.reader(file_user, delimiter=',')
    i = 0
    for row in read_user:
        user[i] = row
        i += 1
    return user

def load_wahana():
    wahana = [None for i in range(1000)]
    file = input("Masukkan nama File Daftar Wahana: ")
    file_wahana = open(file, 'r')
    read_wahana = csv.reader(file_wahana, delimiter=',')
    i = 0
    for row in read_wahana:
        wahana[i] = row
        i += 1
    return wahana

def load_pembelian():
    pembelian = [None for i in range(1000)]
    file = input("Masukkan nama File Pembelian Tiket: ")
    file_pembelian = open(file, 'r')
    read_pembelian = csv.reader(file_pembelian, delimiter=',')
    i = 0
    for row in read_pembelian:
        pembelian[i] = row
        i += 1
    return pembelian

def load_penggunaan():
    penggunaan = [None for i in range(1000)]
    file = input("Masukkan nama File Penggunaan Tiket: ")
    file_penggunaan = open(file, 'r')
    read_penggunaan = csv.reader(file_penggunaan, delimiter=',')
    i = 0
    for row in read_penggunaan:
        penggunaan[i] = row
        i += 1
    return penggunaan

def load_tiket():
    tiket = [None for i in range(1000)]
    file = input("Masukkan nama File Kepemilikan Tiket: ")
    file_tiket = open(file, 'r')
    read_tiket = csv.reader(file_tiket, delimiter=',')
    i = 0
    for row in read_tiket:
        tiket[i] = row
        i += 1
    return tiket

def load_refund():
    refund = [None for i in range(1000)]
    file = input("Masukkan nama File Refund Tiket: ")
    file_refund = open(file, 'r')
    read_refund = csv.reader(file_refund, delimiter=',')
    i = 0
    for row in read_refund:
        refund[i] = row
        i += 1
    return refund

def load_kritiksaran():
    kritiksaran = [None for i in range(1000)]
    file = input("Masukkan nama File Kritik dan Saran: ")
    file_kritiksaran = open(file, 'r')
    read_kritiksaran = csv.reader(file_kritiksaran, delimiter=',')
    i = 0
    for row in read_kritiksaran:
        kritiksaran[i] = row
        i += 1
    return kritiksaran

def load_hilang():
    hilang = [None for i in range(1000)]
    file = input("Masukkan nama File Laporan Kehilangan Tiket: ")
    file_hilang = open(file, 'r')
    read_hilang = csv.reader(file_hilang, delimiter=',')
    i = 0
    for row in read_hilang:
        hilang[i] = row
        i += 1
    return hilang

user = load_user()
wahana = load_wahana()
pembelian = load_pembelian()
penggunaan = load_penggunaan()
tiket = load_tiket()
refund = load_refund()
kritiksaran = load_kritiksaran()
hilang = load_hilang()
print ("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")

# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F04-Login User berfungsi untuk melakukan login pemain atau admin
# Kamus
# Username, Password : String
# IsValid : Boolean

logged_in = None

def login():
    if (logged_in == None):
        Username = input("Masukkan username: ") # Memasukkan username dan password
        Password = input("Masukkan password: ")

        # NIM/Nama  : 16519222/Dhimas Adi Nur Fauzi
        # Deskripsi :
        # B01 - Penyimpanan password berfungsi untuk hashing password user
        # Kamus
        # Password = String

        import hashlib, binascii, os
        def hash_password(Password):
            # melakukan hash pada passwword untuk disimpan
            salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            passwordhash = hashlib.pbkdf2_hmac('sha512', Password.encode('utf-8'), salt, 100000)
            passwordhash = binascii.hexlify(passwordhash)
            return (salt + passwordhash).decode('ascii')

        stored_password = hash_password(Password)
        print("Password terenkripsi Anda: ", stored_password)

        IsValid = False
        i = 1
        while (not(IsValid)):
            if (user[i][3] == Username) and (user[i][4] == Password): # Mengecek apakah username dan password sesuai
                IsValid = True
            else:
                i += 1
                if user[i] == None:
                    break
        if (IsValid):
            print ("Selamat bersenang-senang, "+ user[i][0]+"!")
            return user[i]
        else:
            print ("Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!")
            return None
    else:
        print("Tidak dapat melakukan Login karena sudah ada yang Login")

# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F02 – Save file berfungsi untuk menyimpan array ke dalam file dalam format csv

def save_user():
    file = input("Masukkan nama File User: ") # Memasukkan file untuk menyimpan data
    file_user = open(file, 'w', newline='') # Membuka file untuk di tulis ulang
    write_user = csv.writer(file_user, delimiter=',')
    i = 0
    while (user[i] != None): # Selama ada data didalam array of tuple, data akan disimpan ke dalam file
        write_user.writerow(user[i])
        i += 1
    return file_user

def save_wahana():
    file = input("Masukkan nama File Daftar Wahana: ")
    file_wahana = open(file, 'w', newline='')
    write_wahana = csv.writer(file_wahana, delimiter=',')
    i = 0
    while (wahana[i] != None):
        write_wahana.writerow(wahana[i])
        i += 1
    return file_wahana

def save_pembelian():
    file = input("Masukkan nama File Pembelian Tiket: ")
    file_pembelian = open(file, 'w', newline='')
    write_pembelian = csv.writer(file_pembelian, delimiter=',')
    i = 0
    while (pembelian[i] != None):
        write_pembelian.writerow(pembelian[i])
        i += 1
    return file_pembelian

def save_penggunaan():
    file = input("Masukkan nama File Penggunaan Tiket: ")
    file_penggunaan = open(file, 'w', newline='')
    write_penggunaan = csv.writer(file_penggunaan, delimiter=',')
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
    write_kritiksaran = csv.writer(file_kritiksaran, delimiter=',')
    i = 0
    while (kritiksaran[i] != None):
        write_kritiksaran.writerow(kritiksaran[i])
        i += 1
    return file_kritiksaran

def save_hilang():
    file = input("Masukkan nama File Laporan Kehilangan Tiket: ")
    file_hilang = open(file, 'w', newline='')
    write_hilang = csv.writer(file_hilang, delimiter=',')
    i = 0
    while (hilang[i] != None):
        write_hilang.writerow(hilang[i])
        i += 1
    return file_hilang


# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F03 - Sign Up. Program melakukan pendaftaran (sign up) pemain baru

# Kamus
# nama adalah nama pemain baru
# birth adalah tanggal lahir pemain baru
# tinggi adalah tinggi badan pemain baru
# username adalah username pemain baru
# password adalah kata sandi username yang akan didaftarkan
# role adalah status user saat itu. secara otomatis memiliki role pemain reguler
# saldo adalah sisa saldo yang dimiliki pemain baru, dalam hal ini, 0.

# Algoritma
def signup():
    if (logged_in[5] == "Admin"): # fungsi ini hanya boleh dilakukan oleh Admin
        nama = input("Masukkan nama pemain: ")
        birth = input("Masukkan tanggal lahir pemain (DD/MM/YYYY): ")
        tinggi = input("Masukkan tinggi badan pemain (cm): ")
        username = input("Masukkan username pemain: ")
        i = 1
        while (i < 1000): # proses ini mengecek apakah username masukan sama dengan yang sudah ada di file
            if (user[i] == None):
                break
            elif (user[i][3] == username):
                print("Username tidak tersedia! Silakan masukkan username lain")
                username = input("Masukkan username pemain: ")
                i = 1
            else:
                i += 1
        password = input("Masukkan password pemain: ")

        # NIM/Nama  : 16519222/Dhimas Adi Nur Fauzi
        # Deskripsi :
        # B01 - Penyimpanan password berfungsi untuk hashing password user
        # Kamus
        # Password = String

        import hashlib, binascii, os
        def hash_password(password):
            # melakukan hash pada passwword untuk disimpan
            salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            passwordhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
            passwordhash = binascii.hexlify(passwordhash)
            return (salt + passwordhash).decode('ascii')

        stored_password = hash_password(password)
        print("Password terenkripsi Anda: ", stored_password)

        role = "Pemain_Reguler"
        saldo = "0"
        user_baru = [nama, birth, tinggi, username, password, role, saldo]
        # proses selanjutnya adalah memasukkan data ke array user
        for i in range(1000):
            if (user[i] == None):
                user[i] = user_baru
                break
    else:
        print("Anda tidak diperkenankan menggunakan fungsi ini!")

# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F05 - Pencarian Pemain berfungsi untuk admin dapat mencari data diri dari pemain wahana. Jika username tidak ditemukan, tampilkan pesan kalau pemain tidak ditemukan.
# Kamus
# pemain : array of character
# Username : string
# IsValid : boolean
# i : integer

def cari_pemain():
    if (logged_in[5] == 'Admin'):
        Username = input('Masukkan username: ')
        IsValid = False
        i = 1
        while (not(IsValid)):
            if (user[i][3] == Username):
                IsValid = True
                break
            else:
                i += 1
                if (user[i] == None):
                    break
        if (IsValid):
            print('Nama Pemain: ' + user[i][0])
            print('Tinggi Pemain: ' + user[i][2])
            print('Tanggal Lahir Pemain: ' + user[i][1])
        else:
            print('Tidak ditemukan username ' + Username)
    else:
        print('Anda tidak diperkenankan menjalankan fungsi ini!')

# Nama/NIM : Dhimas Adi Nur Fauzi/16519222
# Deskripsi Program:
# F06 – Pencarian Wahana berfungsi untuk mencari wahana bedasarkan batasan umur dan tinggi pemain
# Kamus
# Batasan_umur, Batasan_tinggi : Character
# IsEmpty, IsFound : Boolean

def cari():
    print ('''Jenis batasan umur:
1. Anak-anak (<17 tahun)
2. Dewasa (>=17 tahun)
3. Semua umur
Jenis batasan tinggi badan:
1. Lebih dari 170 cm
2. Tanpa batasan''')

    Batasan_umur = input("Batasan umur pemain: ") # Menginput batas umur
    while (Batasan_umur != '1') and (Batasan_umur != '2') and (Batasan_umur != '3'): # Melakukan validasi input yang sesuai
        print ("Batasan umur tidak valid! ")
        Batasan_umur = input("Batasan umur pemain: ")

    Batasan_tinggi = input("Batasan tinggi badan: ") # Menginput batas umur
    while (Batasan_tinggi != '1') and (Batasan_tinggi != '2'): # Melakukan validasi input yang sesuai
        print ("Batasan tinggi badan tidak valid! ")
        Batasan_tinggi = input("Batasan tinggi badan: ")

    i = 1
    IsEmpty = False
    IsFound = False
    print("Hasil Pencarian:")
    while (not (IsEmpty)):
        if (wahana[i] == None):
            IsEmpty = True
        elif (Batasan_umur == wahana[i][3]):
            if (Batasan_tinggi == wahana[i][4]):
                print(wahana[i][0] + ' | ' + wahana[i][1] + ' | ' + wahana[i][2])
                IsFound = True
                i += 1
            else:
                i += 1
        else:
            i += 1
    if (not(IsFound)):
        print("Tidak ada wahana yang sesuai dengan pencarian kamu.")

# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F07 - Pembelian Tiket. Pembelian tiket yang dilakukan oleh user

# Kamus
# a adalah input ID wahana yang ingin dibeli tiketnya
# b adalah input tanggal pembelian tiket
# c adalah jumlah tiket yang dibeli

# Algoritma
def beli_tiket():
    if (logged_in[5] != "Admin"):
        a = input("Masukkan ID Wahana: ")
        b = input("Masukkan tanggal hari ini (DD/MM/YYYY): ")
        c = int(input("Jumlah tiket yang dibeli: "))
        wahana_pakai = [] # data wahana yang akan dibeli tiketnya
        for i in range(1,1000):
            if (wahana[i][0] == a):
                wahana_pakai = wahana[i]
                break
        day = int(b[0:2]) # hari pada tanggal hari ini
        month = int(b[3:5]) # bulan pada tanggal hari ini
        year = int(b[6:10]) # tahun pada tanggal hari ini
        x = logged_in[1] # menggunakan data user yang login
        day_birth = int(x[0:2]) # hari lahir user
        month_birth = int(x[3:5]) # bulan lahir user
        year_birth = int(x[6:10]) # tahun lahir user
        umur = year - year_birth # umur user saat membeli tiket
        if (month_birth > month):
            umur = umur - 1
        elif (month_birth == month):
            if (day_birth > day):
                umur = umur - 1
        # kondisi month_birth < month tidak perlu ditulis karena hasilnya
        # sama saja dengan variabel umur
        def syarat(): # diberikan jika user tidak memenuhi persyaratan wahana yang akan dibeli tiketnya
            print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
            print("Silakan menggunakan wahana lain yang tersedia.")
        def no_saldo(): # diberikan jika user tidak memiliki cukup saldo untuk membeli sejumlah tiket wahana
            print("Saldo Anda tidak cukup")
            print("Silakan mengisi saldo Anda")
        if (wahana_pakai[4] == "1"): # untuk batasan tinggi badan wahana lebih dari 170 cm
            if (int(logged_in[2]) <= 170): # mengecek tinggi badan user
                syarat()
            else: # tinggi badan user di atas 170 cm
                if (wahana_pakai[3] == "1"): # untuk batasan umur wahana kurang dari 17 tahun
                    if (umur >= 17):
                        syarat()
                    else:
                        harga_total = int(wahana_pakai[2]) * c
                        if (logged_in[5] == "Gold"):
                            harga_total = int(harga_total * 0.5)
                        sisa = int(logged_in[6]) # sisa saldo user
                        if (sisa >= harga_total):
                            sisa -= harga_total
                            logged_in[6] = str(sisa)
                            print("")
                            print("Selamat bersenang-senang di " + wahana_pakai[1] + ".")
                            # proses selanjutnya adalah menyimpan data di atas ke file pembelian dan kepemilikan tiket
                            data_beli = [logged_in[3], b, a, str(c)]
                            pemilik = [logged_in[3], a, str(c)]
                            for i in range(1,1000):
                                if (pembelian[i] == None):
                                    pembelian[i] = data_beli
                                    break
                            for i in range(1,1000):
                                if (tiket[i] == None):
                                    tiket[i] = pemilik
                                    break
                                elif (logged_in[3] == tiket[i][0]) and (tiket[i][1] == a):
                                    tiket_total = int(tiket[i][2])
                                    tiket_total += c
                                    tiket[i][2] = str(tiket_total)
                                    break
                        else:
                            no_saldo()
                elif (wahana_pakai[3] == "2"): # untuk batasan umur wahana lebih dari sama dengan 17 tahun
                    if (umur < 17):
                        syarat()
                    else:
                        harga_total = int(wahana_pakai[2]) * c
                        if (logged_in[5] == "Gold"):
                            harga_total = int(harga_total * 0.5)
                        sisa = int(logged_in[6]) # sisa saldo user
                        if (sisa >= harga_total):
                            sisa -= harga_total
                            logged_in[6] = str(sisa)
                            print("")
                            print("Selamat bersenang-senang di " + wahana_pakai[1] + ".")
                            # proses selanjutnya adalah menyimpan data di atas ke file pembelian dan kepemilikan tiket
                            data_beli = [logged_in[3], b, a, str(c)]
                            pemilik = [logged_in[3], a, str(c)]
                            for i in range(1,1000):
                                if (pembelian[i] == None):
                                    pembelian[i] = data_beli
                                    break
                            for i in range(1,1000):
                                if (tiket[i] == None):
                                    tiket[i] = pemilik
                                    break
                                elif (logged_in[3] == tiket[i][0]) and (tiket[i][1] == a):
                                    tiket_total = int(tiket[i][2])
                                    tiket_total += c
                                    tiket[i][2] = str(tiket_total)
                                    break
                        else:
                            no_saldo()
                else: # untuk semua umur
                    harga_total = int(wahana_pakai[2]) * c
                    if (logged_in[5] == "Gold"):
                        harga_total = int(harga_total * 0.5)
                    sisa = int(logged_in[6]) # sisa saldo user
                    if (sisa >= harga_total):
                        sisa -= harga_total
                        logged_in[6] = str(sisa)
                        print("")
                        print("Selamat bersenang-senang di " + wahana_pakai[1] + ".")
                        # proses selanjutnya adalah menyimpan data di atas ke file pembelian dan kepemilikan tiket
                        data_beli = [logged_in[3], b, a, str(c)]
                        pemilik = [logged_in[3], a, str(c)]
                        for i in range(1,1000):
                            if (pembelian[i] == None):
                                pembelian[i] = data_beli
                                break
                        for i in range(1,1000):
                            if (tiket[i] == None):
                                tiket[i] = pemilik
                                break
                            elif (logged_in[3] == tiket[i][0]) and (tiket[i][1] == a):
                                tiket_total = int(tiket[i][2])
                                tiket_total += c
                                tiket[i][2] = str(tiket_total)
                                break
                    else:
                        no_saldo()
        else: # untuk wahana tanpa batasan tinggi badan
            if (wahana_pakai[3] == "1"): # untuk batasan umur wahana kurang dari 17 tahun
                    if (umur >= 17):
                        syarat()
                    else:
                        harga_total = int(wahana_pakai[2]) * c
                        if (logged_in[5] == "Gold"):
                            harga_total = int(harga_total * 0.5)
                        sisa = int(logged_in[6]) # sisa saldo user
                        if (sisa >= harga_total):
                            sisa -= harga_total
                            logged_in[6] = str(sisa)
                            print("")
                            print("Selamat bersenang-senang di " + wahana_pakai[1] + ".")
                            # proses selanjutnya adalah menyimpan data di atas ke file pembelian dan kepemilikan tiket
                            data_beli = [logged_in[3], b, a, str(c)]
                            pemilik = [logged_in[3], a, str(c)]
                            for i in range(1,1000):
                                if (pembelian[i] == None):
                                    pembelian[i] = data_beli
                                    break
                            for i in range(1,1000):
                                if (tiket[i] == None):
                                    tiket[i] = pemilik
                                    break
                                elif (logged_in[3] == tiket[i][0]) and (tiket[i][1] == a):
                                    tiket_total = int(tiket[i][2])
                                    tiket_total += c
                                    tiket[i][2] = str(tiket_total)
                                    break
                        else:
                            no_saldo()
            elif (wahana_pakai[3] == "2"): # untuk batasan umur wahana lebih dari sama dengan 17 tahun
                if (umur < 17):
                    syarat()
                else:
                    harga_total = int(wahana_pakai[2]) * c
                    if (logged_in[5] == "Gold"):
                        harga_total = int(harga_total * 0.5)
                    sisa = int(logged_in[6]) # sisa saldo user
                    if (sisa >= harga_total):
                        sisa -= harga_total
                        logged_in[6] = str(sisa)
                        print("")
                        print("Selamat bersenang-senang di " + wahana_pakai[1] + ".")
                        # proses selanjutnya adalah menyimpan data di atas ke file pembelian dan kepemilikan tiket
                        data_beli = [logged_in[3], b, a, str(c)]
                        pemilik = [logged_in[3], a, str(c)]
                        for i in range(1,1000):
                            if (pembelian[i] == None):
                                pembelian[i] = data_beli
                                break
                        for i in range(1,1000):
                            if (tiket[i] == None):
                                tiket[i] = pemilik
                                break
                            elif (logged_in[3] == tiket[i][0]) and (tiket[i][1] == a):
                                tiket_total = int(tiket[i][2])
                                tiket_total += c
                                tiket[i][2] = str(tiket_total)
                                break
                    else:
                        no_saldo()
            else: # untuk semua umur
                harga_total = int(wahana_pakai[2]) * c
                if (logged_in[5] == "Gold"):
                    harga_total = int(harga_total * 0.5)
                sisa = int(logged_in[6]) # sisa saldo user
                if (sisa >= harga_total):
                    sisa -= harga_total
                    logged_in[6] = str(sisa)
                    print("")
                    print("Selamat bersenang-senang di " + wahana_pakai[1] + ".")
                    # proses selanjutnya adalah menyimpan data di atas ke file pembelian dan kepemilikan tiket
                    data_beli = [logged_in[3], b, a, str(c)]
                    pemilik = [logged_in[3], a, str(c)]
                    for i in range(1,1000):
                        if (pembelian[i] == None):
                            pembelian[i] = data_beli
                            break
                    for i in range(1,1000):
                        if (tiket[i] == None):
                            tiket[i] = pemilik
                            break
                        elif (logged_in[3] == tiket[i][0]) and (tiket[i][1] == a):
                            tiket_total = int(tiket[i][2])
                            tiket_total += c
                            tiket[i][2] = str(tiket_total)
                            break
                else:
                    no_saldo()
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# Nama/NIM : Dhimas Adi Nur Fauzi/16519222
# Deskripsi Program:
# F08- Menggunakan Tiket berfungsi untuk pemain dapat menggunakan tiket untuk bermain.
# Kamus
# Idwahana, Tanggal : string
# JmlTiket : integer
# IsValid : boolean
# data : array of string

def main():
    if (logged_in[5] != "Admin"):
        Idwahana = input('Masukkan ID wahana: ')
        Tanggal = input('Masukkan tanggal hari ini: ')
        JmlTiket = int(input('Jumlah tiket yang digunakan: '))

        IsValid = False
        i = 1
        while (not(IsValid)):
            if (tiket[i] == None):
                break
            elif (tiket[i][1] == Idwahana) and (int(tiket[i][2]) >= JmlTiket):
                IsValid = True
                sisa_tiket = int(tiket[i][2])
                sisa_tiket = sisa_tiket - JmlTiket
                tiket[i][2] = str(sisa_tiket)
            else:
                i += 1
                if (tiket[i] == None):
                    break

        if (IsValid):
            print('Terima kasih telah bermain.')
        else:
            print('Tiket Anda tidak valid dalam sistem kami.')
        # proses selanjutnya adalah menyatat penggunaan tiket ke array penggunaan
        data = [logged_in[3], Tanggal, Idwahana, str(JmlTiket)]
        for i in range(1000):
            if (penggunaan[i] == None):
                penggunaan[i] = data
                break
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini")

# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F09-Refund User berfungsi untuk melakukan refund tiket pemain dan mengembalikan saldo pemain
# sebanyak tiket yang direfund dan dipotong 50 % dari harga tiketnya.
# Kamus
# Username, ID_Wahana, Tanggal_Refund : String
# Refund_tiket, Harga_Tiket, Harga_Refund, Jumlah_TIket, Saldo : Integer
# IsFound, IsEmpty : Boolean

def refund_tiket():
    if (logged_in[5] != "Admin"):
        Username = logged_in[3]
        ID_Wahana = input("Masukkan ID wahana: ")
        Refund_Tiket = int(input("Jumlah tiket yang di-refund: "))
        Tanggal_Refund = input("Masukkan tanggal refund: ")
        # Mencari harga tiket sesuai ID wahana yang diinput
        Harga_Tiket = 0
        IsFound = False
        i = 1
        while (not(IsFound)):
            if (wahana[i][0] == ID_Wahana):
                Harga_Tiket = int(wahana[i][2])
                IsFound = True
            else:
                i += 1
                if (wahana[i] == None):
                    break
        # Mencari jumlah tiket yang dimiliki pemain
        Jumlah_Tiket = 0
        IsFound = False
        j = 1
        while (not(IsFound)):
            if (tiket[j][0] == Username):
                Jumlah_Tiket = int(tiket[j][2])
                IsFound = True
            else:
                j += 1
                if (tiket[j] == None):
                    break
        if (Jumlah_Tiket >= Refund_Tiket): # Mengecek apakah pemain memiliki tiket terkait
            Harga_Refund = int((Harga_Tiket*50/100)*Refund_Tiket) # harga refund 50% harga tiket awalnya
            Jumlah_Tiket = Jumlah_Tiket - Refund_Tiket # Mengurangi jumlah tiket pemain sebanyak yang direfund
            tiket[j][2] = str(Jumlah_Tiket)
            Saldo = int(logged_in[6])
            Saldo = Saldo + Harga_Refund
            logged_in[6] = str(Saldo)
            IsEmpty = False
            k = 1
            while (not(IsEmpty)): # memasukkan data kedalam array of tuple
                if refund[k] == None:
                    refund[k] = [Username, Tanggal_Refund, ID_Wahana, Refund_Tiket]
                    IsEmpty = True
                else:
                    k += 1
            print("Uang refund sudah kami berikan pada akun Anda.")
        else:
            print("Anda tidak memiliki tiket terkait.")
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F10 - Kritik dan saran berfungsi untuk menanyakan user apakah data ingin disimpan atau tidak dan mengeluarkan user.
# Kamus
# kritik : array of string
# Idwahana, Tanggal, InputKritik : string
# IsValid : boolean

def kritik_saran():
    if (logged_in[5] != "Admin"):
        Idwahana = input('Masukkan ID Wahana: ')
        Tanggal = input('Masukkan tanggal pelaporan: ')
        InputKritik = input('Kritik/saran Anda: ')

        IsValid = False
        i = 1
        while (not(IsValid)):
            if (kritiksaran[i] == None):
                IsValid = True
                kritik = [logged_in[3], Tanggal, Idwahana, InputKritik]
                kritiksaran[i] = kritik
            else:
                i += 1
        print('Kritik dan saran Anda kami terima')
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F11 - Melihat Kritik Saran digunakan untuk melihat kritik dan saran yang masuk

# Kamus
# i integer
# Algoritma
def lihat_laporan():
    if (logged_in[5] == "Admin"):
        for i in range(1,1000):
            if (kritiksaran[i] == None):
                if (i == 1): # jika tidak ada data di baris pertama atau file kosong
                    print("Tidak ada kritik dan saran")
                break
            else:
                print("Kritik dan saran: ")
                print(kritiksaran[i][2]+" | "+kritiksaran[i][1]+" | "+kritiksaran[i][0]+" | "+kritiksaran[i][3])
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
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
        print("Info wahana telah ditambahkan!")
        # Asumsi semua input valid
        wahana_baru = [ID_baru, nama, harga, umur, tinggi]
        for i in range(1000):
            if (wahana[i] == None):
                wahana[i] = wahana_baru
                break
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F13 - Top Up Saldo berfungsi agar admin dapat menambahkan saldo terhadap seorang pemain
# Kamus

def topup():
    if (logged_in[5] == "Admin"):
        Username = input('Masukkan username: ')
        Saldo_topup = int(input('Masukkan saldo yang di-top up: '))
        IsValid = False
        i = 1
        while (not(IsValid)):
            if (user[i][3] == Username):
                IsValid = True
                saldo = int(user[i][6])
                saldo = saldo + Saldo_topup
                user[i][6] = str(saldo)
            else:
                i += 1
                if (user[i] == None):
                    break
        if (IsValid):
            print('Top up berhasil. Saldo ' + user[i][0] + ' bertambah menjadi ' + user[i][6])
        else:
            print('Username tidak ditemukan silakan coba lagi.')
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# Nama/NIM          : Dhimas Adi Nur Fauzi/16519222
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

# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F15 – Melihat Jumlah Tiket Pemain berfungsi untuk melihat jumlah tiket yang dimiliki pemain
# Kamus
# Username_pemain : String
# i,j : Integer
# IsEmpty : Boolean

def tiket_pemain():
    if (logged_in[5] == "Admin"):
        Username_pemain = input("Masukkan username: ") # Menginput username pemain
        i = 1
        j = 1
        IsEmpty = False
        print ("Riwayat:")
        while(not(IsEmpty)): # Mencari semua riwayat pemain selama array tidak kosong
            if (tiket[i] == None):
                IsEmpty = True
            elif (Username_pemain == tiket[i][0]): # mengecek apakah username ada didalam data kepemilikan tiket
                if (tiket[i][1] == wahana[j][0]): # mencari nama wahana sesuai ID_Wahana pada tiket yang dimiliki pemain
                    print (tiket[i][1]+' | '+wahana[j][1]+' | '+tiket[i][2])
                    i += 1
                else:
                    j += 1
            else:
                i += 1
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F16- Exit berfungsi untuk menanyakan user apakah data ingin disimpan atau tidak dan mengeluarkan user.
# Kamus
# simpan adalah input untuk mengonfirmasi user untuk melakukan penyimpanan
# data terakhir atau tidak

def keluar():
    simpan = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)?: ')
    if (simpan == 'Y'):
        for i in range(1000): # balikin data login user ke array user
            if(user[i][3] == logged_in[3]):
                user[i] = logged_in
                break
        file_user = save_user()
        file_wahana = save_wahana()
        file_pembelian = save_pembelian()
        file_penggunaan = save_penggunaan()
        file_tiket = save_tiket()
        file_refund = save_refund()
        file_kritiksaran = save_kritiksaran()
        file_hilang = save_hilang()

        file_user.close()
        file_wahana.close()
        file_pembelian.close()
        file_penggunaan.close()
        file_tiket.close()
        file_refund.close()
        file_kritiksaran.close()
        file_hilang.close()
        print ("Data berhasil disimpan!")
    else:
        print('Data tidak disimpan')

    print("SAMPAI JUMPA KEMBALI DI WAHANA PERMAINAN WILLY WANGKY CHOCOLATE FACTORY")

# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# B02 – Golden Account berfungsi untuk melakukan upgrade account pemain oleh admin dengan biaya 100000
# pemilik golden account dapat membeli tiket wahana dengan setengah harga normalnya
# Kamus
# biaya_upgrade, Saldo_pemain : Integer
# Username_upgrade : String
# IsFound : Boolean

def upgrade_gold():
    if (logged_in[5] == "Admin"):
        biaya_upgrade = 100000
        Username_upgrade = input("Masukkan username yang ingin di-upgrade: ")
        # Mengecek saldo yang dimiliki pemain
        Saldo_pemain = 0
        IsFound = False
        i = 1
        while (not (IsFound)):
            if (user[i][3] == Username_upgrade):
                Saldo_pemain = int(user[i][6])
                IsFound = True
            else:
                i += 1
                if user[i] == None:
                    break
        if (Saldo_pemain >= biaya_upgrade): # Upgrade hanya bisa dilakukan jika saldo pemain cukup
            Saldo_pemain = Saldo_pemain - biaya_upgrade
            user[i][6] = str(Saldo_pemain)
            user[i][5] = 'Gold'
            print ("Akun Anda telah diupgrade.")
        else:
            print ("Saldo pemain tidak cukup untuk melakukan upgrade.")
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")

# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : B03 - Best Wahana. Program mencari 3 wahana terbaik berdasarkan hasil penjualan tiket

# Kamus
# best_wahana adalah array of array of string
# jumlah_tiket adalah jumlah tiket terjual per wahana

# Algoritma
def best_wahana():
    best_wahana = [None for i in range(1000)]
    jumlah_tiket = 0
    for i in range(1,1000): # loop dari file wahana
        if (wahana[i] == None):
            break
        else:
            for j in range(1,1000): # loop dari file pembelian
                if (pembelian[j] == None):
                    break
                elif (pembelian[j][2] == wahana[i][0]): # jika ID wahana sama
                    jumlah_tiket += int(pembelian[j][3]) # menambah jumlah tiket terjual untuk setiap wahana
        best_wahana[i] = [wahana[i][0], wahana[i][1], str(jumlah_tiket)]
        jumlah_tiket = 0 
    # proses selanjutnya adalah mengurutkan best_wahana berdasarkan jumlah tiket terjual
    for i in range(1,1000):
        if (best_wahana[i] == None):
            break
        else:
            terlaku = best_wahana[i]
            index_maks = i
            for j in range(i+1,1000):
                if (best_wahana[j] == None):
                    break
                else:
                    if ((int(terlaku[2]) < int(best_wahana[j][2]))):
                        terlaku = best_wahana[j]
                        index_maks = j
            if (index_maks != i):
                x = best_wahana[i]
                best_wahana[i] = best_wahana[index_maks]
                best_wahana[index_maks] = x
    # proses selanjutnya adalah menampilkan hasilnya ke layar
    for i in range(1,1000):
        print(str(i) + " | " + best_wahana[i][0] + " | " + best_wahana[i][1] + " | " + best_wahana[i][2])
        if (i == 3):
            break

# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : B04 - Laporan Kehilangan Tiket. Program berfungsi membuat laporan kehilangan tiket

# Kamus
# username adalah username pemain yang kehilangan tiket
# tanggal adalah tanggal pemain kehilangan tiket
# ID adalah ID wahana yang tercantum dalam tiket pemain yang hilang
# tiket adalah jumlah tiket yang hilang

# Algoritma
def tiket_hilang():
    if (logged_in[5] != "Admin"):
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
                tiket_ada = int(tiket[i][2])
                tiket_ada -= int(tiket_hilang)
                tiket[i][2] = str(tiket_ada)
                break
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
# Prosedur ini menyambut user yang akan bermain di wahana Willy Wangky
print("""
    === SELAMAT DATANG DI WAHANA PERMAINAN WILLY WANGKY CHOCOLATE FACTORY ===

=== DISINI KALIAN AKAN BERSENANG-SENANG SEMBARI MELARIKAN DIRI DARI DUNIA NYATA ===

=== BERMAINLAH SEPUASNYA KARENA WAHANA INI TIDAK TUTUP APABILA ANDA TIDAK PUAS! ===
""")

while (logged_in == None): # program akan meminta user untuk login
    logged_in = login()

def pilihan():
    print("""

=== PILIH FUNGSI DI BAWAH INI UNTUK MEMULAI PERJALANANMU! ===

        === MASUKKAN 3 -------> SAVE FILE                         ===
        === MASUKKAN 4 -------> SIGN UP                           ===
        === MASUKKAN 5 -------> PENCARIAN PEMAIN                  ===
        === MASUKKAN 6 -------> PENCARIAN WAHANA                  ===
        === MASUKKAN 7 -------> PEMBELIAN TIKET                   ===
        === MASUKKAN 8 -------> PENGGUNAAN TIKET                  ===
        === MASUKKAN 9 -------> REFUND TIKET                      ===
        === MASUKKAN 10 ------> MEMASUKKAN KRITIK DAN SARAN       ===
        === MASUKKAN 11 ------> MELIHAT KRITIK DAN SARAN          ===
        === MASUKKAN 12 ------> MENAMBAH WAHANA BARU              ===
        === MASUKKAN 13 ------> MELAKUKAN TOP UP SALDO            ===
        === MASUKKAN 14 ------> MELIHAT RIWAYAT PENGGUNAAN WAHANA ===
        === MASUKKAN 15 ------> MELIHAT JUMLAH TIKET              ===
        === MASUKKAN 16 ------> KELUAR DAN LOG OUT                ===
        === MASUKKAN B2 ------> UPGRADE AKUN                      ===
        === MASUKKAN B3 ------> MELIHAT 3 WAHANA TERBAIK          ===
        === MASUKKAN B4 ------> MELAPORKAN KEHILANGAN TIKET       ===
        
    """)

pilihan()
permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
while (permainan != "16"):
    if (permainan == "3"):
        save_user()
        save_wahana()
        save_pembelian()
        save_penggunaan()
        save_tiket()
        save_refund()
        save_kritiksaran()
        save_hilang()
        print ("Data berhasil disimpan!")
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "4"):
        signup()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "5"):
        cari_pemain()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "6"):
        cari()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "7"):
        beli_tiket()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "8"):
        main()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "9"):
        refund_tiket()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "10"):
        kritik_saran()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "11"):
        lihat_laporan()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "12"):
        tambah_wahana()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "13"):
        topup()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "14"):
        riwayat_wahana()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "15"):
        tiket_pemain()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "B2"):
        upgrade_gold()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "B3"):
        best_wahana()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    elif (permainan == "B4"):
        tiket_hilang()
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
    else:
        print("MASUKKAN TIDAK VALID. SILAKAN ULANGIN LAGI!")
        pilihan()
        permainan = input("SILAKAN MASUKKAN SALAH SATU KODE/NOMOR DI ATAS: ")
keluar()
