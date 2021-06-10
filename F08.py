# Nama/NIM : Jason/16519432
# Deskripsi Program:
# F08- Menggunakan Tiket berfungsi untuk pemain dapat menggunakan tiket untuk bermain.
# Kamus
# Idwahana, Tanggal : string
# JmlTiket : integer
# IsValid : boolean
# data : array of string

def main():
        if (logged_in[5] != "Admin"):
                Idwahana = input('Masukkan ID wahana: ')
                Tanggal = input('Masukkan tanggal hari ini: ')
                JmlTiket = int(input('Jumlah tiket yang digunakan: '))

                IsValid = False
                i = 1
                while (not(IsValid)):
                        if (tiket[i][1] == Idwahana) and (int(tiket[i][2]) >= JmlTiket) :
                                IsValid = True
                                sisa_tiket = int(tiket[i][2])
                                sisa_tiket = sisa_tiket - JmlTiket
                                tiket[i][2] = str(sisa_tiket)
                        else:
                                i += 1
                        if (user[i] == None):
                                break

                if (IsValid):
                        print('Terima kasih telah bermain.')
                else:
                        print('Tiket Anda tidak valid dalam sistem kami.')
                # proses selanjutnya adalah menyatat penggunaan tiket ke array penggunaan
                data = [logged_in[3], Tanggal, Idwahana, str(JmlTiket)]
                for i in range(1000):
                        if (penggunaan[i] == None):
                                penggunaan[i] = data
                                break
        else:
                print("Anda tidak diperkenankan menjalankan fungsi ini")
