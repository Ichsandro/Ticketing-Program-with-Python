# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F06 – Pencarian Wahana berfungsi untuk mencari wahana
# Kamus
# Batasan_umur, Batasan_tinggi : Character
# IsEmpty : Boolean

def cari():
    Batasan_umur = input("Batasan umur pemain: ")
    while (Batasan_umur != '1') and (Batasan_umur != '2') and (Batasan_umur != '3'):
        print ("Batasan umur tidak valid! ")
        Batasan_umur = input("Batasan umur pemain: ")

    Batasan_tinggi = input("Batasan tinggi badan: ")
    while (Batasan_tinggi != '1') and (Batasan_tinggi != '2'):
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

