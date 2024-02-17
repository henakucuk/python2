
def asallariuret():
    liste=[]
    for sayi in range(2,1000):
        asalmi=1
        for i in range(2,sayi):
            if sayi%i==0:
                asalmi=0
                break
        if asalmi==1:
            liste.append(sayi)
    return liste

def goldbachsayilari(anasayi):
    asal=asallariuret()
    fark=0

    for eleman in asal:
        fark = anasayi-eleman   #2 çıkar sayıdan,kalan asal mı? hayır sa 3 çıkar böyle böyle devam et
        if fark in asal:
            print("buldum",fark,eleman)
            break

goldbachsayilari(40)
