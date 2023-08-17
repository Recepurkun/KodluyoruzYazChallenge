"""
Bir çiftlikte toplamda 36 baş tavuk ve koyun bulunmaktadır. 
Bu hayvanlardan toplamda 100 bacak çıkmaktadır. 
Çiftlikte kaçar tane tavuk ve koyun olduğunu bulan kod parçacığını yazar mısın?
"""

def hayvanBul(toplam_hayvan_sayisi, toplam_ayak_sayisi):
    # x: tavuk sayısı, y: koyun sayısı
    # x + y = toplam hayvan sayısı
    # 2x + 4y = toplam bacak sayısı

    for x in range(toplam_hayvan_sayisi + 1):
        y = toplam_hayvan_sayisi - x
        print("x: " , x , "| y: " , y)
        if (2 * x) + (4 * y) == toplam_ayak_sayisi:
            return x, y

toplam_hayvan_sayisi = 36
toplam_ayak_sayisi = 100

sonuc = hayvanBul(toplam_hayvan_sayisi, toplam_ayak_sayisi)

if sonuc:
    tavuk_sayisi, koyun_sayisi = sonuc
    print("Tavuk sayısı:", tavuk_sayisi)
    print("Koyun sayısı:", koyun_sayisi)