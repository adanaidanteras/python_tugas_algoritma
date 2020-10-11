print("-" * 40)

# Lingkaran
print("1. Menghitung Luas Lingkaran")
jari_jari=float(input("Masukan Jari-jari : "));
phi = 3.14 ;
luas = phi * (jari_jari * jari_jari);
print("Luas Lingkaran dengan Jari-jari " + str(jari_jari) + " adalah " + str(luas));
print("-" * 40)

# Persegi panjang
print("2. Menghitung Luas Persegi Panjang")
panjang=float(input("Masukan Panjang : "));
lebar=float(input("Masukan Lebar : "));
luas = panjang * lebar;
print("Luas Persegi Panjang dengan Panjang "+str(panjang)+" dan Lebar "+str(lebar)+" adalah "+str(luas)); 
print("-" * 40)

# Bujur Sangkar
print("3. Menghitung Luas Bujur Sangkar")
sisi=float(input("Masukan Sisi : "));
luas = sisi;
print("Luas Bujur Sangkar dengan Sisi "+str(sisi)+" adalah "+str(luas));
