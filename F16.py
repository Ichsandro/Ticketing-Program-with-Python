# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F16- Exit berfungsi untuk menanyakan user apakah data ingin disimpan atau tidak dan mengeluarkan user.
# Kamus
# simpan adalah input untuk mengonfirmasi user untuk melakukan penyimpanan
# data terakhir atau tidak

def exit():
    simpan = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N)?: ')
    if (simpan == 'Y'):
        for i in range(1000): # balikin data login user ke array user
            if(user[i][3] == logged_in[3]):
                user[i] = logged_in
                break
        logged_in = None
        file_user = save_user()
        file_wahana = save_wahana()
        file_pembelian = save_pembelian()
        file_penggunaan = save_penggunaan()
        file_tiket = save_tiket()
        file_refund = save_refund()
        file_kritiksaran = save_kritiksaran()
        file_hilang = save_hilang()
        print ("Data berhasil disimpan!")
    else :
        print('Data tidak disimpan')
    file_user.close()
    file_wahana.close()
    file_pembelian.close()
    file_penggunaan.close()
    file_tiket.close()
    file_refund.close()
    file_kritiksaran.close()
    file_hilang.close()
    print("SAMPAI JUMPA KEMBALI DI WAHANA PERMAINAN WILLY WANGKY CHOCOLATE FACTORY")
