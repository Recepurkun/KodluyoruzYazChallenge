"""
💪🏻Hard: Kullanıcıdan aldığınız bir sayının Armstrong sayısı olup olmadığını kontrol eden bir kod parçacığı yazar mısınız? (Armstrong sayısı: Basamaklarının üçüncü kuvvetinin toplamı, sayıya eşit olan sayılardır.)
🗝️ 407 için = (4*4*4)+(7*7*7)=407 bir armstrong sayısıdır.🤗
"""
def armstrongSayisiBul(sayi):
    sonuc = 0
    for i in str(sayi):
        sonuc += int(i) ** 3
    if(sonuc==sayi):
        print(f"Girdiğiniz {sayi} sayisi Armstrong sayisidir")    
    else:
        print(f"Girdiğiniz {sayi} sayisi Armstrong sayisi değildir")
        

sayi = int(input("Bir sayi giriniz: "))
armstrongSayisiBul(sayi)
