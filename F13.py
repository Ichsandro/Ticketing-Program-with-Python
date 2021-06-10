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
