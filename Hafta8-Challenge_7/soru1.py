"""
🙌🏼 Easy: Kullanıcıdan alınan bir kelimenin uzunluğunu hesaplayan bir kod parçacığı yazar mısın?
"""
def kelimeUzunlukHesapla(kelime):   
    uzunluk = 0
    for i in kelime:
        uzunluk +=1
    print(uzunluk) 

kelime = input("Bir kelime giriniz: ")
kelimeUzunlukHesapla(kelime)