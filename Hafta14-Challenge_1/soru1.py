"""
🙌🏼 Easy: Bir kutuda 5 kırmızı, 4 yeşil ve 3 mavi top bulunuyor. Kutudan rastgele çekilen 2 topun aynı renk olma olasılığı nedir?
🗝️ Bu problemi çözen kodu yazmanı istiyorum🤗
"""
import math

kirmiziTop = 5
yesilTop = 4
maviTop = 3

toplarin_toplam_sayisi = kirmiziTop + yesilTop + maviTop # Topların toplam sayısı
ayni_renk_olasiligi = 0 # İki topun aynı renk olma olasılığı

# İki topun aynı renk olma durumlarını hesapla
ayni_renk_olasiligi += (kirmiziTop / toplarin_toplam_sayisi) * ((kirmiziTop - 1) / (toplarin_toplam_sayisi - 1)) # Kırmızı renkte iki top
ayni_renk_olasiligi += (yesilTop / toplarin_toplam_sayisi) * ((yesilTop - 1) / (toplarin_toplam_sayisi - 1)) # Yeşil renkte iki top
ayni_renk_olasiligi += (maviTop / toplarin_toplam_sayisi) * ((maviTop - 1) / (toplarin_toplam_sayisi - 1)) # Mavi renkte iki top

print("İki topun aynı renk olma olasılığı: %",round(ayni_renk_olasiligi*100, 2))