range_bil = 200
for bilangan in range(200):
    if (bilangan >= 2):
        jumlah_bisa_dibagi = 0
        pembagi_bilangan = 2
        while pembagi_bilangan < bilangan:
            if (bilangan % pembagi_bilangan) == 0:
                jumlah_bisa_dibagi += 1;
            pembagi_bilangan += 1;
        if jumlah_bisa_dibagi == 0:
            print(bilangan, end=',')