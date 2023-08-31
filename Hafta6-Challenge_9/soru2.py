"""
🌟 Medium: Bir dizi oluşturup içindeki çift sayıların toplamını hesaplayan bir kod parçacığı yazar mısınız?
"""
dizi = [1,2,3,4,5,6,7,8,9,10]

def ciftSayilariTopla(arr):
    sayac = 0
    toplam = 0
    for i in arr:
        if i % 2 == 0:
            sayac+=1
            toplam+=i
    
    return sayac, toplam

sayac,sonucToplam = ciftSayilariTopla(dizi)
print(f"Çift sayıların toplamlari: {sonucToplam} \nÇift sayıların adeti: {sayac}")
    