#password2 but this one is tkinter

import tkinter as tk
import string

pen = tk.Tk()
pen.geometry("400x400")

def look():
    mypsw = psw.get() #my password -> password
    szlk = {0:"very very weak",1:"very weak",2:"weak",3:"strong",4:"very strong"}

    num,low,upp,sym = 0,0,0,0 #false
    numcolor,lowcolor,uppcolor,symcolor = "red","red","red","red"

    if len(mypsw)>=8:
        for character in mypsw:
            if character in string.digits:
                num = 1 #true
                numcolor = "green"
            elif character in string.ascii_lowercase:
                low = 1
                lowcolor = "green"
            elif character in string.ascii_uppercase:
                upp = 1
                uppcolor = "green"
            elif character in string.punctuation:  #semboller özel karakterler
                sym = 1
                symcolor = "green"

    toplam = num+low+upp+sym
    lblgnl["text"] = szlk[toplam]
    lblnum["fg"] = numcolor
    lblnum["text"] = "NUMBER"
    lbllow["fg"] = lowcolor
    lbllow["text"] = "LOWER"
    lblupp["fg"] = uppcolor
    lblupp["text"] = "UPPER"
    lblsym["fg"] = symcolor
    lblsym["text"] = "SYMBOL"

psw = tk.Entry()
psw.pack()

btn = tk.Button(text = "CHECK",command = look)
btn.pack()

lblgnl = tk.Label(text = "")
lblgnl.pack()
lbllow = tk.Label(text = "")
lbllow.pack()
lblupp = tk.Label(text = "")
lblupp.pack()
lblsym = tk.Label(text = "")
lblsym.pack()
lblnum = tk.Label(text = "")
lblnum.pack()

pen.mainloop()
