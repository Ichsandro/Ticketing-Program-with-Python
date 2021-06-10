# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F09-Refund User berfungsi untuk melakukan login pemain atau admin
# Kamus
# Username, Password : String
# IsValid : Boolean

def refund():
    if (logged_in[5] != "Admin"):
        ID_Wahana = input("Masukkan ID wahana: ")
        Refund_Tiket = int(input("Jumlah tiket yang di-refund: "))
        Tanggal_Refund = input("Masukkan tanggal hari ini: ")
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
        Jumlah_Tiket = 0
        IsFound = False
        j = 1
        while (not(IsFound)):
            if (tiket[j][0] == logged_in[3]):
                Jumlah_Tiket = int(tiket[j][2])
                IsFound = True
            else:
                j += 1
                if (tiket[j] == None):
                    break
        if (Jumlah_Tiket >= Refund_Tiket):
            Harga_Refund = int((Harga_Tiket*50/100)*Refund_Tiket)
            Jumlah_Tiket = Jumlah_Tiket - Refund_Tiket
            tiket[j][2] = str(Jumlah_Tiket)
            Saldo = int(logged_in[6])
            Saldo = Saldo + Harga_Refund
            logged_in[6] = str(Saldo)
            IsKosong = False
            f = 1
            while (not(IsKosong)):
                if refund[f] == None:
                    refund[f] = [Username, Tanggal_Refund, ID_Wahana, Refund_Tiket]
                    IsKosong = True
                else:
                    f += 1
            print("Uang refund sudah kami berikan pada akun Anda.")
        else:
            print("Anda tidak memiliki tiket terkait.")
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
