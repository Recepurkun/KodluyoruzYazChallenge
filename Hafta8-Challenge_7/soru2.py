"""
🌟Medium:  Kullanıcıdan aldığınız bir sayının basamaklarının toplamını hesaplayan bir kod parçacığı yazar mısın?
"""
def basamaklariniTopla(sayi):
    toplam = 0
    for i in str(sayi):
        toplam += int(i)
    return toplam

sayi = input("Bir sayi giriniz: ")
print(basamaklariniTopla(sayi))