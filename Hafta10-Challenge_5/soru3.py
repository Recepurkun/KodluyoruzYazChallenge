"""
💪🏻Hard: Kullanıcının girdiği bir sayı karekökten çıkıyorsa çıktığı halini eğer çıkmıyorsa karekökten tam olarak çıkmıyor hata mesajı veren kod parçacığını yazar mısın?
🗝️   Kullanıcı Sayı:64
       Cevap:8
       Kullanıcı Sayı:72
       Cevap: Karekökten tam olarak çıkmıyor.
"""
import math

try:
    kullanici_sayi = float(input("Bir sayı girin: "))
    karekok = math.sqrt(kullanici_sayi)
    
    if karekok.is_integer(): #? Karekökün tam sayıya dönüp dönmediğini kontrol et
        print(f"Cevap: {int(karekok)}") #? Tam sayı ise tam sayı değerini döndür
    else:
        print("Cevap: Karekökten tam olarak çıkmıyor.")
except ValueError:
    print("Lütfen geçerli bir sayı girin.")
