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
