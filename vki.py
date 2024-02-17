#vucüt kitle indeksi

import tkinter as tk

pen = tk.Tk()
pen.geometry("400x400")

def vki():
    kilo=int(entkilo.get())   #kilo bilgisini entry den al
    boy=int(entboy.get())      #boy bilgisini entry den al
    boy=boy/100
    sonuc=kilo/(boy*boy)

    if sonuc<=18.5:
        lblsnc["font"]=("Arial",32)
        lblsnc["bg"]="pink"
        lblsnc["fg"]="white"
        lblsnc["text"]=f"{round(sonuc,2)}  - ZAYIF"
    elif sonuc>= 18.5 and sonuc<=24.9:
        lblsnc["font"]=("Arial",32)
        lblsnc["bg"]="lightblue"
        lblsnc["fg"]="white"
        lblsnc["text"]=f"{round(sonuc,2)}   - NORMAL"
    elif sonuc>= 25 and sonuc<=29.9:
        lblsnc["font"]=("Arial",32)
        lblsnc["bg"]="blue"
        lblsnc["fg"]="white"
        lblsnc["text"]=f"{round(sonuc,2)}   - KİLOLU"
    elif sonuc>= 30 and sonuc<=34.9:
        lblsnc["font"]=("Arial",32)
        lblsnc["bg"]="red"
        lblsnc["fg"]="white"
        lblsnc["text"]=f"{round(sonuc,2)}   - OBEZ"
    elif sonuc>= 35:
        lblsnc["font"]=("Arial",25)
        lblsnc["bg"]="brown"
        lblsnc["fg"]="white"
        lblsnc["text"]=f"{round(sonuc,2)}   - MORBİD OBEZ"



entboy = tk.Entry()       #ekranda boy entrysi için
entboy.pack()              

entkilo = tk.Entry()       #ekranda kilo enreysi için
entkilo.pack()

btnhsp = tk.Button(text = "HESAPLA",command=vki)  #buton,tıklarsan vki fonksiyonuna gider
btnhsp.pack()

lblsnc=tk.Label(text="")  #sonucu yazacagım alan
lblsnc.pack()


pen.mainloop()
