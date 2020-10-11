print("-"*30)
print("\t Kasir CLI")
print("-"*30)

harga = float(input("Masukan Harga Barang \t : Rp."))
qty = int(input("Masukan Jumlah Barang \t : "))

harga_bayar = harga * qty
discount = 0

if (harga_bayar >= 100000):
    discount = harga_bayar * 10 / 100
else :
    discount = 0

total_harga_bayar = harga_bayar - discount

print("-"*30)
print("Harga Bayar \t\t : Rp."+str(harga_bayar))
print("Discount \t\t : Rp."+str(discount))
print("Total Harga Bayar \t : Rp." + str(total_harga_bayar))
