# NIM/Nama Pembuat  : 16519092/Rafidika Samekto
# Deskripsi         : F07 - Pembelian Tiket. Pembelian tiket yang dilakukakn oleh user

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
            if (int(logged_in[3]) <= 170): # mengecek tinggi badan user
                syarat()
            else: # tinggi badan user di atas 170 cm
                if (wahana_pakai[3] == "1"): # untuk batasan umur wahana kurang dari 17 tahun
                    if (umur >= 17):
                        syarat()
                    else:
                        harga_total = int(wahana_pakai[2]) * c
                        if (logged_in[5] == "Gold"):
                            harga_total = harga_total * 0.5
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
                        else:
                            no_saldo()
                elif (wahana_pakai[3] == "2"): # untuk batasan umur wahana lebih dari sama dengan 17 tahun
                    if (umur < 17):
                        syarat()
                    else:
                        harga_total = int(wahana_pakai[2]) * c
                        if (logged_in[5] == "Gold"):
                            harga_total = harga_total * 0.5
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
                        else:
                            no_saldo()
                else: # untuk semua umur
                    harga_total = int(wahana_pakai[2]) * c
                    if (logged_in[5] == "Gold"):
                        harga_total = harga_total * 0.5
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
                    else:
                        no_saldo()
        else: # untuk wahana tanpa batasan tinggi badan
            if (wahana_pakai[3] == "1"): # untuk batasan umur wahana kurang dari 17 tahun
                    if (umur >= 17):
                        syarat()
                    else:
                        harga_total = int(wahana_pakai[2]) * c
                        if (logged_in[5] == "Gold"):
                            harga_total = harga_total * 0.5
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
                        else:
                            no_saldo()
            elif (wahana_pakai[3] == "2"): # untuk batasan umur wahana lebih dari sama dengan 17 tahun
                if (umur < 17):
                    syarat()
                else:
                    harga_total = int(wahana_pakai[2]) * c
                    if (logged_in[5] == "Gold"):
                        harga_total = harga_total * 0.5
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
                    else:
                        no_saldo()
            else: # untuk semua umur
                harga_total = int(wahana_pakai[2]) * c
                if (logged_in[5] == "Gold"):
                    harga_total = harga_total * 0.5
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
                else:
                    no_saldo()
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
