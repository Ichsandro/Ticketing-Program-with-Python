# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F10 - Kritik dan saran berfungsi untuk menanyakan user apakah data ingin disimpan atau tidak dan mengeluarkan user.
# Kamus
# kritik : array of string
# Idwahana, Tanggal, InputKritik : string
# IsValid : boolean

def kritik_saran():
        if (logged_in[5] != "Admin"):
                Idwahana = input('Masukkan ID Wahana: ')
                Tanggal = input('Masukkan tanggal pelaporan: ')
                InputKritik = input('Kritik/saran Anda: ')

                IsValid = False
                i = 1
                while (not(IsValid)):
                        if (kritiksaran[i] == None):
                                IsValid = True
                                kritik = [logged_in[3], Tanggal, Idwahana, InputKritik]
                                kritiksaran[i] = kritik
                        else:
                                i += 1
                print('Kritik dan saran Anda kami terima')
        else:
                print("Anda tidak diperkenankan menjalankan fungsi ini!")
