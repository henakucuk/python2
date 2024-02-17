#100 ile bin arasındaki bütün sayılardan arm bul

for sayi in range(100,1000):
    
    b1 = sayi//100
    b2 = (sayi//10)%10
    b3 = sayi%10

    toplam = b1**3+b2**3+b3**3

    if toplam==sayi:
        print(f"{toplam} ARM")

