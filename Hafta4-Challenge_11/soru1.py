"""
🙌🏼Easy: Kullanıcıdan aldığınız bir sayının faktöriyelini hesaplayan kod parçacığını yazmanızı istiyorum.
"""

girilenSayi = int(input("Bir sayi giriniz: "))

def faktoriyel(girilenSayi):
    if(girilenSayi < 0):
        print("Negatif sayıların faktöriyeli hesaplanamaz.")
        return 
    elif(girilenSayi == 0):
        return 1
    else:
        return girilenSayi * (faktoriyel(girilenSayi-1))

print(f"Sonuc: {faktoriyel(girilenSayi)}")