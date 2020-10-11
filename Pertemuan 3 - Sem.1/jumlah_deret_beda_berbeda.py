# deret angka S = 2 + 5 + 10 + 17 + 26 + 37

#memasukan suku pertama
a = int(input("Masukan Suku Pertama = "))
#memasukan beda
b1 = int(input("Masukan Beda Pertama (Bilangan Ganjil) = "))

if b1 % 2 == 1 :

    #memasukan range
    range_suku = int(input("Masukan Range Suku = "))

    #inisialisasi jumlah suku 
    b = b1
    suku_n = a
    index_suku = 1
    jumlah_suku = 0

    while index_suku <= range_suku:
        print(str(suku_n), end =" ")
        jumlah_suku += suku_n
        suku_n += b
        b += 2
        index_suku += 1

    print("\n Jumlah Suku Deret adalah " + str(jumlah_suku))
else:
    print("Maaf, Deret pertama harus bilangan Ganjil")
    