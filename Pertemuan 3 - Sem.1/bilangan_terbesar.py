#bilangan terbesar

b1 = 20
b2 = 60
b3 = 40
b4 = 100

if (b1 > b2) and (b1 > b3) and (b1 > b4):
    #false and false and false => false
    print("bilangan 1 = " + str(b1) + " adalah bilangan terbesar")
elif (b2 > b1) and (b2 > b3) and (b2 > b4):
    #true and true and false => false
    print("bilangan 2 = "+str(b2)+" adalah bilangan terbesar")
elif (b3 > b1) and (b3 > b2) and (b3 > b4):
    #fasle and false and fasle => false
    print("bilangan 3 = " + str(b3) + " adalah bilangan terbesar")    
else:
    print("bilangan 4 = " + str(b4) + " adalah bilangan terbesar")