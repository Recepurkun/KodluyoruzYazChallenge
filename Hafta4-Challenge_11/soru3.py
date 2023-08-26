"""
💪🏻Hard: Bir sıralanmış dizide (örneğin, artan sırada) hedef bir sayının kaç kez tekrar ettiğini bulan bir kod parçacığı yazar mısın?
"""
ornekDizi = [2,3,4,5,5,5,6,7,8,8,9,9,9,9,9,9,9,10,10,10,10]
ornekDizi2 = [2, 3, 5, 5, 5, 7, 7, 8, 9, 9, 9, 10, 10, 11]

def hedefBul(sayi):
    sayac = 0
    for i in ornekDizi2:
        if(i == sayi):
            sayac+=1
    
    return sayac

sayi = int(input("bir sayi giriniz: "))
print(f"{sayi} sayısı {hedefBul(sayi)} kez tekrar ediyor.")