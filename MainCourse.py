# Author        = vrs.scrypt
# Github        = https://github.com/KiplixGG
# IG            = @vrs.scrypt
# Contact       = 0895321579467

import os, time, random
from os import system

z = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagitarius',
     'Capricon']


def garis():
    print("=======================================================")


def menu():
    os.system('clear')
    choice = input('''
v.1.0
=======================================================
|        SELAMAT DATANG DI PUSAT PENGETAHUAN          | 	
=======================================================
| 1. Bangun Datar                                     |
| 2. Bangun Ruang                                     |
| 3. Konversi Suhu                                    |
| 4. Peta {S,JP,JS}                                   |
| 5. Mini Kalkulator                                  |
| 6. Mencari Zodiak                                   |
| 7. Generate Password                                |
| 8. Matematika                                       |
| 99. Keluar                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        bangundatar()
    elif choice == '2':
        bangunruang()
    elif choice == '3':
        suhu()
    elif choice == '4':
        peta()
    elif choice == '5':
        kalkulator()
    elif choice == '6':
        zodiak()
    elif choice == '7':
        password()
    elif choice == '8':
        mtkdasar()
    elif choice == '99':
        print("\nGood Bye")
        time.sleep(2)
        exit()
    else:
        menu()


def bangundatar():
    os.system('clear')
    choice = input('''
=======================================================
|                    BANGUN DATAR                     |
=======================================================
| 1. Persegi                                          |
| 2. Persegi Panjang                                  |
| 3. Segitiga                                         |
| 4. Jajar Genjang                                    |
| 5. Trapesium                                        |
| 6. Layang-Layang                                    |
| 7. Belah Ketupat                                    |
| 8. Lingkaran                                        |
| 9. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        pilih1()
    elif choice == '2':
        pilih2()
    elif choice == '3':
        pilih3()
    elif choice == '4':
        pilih4()
    elif choice == '5':
        pilih5()
    elif choice == '6':
        pilih6()
    elif choice == '7':
        pilih7()
    elif choice == '8':
        pilih8()
    elif choice == '9':
        menu()
    else:
        bangundatar()


def pilih1():
    # Rumus Bangun Datar Persegi
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Sisinya : "))
        print("\nLuas Persegi : Sisi x Sisi")
        garis()
        print(n1,"x",n1,"=",n1*n1)
        garis()

    elif choice == '2':
        n1 = 4
        n2 = int(input("\nMasukan Sisinya : "))
        print("\nKeliling Persegi : 4 x Sisi")
        garis()
        print(n1,"x",n2,"=",n1*n2)
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih1()

    bicara()


def pilih2():
    # Rumus Bangun Datar Persegi Panjang
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Panjangnya : "))
        n2 = int(input("Masukan Lebarnya   : "))
        print("\nLuas Persegi Panjang : Panjang x Lebar")
        garis()
        print(n1,"x",n2,"=",n1*n2)
        garis()

    elif choice == '2':
        n1 = 2
        n2 = int(input("\nMasukan Panjangnya : "))
        n3 = int(input("Masukan Lebarnya   : "))
        print("\nKeliling Persegi Panjang : 2 x (Panjang + Lebar)")
        garis()
        print(n1,"x","(",n2,"+",n3,") =",n1*(n2+n3))
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih2()

    bicara()


def pilih3():
    # Rumus Bangun Datar Segitiga
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Alasnya   : "))
        n2 = int(input("Masukan Tingginya : "))
        print("\nLuas Segitiga : 1/2 x Alas x Tinggi")
        garis()
        print(1/2,"x",n1,"x",n2,"=",1/2*n1*n2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Sisi Ke-1 : "))
        n2 = int(input("Masukan Sisi Ke-2 : "))
        n3 = int(input("Masukan Sisi Ke-3 : "))
        print("\nKeliling Segitiga : Sisi1 + Sisi2 + Sisi3")
        garis()
        print(n1,"+",n2,"+",n3,"=",n1+n2+n3)
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih3()

    bicara()


def pilih4():
    # Rumus Bangun Datar Jajar Genjang
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Alasnya   : "))
        n2 = int(input("Masukan Tingginya : "))
        print("\nLuas Jajar Genjang : Alas x Tinggi")
        garis()
        print(n1,"x",n2,"=",n1*n2)
        garis()

    elif choice == '2':
        n1 = int(input("\nSisi yang Sejajar ke-1 : "))
        n2 = int(input("Sisi yang Sejajar ke-2 : "))
        print("\nKeliling Jajar Genjang : 2 x (Sisi1 + Sisi2)")
        garis()
        print(2,"(",n1,"+",n2,") =",2*(n1+n2))
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih4()

    bicara()


def pilih5():
    # Rumus Bangun Datar Trapesium
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Sisi Atasnya  : "))
        n2 = int(input("Masukan Sisi Bawahnya : "))
        n3 = int(input("Masukan Tingginya     : "))
        print("\nLuas Trapesium : 1/2 x (Sisi Atas + Sisi Bawah) x tinggi")
        garis()
        print(1/2,"x (",n1,"+",n2,") x",n3,"=",1/2*(n1+n2)*n3)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Sisi Ke-1 : "))
        n2 = int(input("Masukan Sisi Ke-2 : "))
        n3 = int(input("Masukan Sisi Ke-3 : "))
        n4 = int(input("Masukan Sisi Ke-4 : "))
        print("\nKeliling Trapesium : Sisi1 + Sisi2 + Sisi3 + Sisi4")
        garis()
        print(n1,"+",n2,"+",n3,"+",n4,"=",n1+n2+n3+n4)
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih5()

    bicara()


def pilih6():
    # Rumus Bangun Datar Layang-Layang
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Diagonal 1 (D1) : "))
        n2 = int(input("Masukan Diagonal 2 (D2) : "))
        print("\nLuas Layang-Layang : 1/2 x D1 x D2")
        garis()
        print(1/2,"x",n1,"x",n2,"=",1/2*n1*n2)
        garis()

    elif choice == '2':
        n1 = int(input("\nSisi Pertama (a) : "))
        n2 = int(input("Sisi Kedua   (b) : "))
        n3 = int(input("Sisi Ketiga  (c) : "))
        n4 = int(input("Sisi Keempat (d) : "))
        print("\nKeliling Layang-Layang : a + b + c + d")
        garis()
        print(n1,"+",n2,"+",n3,"+",n4,"=",n1+n2+n3+n4)
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih6()

    bicara()


def pilih7():
    # Rumus Bangun Datar Belah Ketupat
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 3. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Diagonal 1 (D1) : "))
        n2 = int(input("Masukan Diagonal 2 (D2) : "))
        print("\nLuas Belah Ketupat : 1/2 x D1 x D2")
        garis()
        print(1/2,"x",n1,"x",n2,"=",1/2*n1*n2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Sisinya : "))
        print("\nKeliling Belah Ketupat : 4 x Sisi")
        garis()
        print(4,"x",n1,"=",4*n1)
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih7()

    bicara()


def pilih8():
    # Rumus Bangun Datar Lingkaran
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas                                     |
| 2. Mencari Keliling                                 |
| 5. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Jari-Jarinya (r) : "))
        print("\nLuas Lingkaran : π x r²")
        garis()
        print(22/7,"x",n1,"x",n1,"=",22/7*n1**2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Jari-Jarinya (r) : "))
        print("\nKeliling Lingkaran : 2 x π x r")
        garis()
        print(2,"x",22/7,"x",n1,"=",2*22/7*n1)
        garis()

    elif choice == '3':
        bangundatar()

    else:
        pilih8()

    bicara()


def bicara():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        bangundatar()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        bicara()


def bangunruang():
    os.system('clear')
    choice = input('''
=======================================================
|                    BANGUN RUANG                     |
=======================================================
| 1. Kubus                                            |
| 2. Balok                                            |
| 3. Limas Segiempat (error)                          |
| 4. Prisma Segitiga (error)                          |
| 5. Limas Segitiga (error)                           |
| 6. Tabung (error)                                   |
| 7. Kerucut (error)                                  |
| 8. Bola                                             |
| 9. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        pilih21()
    elif choice == '2':
        pilih22()
    elif choice == '3':
        pilih23()
    elif choice == '4':
        pilih24()
    elif choice == '5':
        pilih25()
    elif choice == '6':
        pilih26()
    elif choice == '7':
        pilih27()
    elif choice == '8':
        pilih28()
    elif choice == '9':
        menu()
    else:
        bangunruang()


def pilih21():
    # Rumus Bangun Ruang Kubus
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Sisinya : "))
        print("\nLuas Permukaan Kubus : 6 x Sisi²")
        garis()
        print(6,"x",n1,"x",n1,"=",6*n1**2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Sisinya : "))
        print("\nVolume Kubus : Sisi x Sisi x Sisi")
        garis()
        print(n1,"x",n1,"x",n1,"=",n1**3)
        garis()

    elif choice == '3':
        n1 = int(input("\nMasukan Sisinya : "))
        print("\nKeliling Kubus : 12 x Sisi")
        garis()
        print(12,"x",n1,"=",12*n1)
        garis()

    elif choice == '4':
        bangunruang()

    else:
        pilih21()

    pitakon()


def pilih22():
    # Rumus Bangun Ruang Balok
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Panjangnya (p) : "))
        n2 = int(input("Masukan Lebarnya (l)   : "))
        n3 = int(input("Masukan Tingginya (t)  : "))
        print("\nLuas Permukaan Balok : 2 x (pxl + lxt + pxt)")
        garis()
        print(2,"x (",n1,"x",n2,"+",n2,"x",n3,"+",n1,"x",n3,")","=",2*(n1*n2+n2*n3+n1*n3))
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Panjangnya : "))
        n2 = int(input("Masukan Lebarnya   : "))
        n3 = int(input("Masukan Tingginya  : "))
        print("\nVolume Balok : Panjang x Lebar x Tinggi")
        garis()
        print(n1,"x",n2,"x",n3,"=",n1*n2*n3)
        garis()

    elif choice == '3':
        n1 = int(input("\nMasukan Panjangnya : "))
        n2 = int(input("Masukan Lebarnya   : "))
        n3 = int(input("Masukan Tingginya  : "))
        print("\nKeliling Balok : 4 x (Panjang + Lebar + Tinggi)")
        garis()
        print(4,"x (",n1,"+",n2,"+",n3,") =",4*(n1+n2+n3))
        garis()

    elif choice == '4':
        bangunruang()

    else:
        pilih22()

    pitakon()


def pilih23():
    # Rumus Bangun Ruang Limas Segiempat
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')


def pilih24():
    # Rumus Bangun Ruang Prisma Segitiga
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')


def pilih25():
    # Rumus Bangun Ruang  Limas Segitiga
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')


def pilih26():
    # Rumus Bangun Ruang Tabung
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')


def pilih27():
    # Rumus Bangun Ruang Kerucut
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas Permukaan                           | 
| 2. Mencari Volume                                   |
| 3. Mencari Keliling                                 |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')


def pilih28():
    # Rumus Bangun Ruang Bola
    os.system('clear')
    choice = input('''
=======================================================
| 1. Mencari Luas (untuk π : 22/7)                    |
| 2. Mencari Luas (untuk π : 3.14)                    |
| 3. Mencari Volume (untuk π : 22/7)                  | 
| 4. Mencari Volume (untuk π : 3.14)                  |                 
| 5. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Jari-Jarinya (r) : "))
        print("\nLuas Bola : 4 x π x r²")
        garis()
        print(4,"x",22/7,"x",n1,"x",n1,"=",4*22/7*n1**2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Jari-Jarinya (r) : "))
        print("\nLuas Bola : 4 x π x r²")
        garis()
        print(4,"x",3.14,"x",n1,"x",n1,"=",4*3.14*n1**2)
        garis()

    elif choice == '3':
        n1 = int(input("\nMasukan Jari-Jarinya (r) : "))
        print("\nVolume Bola : 4/3 x π x r³")
        garis()
        print(4/3,"x",22/7,"x",n1,"x",n1,"x",n1,"=",4/3*22/7*n1**3)
        garis()

    elif choice == '4':
        n1 = int(input("\nMasukan Jari-Jarinya (r) : "))
        print("\nVolume Bola : 4/3 x π x r³")
        garis()
        print(4/3,"x",3.14,"x",n1,"x",n1,"x",n1,"=",4/3*3.14*n1**3)
        garis()

    elif choice == '3':
        bangunruang()

    else:
        pilih28()

    pitakon()


def pitakon():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        bangunruang()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        pitakon()


def suhu():
    os.system('clear')
    choice = input('''
==========================================================		
|                     KONVERSI SUHU                      |
==========================================================
| 1. Celcius Ke Reamur          7. Fahrenheit Ke Celcius |
| 2. Celcius Ke Fahrenheit      8. Fahrenheit Ke Reamur  |
| 3. Celcius Ke Kelvin          9. Fahrenheit Ke Kelvin  |
| 4. Reamur Ke Celcius          10. Kelvin Ke Celcius    |
| 5. Reamur Ke Fahrenheit       11. Kelvin Ke Reamur     |
| 6. Reamur Ke Kelvin           12. Kelvin Ke Fahrenheit |
|                                                        |
|                      0. Kembali                        |
==========================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Nilainya (°C) : "))
        print("\nIni Rumusnya : 4/5 x °C")
        garis()
        print(4/5,"x",n1,"=",4/5*n1,"°R")
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Nilainya (°C) : "))
        print("\nIni Rumusnya : (9/5 x °C) + 32°")
        garis()
        print("(",9/5,"x",n1,") +",32,"=",(9/5*n1)+32,"°F")
        garis()

    elif choice == '3':
        n1 = int(input("\nMasukan Nilainya (°C) : "))
        print("\nIni Rumusnya : °C + 273")
        garis()
        print(n1,"+",273,"=",n1+273,"°K")
        garis()

    elif choice == '4':
        n1 = int(input("\nMasukan Nilainya (°R) : "))
        print("\nIni Rumusnya : 5/4 x °R")
        garis()
        print(5/4,"x",n1,"=",5/4*n1,"°C")
        garis()

    elif choice == '5':
        n1 = int(input("\nMasukan Nilainya (°R) : "))
        print("\nIni Rumusnya : 9/4 x °R + 32")
        garis()
        print(9/4,"x",n1,"+",32,"=",9/4*n1+32,"°F")
        garis()

    elif choice == '6':
        n1 = int(input("\nMasukan Nilainya (°R) : "))
        print("\nIni Rumusnya : 5/4 x °R + 273)")
        garis()
        print(5/4,"x",n1,"+",273,"=",5/4*n1+273,"°K")
        garis()

    elif choice == '7':
        n1 = int(input("\nMasukan Nilainya (°F) : "))
        print("\nIni Rumusnya : 5/9 x (°F - 32)")
        garis()
        print(5/9,"x (",n1,"-",32,")c=",5/9*(n1-32),"°C")
        garis()

    elif choice == '8':
        n1 = int(input("\nMasukan Nilainya (°F) : "))
        print("\nIni Rumusnya : 4/9 x (°F - 32)")
        garis()
        print(4/9,"x (",n1,"-",32," =",4/9*(n1-32),"°R")
        garis()

    elif choice == '9':
        n1 = int(input("\nMasukan Nilainya (°F) : "))
        print("\nIni Rumusnya : 5/9 x (°F - 32) + 273")
        garis()
        print(5/9,"x (",n1,"-",32,") +",273,"=",5/9*(n1-32)+273,"°K")
        garis()

    elif choice == '10':
        n1 = int(input("\nMasukan Nilainya (°K) : "))
        print("\nIni Rumusnya : °K - 273")
        garis()
        print(n1,"-",273,"=",n1-273,"°C")
        garis()

    elif choice == '11':
        n1 = int(input("\nMasukan Nilainya (°K) : "))
        print("\nIni Rumusnya : 4/5 x (°K - 273)")
        garis()
        print(4/5,"x (",n1,"-",273,") =",4/5*(n1-273),"°R")
        garis()

    elif choice == '12':
        n1 = int(input("\nMasukan Nilainya (°K) : "))
        print("\nIni Rumusnya : 9/5 x (°K - 273) + 32")
        garis()
        print(9/5,"x (",n1,"-",273,") +",32,"=",9/5*(n1-273)+32,"°F")
        garis()

    elif choice == '0':
        menu()

    else:
        suhu()

    tekok()


def tekok():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        suhu()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        tekok()


def peta():
    os.system('clear')
    choice = input('''
=======================================================
|                  PETA {S, JS, JP}                   |
=======================================================
| 1. Mencari Skala                                    |
| 2. Mencari Jarak Sesungguhnya                       |
| 3. Mencari Jarak di Peta                            |
| 4. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Jarak Sesungguhnya (convert ke cm) : "))
        n2 = int(input("Masukan Jarak Pada Peta (cm) : "))
        print("\nIni Hasilnya")
        garis()
        print(n1,"/",n2,"=",n1/n2,",Skalanya Adalah 1 :",n1/n2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Jarak Pada Peta (cm) : "))
        n2 = int(input("Masukan Skala 1 : "))
        print("\nIni Hasilnya")
        garis()
        print(n1,"x",n2,"=",n1*n2,"Cm /",n1*n2/100000,"Km")
        garis()

    elif choice == '3':
        n1 = int(input("\nMasukan Jarak Sesungguhnya (convert ke cm) : "))
        n2 = int(input("Masukan Skalanya 1 : "))
        print("\nIni Hasilnya")
        garis()
        print(n1,"/",n2,"=",n1/n2,"Cm")
        garis()

    elif choice == '4':
        menu()

    else:
        peta()

    nyambung()


def nyambung():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        peta()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        nyambung()


def kalkulator():
    os.system('clear')
    choice = input('''
=======================================================
|                   MINI KALKULATOR                   |
=======================================================
| 1. Untuk Tambah                                     |
| 2. Untuk Kurang                                     |
| 3. Untuk Kali                                       |
| 4. Untuk Bagi                                       |
| 5. Untuk Pangkat                                    |
| 6. Untuk Akar                                       |
| #. Untuk Kembali                                    |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        n1 = int(input("\nMasukan Bilangan Pertama : "))
        n2 = int(input("Masukan Bilangan Kedua   : "))
        print("\nIni Hasilnya :")
        garis()
        print(n1,"+",n2,"=",n1+n2)
        garis()

    elif choice == '2':
        n1 = int(input("\nMasukan Bilangan Pertama : "))
        n2 = int(input("Masukan Bilangan Kedua   : "))
        print("\nIni Hasilnya :")
        garis()
        print(n1,"-",n2,"=",n1-n2)
        garis()

    elif choice == '3':
        n1 = int(input("\nMasukan Bilangan Pertama : "))
        n2 = int(input("Masukan Bilangan Kedua   : "))
        print("\nIni Hasilnya")
        garis()
        print(n1,"x",n2,"=",n1*n2)
        garis()

    elif choice == '4':
        n1 = int(input("\nMasukan Bilangan Pertama : "))
        n2 = int(input("Masukan Bilangan Kedua   : "))
        print("\nIni Hasilnya")
        garis()
        print(n1,"/",n2,"=",n1/n2)
        garis()

    elif choice == '5':
        n1 = int(input("\nMasukan Bilangan : "))
        n2 = int(input("Masukan Pangkat  : "))
        print("\nIni Hasilnya")
        garis()
        print(n1,"Pangkat",n2,"=",n1**n2)
        garis()

    elif choice == '6':
        n1 = int(input("\nMasukan Bilangannya : "))
        print("\nIni Hasilnya")
        garis()
        print("√",n1,"=",n1**0.5)
        garis()

    elif choice == '#':
        menu()

    else:
        kalkulator()

    terusan()


def terusan():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        kalkulator()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        terusan()


def zodiak():
    os.system('clear')
    print('''
=======================================================
|                     MY ZODIAC                       |
=======================================================''')
    y = int(input("\nMasukan Tanggal Lahir : "))
    x = input('''
=======================================================
|               Pilih Bulan Anda Lahir                |
=======================================================
|         1. Januari              7. Juli             |
|         2. Februari             8. Agustus          |
|         3. Maret                9. September        |
|         4. April                10. Oktober         |
|         5. Mei                  11. November        |
|         6. Juni                 12. Desember        |
=======================================================
Pilih Nomernya Saja   : ''')

    if x == '1' and 20 <= y <= 31 or x == '2' and y <= 18:
        print("\n> Zodiak Anda Adalah", z[0], "<")
    elif x == '2' and 19 <= y <= 29 or x == '3' and y <= 20:
        print("\n> Zodiak Anda Adalah", z[1], "<")
    elif x == '3' and 21 <= y <= 31 or x == '4' and y <= 20:
        print("\n> Zodiak Anda Adalah", z[2], "<")
    elif x == '4' and 21 <= y <= 30 or x == '5' and y <= 20:
        print("\n> Zodiak Anda Adalah", z[3], "<")
    elif x == '5' and 21 <= y <= 31 or x == '6' and y <= 20:
        print("\n> Zodiak Anda Adalah", z[4], "<")
    elif x == '6' and 21 <= y <= 30 or x == '7' and y <= 20:
        print("\n> Zodiak Anda Adalah", z[5], "<")
    elif x == '7' and 21 <= y <= 31 or x == '8' and y <= 21:
        print("\n> Zodiak Anda Adalah", z[6], "<")
    elif x == '8' and 22 <= y <= 31 or x == '9' and y <= 22:
        print("\n> Zodiak Anda Adalah", z[7], "<")
    elif x == '9' and 23 <= y <= 30 or x == '10' and y <= 22:
        print("\n> Zodiak Anda Adalah", z[8], "<")
    elif x == '10' and 22 <= y <= 31 or x == '11' and y <= 22:
        print("\n> Zodiak Anda Adalah", z[9], "<")
    elif x == '11' and 23 <= y <= 30 or x == '12' and y <= 20:
        print("\n> Zodiak Anda Adalah", z[10], "<")
    elif x == '12' and 21 <= y <= 31 or x == '1' and y <= 19:
        print("\n> Zodiak Anda Adalah", z[11], "<")
    else:
        print("\nAnda Alien Yaa")
        time.sleep(1)
        zodiak()

    nyinyer()


def nyinyer():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        zodiak()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        nyinyer()


def password():
    os.system('clear')
    print('''
=======================================================
|                GENERATE PASSWORD                    |
=======================================================''')
    x = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    passlen = int(input("\nMasukan Panjang Password : "))
    p = "".join(random.sample(x, passlen))
    print("\nPlease Wait!!!")
    time.sleep(3)
    print("\nYour Password Is =", p, )
    huek()


def huek():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        password()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        huek()


def mtkdasar():
    os.system('clear')
    choice = input('''
=======================================================
|                     MATEMATIKA                      |
=======================================================
| 1. Mencari FPB Dan KPK                              |
| 2. Menemukan Faktor Bilangan                        |
| 3. Menentukan Bilangan Ganjil Genap                 |
| 4. Menentukan Bilangan Prima                        |
| 5. Menentukan Bilangan Prima Dalam Rentang Tertentu |
| 6. Kembali                                          |
=======================================================
Pilih Nomer : ''')

    if choice == '1':
        def fpb(a,b):
            if a < b:
                smaller = a
            for i in range (1, smaller+1):
                if a % i == 0 and b % i == 0:
                    fpb = i
            return fpb

        def kpk(a,b):
            kpk = int(a*b/fpb(a,b))
            return kpk

        a = int(input("\nMasukan Bilangan Pertama : "))
        b = int(input("Masukan Bilangan Kedua   : "))
        print("\nFPB Dari",a,"Dan",b,"Adalah",fpb(a,b))
        print("KPK Dari",a,"Dan",b,"Adalah",kpk(a,b))


    elif choice == '2':
        x = int(input("\nMasukan Bilangan : "))
        print("\nFaktor Dari",x,"Adalah")
        for i in range(1, x+1):
            if x % i == 0:
                print(i)

    elif choice == '3':
        x = int(input("\nMasukan Bilangan : "))
        if x % 2 == 0:
            print("\nAngka",x,"Adalah Bilangan Genap")
        else:
            print("\nAngka",x,"Adalah Bilangan Ganjil")

    elif choice == '4':
        num = int(input("\nMasukan Bilangan : "))
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    print("\nAngka",num,"Bukan Bilangan Prima")
                    print(i,"Kali",num//i,"=",num)
                    break
            else:
                print("\nAngka",num,"Adalah Bilangan Prima")

    elif choice == '5':
        x = int(input("\nMasukan Rentang Awal  : "))
        y = int(input("Masukan Rentang Akhir : "))
        print("\nBilangan Prima Antara",x,"Dan",y,"Adalah")
        for num in range(x, y + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)

    elif choice == '6':
        menu( )

    jitok()

def jitok():
    calc_again = input('''
Apakah Mau Menggunakan Lagi
Ketik Y/y Untuk Ya
Ketik N/n Untuk Tidak
=======================================================
Ketik Apa : ''')

    if calc_again.upper() == 'Y':
        mtkdasar()

    elif calc_again.upper() == 'N':
        menu()

    else:
        print("\nInput Salah")
        jitok()

menu()
