# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# B02 – Golden Account berfungsi untuk melakukan login pemain atau admin
# Kamus
# Username, Password : String
# IsFound : Boolean

def upgrade_gold():
    if (logged_in[5] == "Admin"):
        biaya_upgrade = 100000
        Username_upgrade = input("Masukkan username yang ingin di-upgrade: ")
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
        if (Saldo_pemain >= biaya_upgrade):
            Saldo_pemain = Saldo_pemain - biaya_upgrade
            user[i][6] = str(Saldo_pemain)
            user[i][5] = 'Gold'
            print ("Akun Anda telah diupgrade.")
        else:
            print ("Saldo pemain tidak cukup untuk melakukan upgrade.")
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
