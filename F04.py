# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F04-Login User berfungsi untuk melakukan login pemain atau admin
# Kamus
# Username, Password : String
# IsValid : Boolean

logged_in = None

def login():
    if (logged_in == None):
        Username = input("Masukkan username: ")
        Password = input("Masukkan password: ")
        IsValid = False
        i = 1
        while (not(IsValid)):
            if (user[i][3] == Username) and (user[i][4] == Password):
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

logged_in = login()
