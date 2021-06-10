# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F15 – Melihat Jumlah Tiket Pemain berfungsi untuk melihat jumlah tiket yang dimiliki pemain
# Kamus
# Username : String
# i,j : Integer
# IsEmpty : Boolean

def tiket_pemain():
    if (logged_in[5] == "Admin"):
        Username_pemain = input("Masukkan username: ")
        i = 1
        j = 1
        IsEmpty = False
        print ("Riwayat:")
        while(not(IsEmpty)):
            if (tiket[i] == None):
                IsEmpty = True
            elif (Username_pemain == tiket[i][0]):
                if (tiket[i][1] == wahana[j][0]):
                    print (tiket[i][1]+' | '+wahana[j][1]+' | '+tiket[i][2])
                    i += 1
                else:
                    j += 1
            else:
                i += 1
    else:
        print("Anda tidak diperkenankan menjalankan fungsi ini!")
