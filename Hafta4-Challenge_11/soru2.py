"""
🌟Medium:  Bir dizi oluşturup bu sayıların ortalamasını hesaplayan bir kod parçacığı yazar mısın?
"""

ornekDizi = [2,3,4,5,6,7,8,9,10] #toplam 54 ortalama 9
ornekDizi2 = [10,15,20,25,30,35,40,45,50] #toplam 270 ortalama 30

def ortalamaHesapla():
    toplam = 0
    ortalama=0
    #for i in ornekDizi2:
    #    toplam += i
    toplam = sum(ornekDizi) #?| sum otomatik topluyo gerek yok for'a
    ortalama = (toplam / int(len(ornekDizi)))
    print(f"Toplam: {toplam} | Ortalama: {round(ortalama)}")

ortalamaHesapla()