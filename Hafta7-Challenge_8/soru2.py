"""
🌟Medium:  Oluşturduğunuz bir dizinin medyanını hesaplayan bir kod parçacığı yazar mısınız?
🗝️ Medyan: Dizideki sayıları sıralandığında ortada bulunan değer.🤗
"""

def medyanHesapla(arr):
    arr = sorted(arr)
    veriAdedi = len(arr)
    if veriAdedi % 2 == 1:
        #bir tane medyan var - tek
        return arr[veriAdedi // 2]
    else:
        #2 tane medyan var demek - çift
        ort1 = arr[(veriAdedi // 2)]
        ort2 = arr[veriAdedi // 2 - 1]
        return  (ort1 + ort2) // 2
 
dizi = [10,20,30,40,45,50,55,60,65,70]
#dizi = [10,20,30,40,45,50,55,60,65]
print(medyanHesapla(dizi))
