#label,düz yazı etiket,obje

import tkinter as tk

pen = tk.Tk()
pen.geometry("300x300") #aha buraya
#mesela diyelim ki ben benim pencerem 300e 300de kalsın büyütemeyelim istiyorum;
pen.resizable("False","False") #böyle yaptık mı büyümüyor veya küçültülmüyor,, (sabit genişlik ve yükseklik içeriyor)

lbl1 = tk.Label(text = "Kullanıcı Adı",fg="red",bg="white",width="20",font=("Arial",25))
#label oluşuyor,ama paketlemiyoruz,,,,fg yani yazı rengi kırmızı oldu,,backgroung(sadece yazının arkası) white oldu,,
#yazının genişliğini büyüttük(20piksellik alanda boşluk yarattı)
#font değiştirdik ve 25 yaptık ama baya büyük oldu

#lbl1.pack()
#şimdi paketledik, ve minicik bir hale geldi çünkü geometrisi yok o yüzden yukarıya gidip pencereye geometri veriyoruz

lbl1.pack(side="bottom") #aşağı aldı yazıyı, farklı paketledik



pen.mainloop()
