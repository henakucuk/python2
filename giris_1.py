"""
import tkinter

pencere = tkinter.Tk()

pencere.mainloop()

böyle diyebiliriz evet,ama her seferinde uzun uzun yazmak yorucu ve gereksiz
"""

import tkinter as tk

p = tk.Tk()
p.title("GiftedCoder") #başlık koymuş olduk
p.geometry("400x500+200+200")

#böyle yapıyoruz çünkü run yapınca ekran minivik çıkıyor ve başlığı görmek için büyütmemiz gerekiyor(en 400,boy 500)
#peki neden sol köşede duruyor? ,,, koordinat vererek(+ ile)değiştirebiliriz bunu ("400x500") idi önceden,sonra koordinat verdik (mesela 0a 0 verirsek sol üstte doğar)
"""
400 -> width
500 -> height
100-> sola mesafe
0 -> uste mesafe
"""
p.configure(bg="red" , cursor="heart") #background u red yapar , cursorunu kalp çekline getirir



p.mainloop()
