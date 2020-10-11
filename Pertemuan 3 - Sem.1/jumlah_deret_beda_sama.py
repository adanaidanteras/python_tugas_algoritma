# deret angka S = 1 + 3 + 5 + 7 + 9 + 11

#memasukan suku pertama
a = int(input("Masukan Suku Pertama = "))
#memasukan beda
b = int(input("Masukan Beda = "))
#memasukan range
range_suku = int(input("Masukan Range Suku = "))

#inisialisasi jumlah suku 
suku_n = a
index_suku = 1
jumlah_suku = 0

while index_suku <= range_suku:
    print(str(suku_n), end =" ")
    jumlah_suku += suku_n
    suku_n += b
    index_suku += 1

print("\n Jumlah Suku Deret adalah " + str(jumlah_suku))
