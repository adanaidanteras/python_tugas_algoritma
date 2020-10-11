def satu():
    print('Nasi Goreng')
    return;

def dua():
    print('Mie Goreng') 

def tiga():
    print('Capcay') 

print("Menu Makanan ")
print("--------------")
print("1. Nasi Goreng")
print("2. Mie Goreng")
print("3. Capcay ")
print("--------------")
menu = input("Pilih menu [1-3] : ")

switcher = {
    '1': lambda: satu(),
    '2': lambda: dua(),
    '3': lambda: tiga()
}

switcher.get(menu)()
