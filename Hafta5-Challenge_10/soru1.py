"""
🙌🏼 Easy: Bir dizi tanımladıktan sonra bu dizinin içinden en büyük sayıyı bulan kod parçacığını yazar mısın?
"""
dizi = [5,8,2,3,7,9,1]
print("Ilk hali: ", dizi)
dizi.sort()
print("Son hali: ", dizi)
print("En büyük elaman: ", max(dizi))

#!-------------------------------------------------------------------------------------------------------

def max_numarayi_bul(arr):
    if len(arr) == 0:
        print("dizi bos")
    
    max_numara = arr[0] #? dizinin ilk elemanını max_numara olarak tutalım

    for num in arr: #* dizinin icerisindeki her elemanı dolaşalım 
        if num > max_numara: #* eğer üstünden geçtiğimiz eleman üstte atadığımız max_numaradan(dizinin ilk elemanından yani) büyükse
            max_numara = num    #* artık bu üstünde olduğumuz eleman max_numara olacak

    return max_numara


sayiArrayi = [10, 5, 23, 8, 45, 67, 12, 92 ,17, 23,101]
enBuyukNumara = max_numarayi_bul(sayiArrayi)
print("\n En büyük sayi: " , enBuyukNumara)