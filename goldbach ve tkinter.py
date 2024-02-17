import tkinter as tk

pencere = tk.Tk()
pencere.geometry("400x400")

def goldbachsayilari():
    anasayi=int(ent1.get())  #git entry den değer al
    asal=[2,3,5,7,9,11,13,17,19,23,29]
    fark=0

    for eleman in asal:
        fark = anasayi-eleman
        if fark in asal:
            print("buldum",fark,eleman)
            lbl1["text"]=f"{fark} ve {eleman}"
            break

ent1=tk.Entry(font=("Arial,32"))
ent1.pack()

btn1=tk.Button(text="BUL",command=goldbachsayilari)  #butona basınca git ve f cagir
btn1.pack()

lbl1=tk.Label(text="")
lbl1.pack()


pencere.mainloop()

#entry ye giren her şey str
