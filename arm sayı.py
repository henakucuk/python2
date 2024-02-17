"""
sayi = "407"

b1 = int(sayi[0])
b2 = int(sayi[1])
b3 = int(sayi[2])

toplam = b1**3+b2**3+b3**3

if toplam == sayi:
    print("arm")
else:
    print("not")

"""

sayi = 407

b1 = sayi//100  #4
b2 = (sayi//10)%10  #0
b3 = sayi%10  #7

toplam = b1**3+b2**3+b3**3

if toplam == sayi:
    print("arm")
else:
    print("not")
