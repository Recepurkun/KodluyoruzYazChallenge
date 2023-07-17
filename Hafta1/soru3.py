
"""
💪🏻Hard: Bir tam sayı dizisi oluşturmanı istiyorum. Kullanıcıdan aldığın hedef sayı doğrultusunda sayı dizisinin içinden sayılar seçip toplayarak hedef sayıya ulaşmasını sağlamalısın. 
Farklı farklı kombinasyonlar ile hedef sayıya ulaşıyor olman burada çok önemli! 🥳
"""

def hedef_sayiya_ulas(tam_sayilar, hedef_sayi, yol=[]):
    if sum(yol) == hedef_sayi:
        print("Bir kombinasyon bulundu:", yol)
    elif sum(yol) > hedef_sayi:
        return
    else:
        for i, sayi in enumerate(tam_sayilar):
            kalan_sayilar = tam_sayilar[i+1:]
            hedef_sayiya_ulas(kalan_sayilar, hedef_sayi, yol + [sayi])

# Kullanıcıdan tam sayı dizisini ve hedef sayıyı al
tam_sayilar_str = input("Tam sayı dizisini girin (virgülle ayırarak): ")
hedef_sayi = int(input("Hedef sayıyı girin: "))

# Tam sayı dizisini oluştur
tam_sayilar = [int(sayi) for sayi in tam_sayilar_str.split(",")]

# Hedef sayıya ulaşmak için farklı kombinasyonları bul
hedef_sayiya_ulas(tam_sayilar, hedef_sayi)