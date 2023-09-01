"""
🌟Medium:  Kullanıcıdan alınan bir metindeki kelime sayısını hesaplayan bir kod parçacığı yazar mısın?
"""
def kelimeSayisiHesapla(metin):
    return len(metin.split(" "))

kullaniciMetin = input("Bir metin giriniz: ")
kelimeSayisi = kelimeSayisiHesapla(kullaniciMetin)
print(f"Girdiğiniz metinde {kelimeSayisi} adet kelime bulunuyor.")