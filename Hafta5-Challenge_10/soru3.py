"""
💪🏻Hard: Kullanıcının girdiği bir sayının tam bölenlerinin toplamını hesaplayan bir kod parçacığı yazınız.
"""
def tamBolenleriBul(sayi):
    toplam = 0
    for i in range(1, sayi+1):
        if sayi % i == 0:
            toplam+=i
    return toplam

girilenSayi = int(input("Bir sayi giriniz: "))
print("Tam bölenlerinin toplamı: ",tamBolenleriBul(girilenSayi))

