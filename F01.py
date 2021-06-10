# Nama/NIM : Muhammad Ichsandro D Noor/16519402
# Deskripsi Program:
# F01 – Load file berfungsi untuk menginput file dan membaca file serta
# memindahkan isi file kedalam array masing-masing

import csv

def load_user():
    user = [None for i in range(1000)]
    file = input("Masukkan nama File User: ")
    file_user = open(file, 'r')
    read_user = csv.reader(file_user, delimiter=',')
    i = 0
    for row in read_user:
        user[i] = row
        i += 1
    return user

def load_wahana():
    wahana = [None for i in range(1000)]
    file = input("Masukkan nama File Daftar Wahana: ")
    file_wahana = open(file, 'r')
    read_wahana = csv.reader(file_wahana, delimiter=',')
    i = 0
    for row in read_wahana:
        wahana[i] = row
        i += 1
    return wahana

def load_pembelian():
    pembelian = [None for i in range(1000)]
    file = input("Masukkan nama File Pembelian Tiket: ")
    file_pembelian = open(file, 'r')
    read_pembelian = csv.reader(file_pembelian, delimiter=',')
    i = 0
    for row in read_pembelian:
        pembelian[i] = row
        i += 1
    return pembelian

def load_penggunaan():
    penggunaan = [None for i in range(1000)]
    file = input("Masukkan nama File Penggunaan Tiket: ")
    file_penggunaan = open(file, 'r')
    read_penggunaan = csv.reader(file_penggunaan, delimiter=',')
    i = 0
    for row in read_penggunaan:
        penggunaan[i] = row
        i += 1
    return penggunaan

def load_tiket():
    tiket = [None for i in range(1000)]
    file = input("Masukkan nama File Kepemilikan Tiket: ")
    file_tiket = open(file, 'r')
    read_tiket = csv.reader(file_tiket, delimiter=',')
    i = 0
    for row in read_tiket:
        tiket[i] = row
        i += 1
    return tiket

def load_refund():
    refund = [None for i in range(1000)]
    file = input("Masukkan nama File Refund Tiket: ")
    file_refund = open(file, 'r')
    read_refund = csv.reader(file_refund, delimiter=',')
    i = 0
    for row in read_refund:
        refund[i] = row
        i += 1
    return refund

def load_kritiksaran():
    kritiksaran = [None for i in range(1000)]
    file = input("Masukkan nama File Kritik dan Saran: ")
    file_kritiksaran = open(file, 'r')
    read_kritiksaran = csv.reader(file_kritiksaran, delimiter=',')
    i = 0
    for row in read_kritiksaran:
        kritiksaran[i] = row
        i += 1
    return kritiksaran

def load_hilang():
    hilang = [None for i in range(1000)]
    file = input("Masukkan nama File Laporan Kehilangan Tiket: ")
    file_hilang = open(file, 'r')
    read_hilang = csv.reader(file_hilang, delimiter=',')
    i = 0
    for row in read_hilang:
        hilang[i] = row
        i += 1
    return hilang

user = load_user()
wahana = load_wahana()
pembelian = load_pembelian()
penggunaan = load_penggunaan()
tiket = load_tiket()
refund = load_refund()
kritiksaran = load_kritiksaran()
hilang = load_hilang()
print ("File perusahaan Willy Wangky’s Chocolate Factory telah di-load.")

