import math
"""
🙌🏼 Easy: Bir araba saatte 60 km hızla hareket ediyor. Bu araba kaç saatte 240 km yol alır?

"""

#Hız = Yol / Zaman

def zamanHesapla(yol, hiz):
    zaman = math.ceil(yol / hiz)
    return zaman

print("Araba", zamanHesapla(240,60), "saatte 240 km yol alır.")