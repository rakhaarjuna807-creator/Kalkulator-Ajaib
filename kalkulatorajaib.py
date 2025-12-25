#kalkulator sederhana by juna 14/12/2025
import math

def tambah(x,y):
    return x + y

def kurang(x,y):
    return x - y

def kali(x,y):
    return x * y

def bagi(x,y):
    return x / y

def persegi(s):
    return s * s

def kelpersegi(s):
    return 4 * s

def kubus(s):
    return s * s * s

def lingkaran(r):
    return math.pi * r * r

def kelingkaran(r):
    return 2 * math.pi * r

def balok(p,l,t):
    return p * l * t

upper = "======Kalkulator Ajaib======" #garis ====== di atas
while True:
    print(upper)
    print("1.Aritmetika Dasar")
    print("2.Menghitung Geometri")

    pilihanmenu = int(input("Masukkan Pilihan Menu : ")) #memilih menu aritmatika dasar atau geometri

    if pilihanmenu == 1:
        print(upper)
        print("1.Pertambahan")
        print("2.Pengurangan")
        print("3.Perkalian")
        print("4.Pembagian")
        print(upper)
    elif pilihanmenu == 2:
        print(upper)
        print("5.Mengihtung Luas Persegi")
        print("6.Menghitung keliling persegi")
        print("7.Menghitung Luas Lingkaran")
        print("8.Menghitung Keliling Lingkaran")
        print("9.Menghitung Volume Kubus")
        print("10.Menghitung Volume Balok")

    pilihan = int(input("MASUKKAN PILIHAN (1/2/3/4 Dst...) : ")) 


    if pilihan == 1:
        angka1 = float(input("MASUKKAN ANGKA PERTAMA : "))
        angka2 = float(input("MASUKKAN ANGKA KEDUA : "))
        print(angka1, "+", angka2, "=", tambah(angka1, angka2))
    elif pilihan == 2:
        angka1 = float(input("MASUKKAN ANGKA PERTAMA : "))
        angka2 = float(input("MASUKKAN ANGKA KEDUA : "))
        print(angka1, "-", angka2, "=", kurang(angka1, angka2))
    elif pilihan == 3:
        angka1 = float(input("MASUKKAN ANGKA PERTAMA : "))
        angka2 = float(input("MASUKKAN ANGKA KEDUA : "))
        print(angka1, "x", angka2, "=", kali(angka1, angka2))
    elif pilihan == 4:
        angka1 = float(input("MASUKKAN ANGKA PERTAMA : "))
        angka2 = float(input("MASUKKAN ANGKA KEDUA : "))
        if angka2 != 0:
         print(angka1, "÷", angka2, "=", bagi(angka1, angka2))
        else:
         print("Tidak Bisa Di Bagi Dengan 0.")
    elif pilihan == 5:
        sisipersegi = float(input("MASUKKAN SISI PERSEGI : "))
        print("Luas Persegi = S x S")
        print(sisipersegi , "x", sisipersegi , "=", persegi(sisipersegi))
    elif pilihan == 6:
        sisipersegi = float(input("MASUKKAN SISI PERSEGI : "))
        print("Keliling Persegi = 4 x s")
        print("4" , "x", sisipersegi , "=", kelpersegi(sisipersegi))
    elif pilihan == 7:
        r = float(input("MASUKKAN JARI - JARI LINGKARAN : "))
        print("Luas Lingkaran = π x r x r")
        print("π" , "x", "r x r" , "=", (lingkaran(r)), "Atau" , round(lingkaran(r)))
    elif pilihan == 8:
        r = float(input("MASUKKAN JARI - JARI LINGKARAN : "))
        print("Keliling Lingkaran = 2 x π x r")
        print("2" , "x", "π x r" , "=", (kelingkaran(r)), "Atau" , round(kelingkaran(r)))
    elif pilihan == 9:
        sisipersegi = float(input("MASUKKAN SISI PERSEGI : "))
        print("Kubus = S x S x S")
        print(sisipersegi , "x", sisipersegi , "=", kubus(sisipersegi))
    elif pilihan == 10:
        panjang = float(input("Masukkan Panjang : "))
        lebar = float(input("Masukkan Lebar : "))
        tinggi  = float(input("Masukkan Tinggi : "))
        print("Volume Balok = P x L x T")
        print(panjang, "x", lebar, "x", tinggi, "=", balok(panjang,lebar,tinggi))
    else:
        print("PILIHAN TIDAK VALID. MASUKKAN (1/2/3/4 Dst...)")

    lanjut = input("Lanjut Atau Tidak? (Y/n) : ").lower()
    if lanjut != 'y':
        print("Terima Kasih Telah Menggunakan Kalkulator")
        break