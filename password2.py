#string.ascii_lowercase

import string

parola = "asd.A34rty6"
szlk = {0:"very very weak",1:"very weak",2:"weak",3:"strong",4:"very strong"}

num,low,upp,sym = 0,0,0,0 #false
numcolor,lowcolor,uppcolor,symcolor = "red","red","red","red"

if len(parola)>=8:
    for character in parola:
        if character in string.digits:
            num = 1 #true
        elif character in string.ascii_lowercase:
            low = 1
        elif character in string.ascii_uppercase:
            upp = 1
        elif character in string.punctuation:  #semboller özel karakterler
            sym = 1

toplam = num+low+upp+sym

print(num,low,upp,sym)

print(szlk[toplam])
