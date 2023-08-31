"""
🙌🏼 Easy: Kullanıcıdan aldığınız sayının tek mi çift mi olduğunu ekrana yazdıran bir kod parçacığı yazar mısın? 
"""
girilenSayi = int(input("Bir sayi giriniz: "))
if girilenSayi<0:
    print("0'dan kücük sayilar çift veya tek olamazlar")
elif girilenSayi % 2 == 0:
    print(girilenSayi, "sayisi çift sayidir")
else:
    print(girilenSayi, "sayisi tek sayidir")