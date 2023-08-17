"""
💪🏻Hard: Bir yüzme havuzunda 2 adet su girişi, 1 adet su çıkışı vardır. 
İlk su girişi havuzu 10 saatte doldururken, ikinci su girişi havuzu 15 saatte doldurmaktadır. 
Havuzun kendiliğinden boşalma hızı ise 30 saatte bir doludur. 
Eğer havuz boşken, her iki su girişi de açılırsa havuz ne kadar sürede dolar?😀
"""

def havuz_dolum_suresi(musluk1, musluk2, havuz_bosalma_suresi):
    # (1/10 + 1/15 - 1/30) = 2/15 -> 1 / (2/15) = 7,5 saat
    toplam_gecen_vakit = round(1 / ((1/musluk1) + (1/musluk2) - (1/havuz_bosalma_suresi)),2) #tersine cevirmek icin 1'e bolduk
    return toplam_gecen_vakit

musluk1 = 10  # İlk su girişi dolum süresi (saat)
musluk2 = 15  # İkinci su girişi dolum süresi (saat)
havuz_bosalma_suresi = 30  # Havuzun kendiliğinden boşalma süresi (saat)

toplam_dolum_suresi = havuz_dolum_suresi(musluk1, musluk2, havuz_bosalma_suresi)
print("Havuzun dolum süresi: ", toplam_dolum_suresi, "saat")