"""
💪🏻Hard: Kullanıcıdan aldığınız bir metnin içindeki sesli harfleri sayan ve bunu kullanıcıya geri dönen bir kod parçacığı yazar mısın?
"""
sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']

def sesliHarfleriveSayisiniBul(metin):
    adet = 0
    for x in metin :
        for harf in sesli_harfler:
            if(x.lower()==harf):
                adet+=1
    return adet

girilenMetin = input("Bir metin giriniz: ")
sesli_sayisi = sesliHarfleriveSayisiniBul(girilenMetin)
print(f"Girdiğiniz metinde {sesli_sayisi} sesli harf bulunuyor.")