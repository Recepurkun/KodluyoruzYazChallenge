#kütüphaneler
from collections import Counter #Nesneleri saymak için kullanılan bir dictionary alt sınıfı

"""
🌟 Medium: Kullanicidan bir metin almanizi istiyorum. Bu metnin içindeki en çok tekrar eden harfi bulmalı ve kaç kere tekrar ettiğini göstermeli.
"""

#hazir fonksiyon kullanarak(bosluk karakteri dahil)
metin = input("Bir metin girin: ")

harf_sayilari = Counter(metin)

en_cok_tekrar_eden_harf, tekrar_sayisi = harf_sayilari.most_common(1)[0]

#eger en cok tekrar eden karakter bosluk ise onu yazdir 
if en_cok_tekrar_eden_harf == ' ':
    en_cok_tekrar_eden_harf = "en cok tekrar eden bosluk karakteridir"

print("En çok tekrar eden harf:", en_cok_tekrar_eden_harf)
print("Tekrar sayısı:", tekrar_sayisi)



# #hazir fonksiyon kullanmadan(bosluk karakteri dahil değil)
# metin = input("Bir metin girin: ")#Kullanıcıdan metni al
# # Metindeki harfleri say
# harf_sayilari = {}

# for harf in metin.lower():
#     if harf.isalpha():
#         if harf in harf_sayilari:
#             harf_sayilari[harf] += 1
#         else:
#             harf_sayilari[harf] = 1

# # En çok tekrar eden harfi ve sayısını bul
# en_cok_tekrar_eden_harf = ""
# tekrar_sayisi = 0

# for harf, sayi in harf_sayilari.items():
#     if sayi > tekrar_sayisi:
#         en_cok_tekrar_eden_harf = harf
#         tekrar_sayisi = sayi

# # Sonucu ekrana yazdır
# print("En çok tekrar eden harf:", en_cok_tekrar_eden_harf)
# print("Tekrar sayısı:", tekrar_sayisi)