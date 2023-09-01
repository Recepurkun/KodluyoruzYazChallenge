"""
💪🏻Hard: Bir yarış pistinde iki yarışmacı aynı anda start alıyor. İlk yarışmacı saatte 15 km hızla, ikinci yarışmacı ise saatte 20 km hızla koşuyor. İkinci yarışmacı kaç saat sonra ilk yarışmacıyı yakalar?😀🗝️ Bu problemi çözen kodu yazmanı istiyorum🤗
"""
hiz_1 = 15 # İlk yarışmacının hızı (km/saat)
hiz_2 = 20 # İkinci yarışmacının hızı (km/saat)
baslangic_pozisyonu = 0 # İlk yarışmacının başlangıç pozisyonu (km)
baslangic_pozisyonu_2 = 0 # İkinci yarışmacının başlangıç pozisyonu (km)
gecen_sure = int((baslangic_pozisyonu - baslangic_pozisyonu_2) / (hiz_2 - hiz_1)) # İkinci yarışmacının ilk yarışmacıyı yakalaması için geçen süre (saat)
print("İkinci yarışmacı ilk yarışmacıyı", gecen_sure, "saat sonra yakalar.")
if(gecen_sure == 0):
    print("Sonuç olarak, ikinci yarışmacı ilk yarışmacıyı başlangıçta yakalar.")
