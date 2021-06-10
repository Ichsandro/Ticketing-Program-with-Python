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
                if (Isvalid):
                        print('Nama Pemain: ' + user[i][0])
                        print('Tinggi Pemain: ' + user[i][2])
                        print('Tanggal Lahir Pemain: ' + user[i][1])
                else:
                        print('Tidak ditemukan username ' + Username)
        else:
                print('Anda tidak diperkenankan menjalankan fungsi ini!')
