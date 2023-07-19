"""
🙌🏼 Easy: Kullanıcıdan bir sayı almanızı ve bu sayının asal olup olmadığını kullanıcıya söylemenizi istiyorum.

🗝️ Asal sayıların ortak özelliği kendisine ve bire kalansız bölünmesidir. 2’nin de asal sayı olduğunu programında unutma 😀Bütün asal sayıları tanımlamak ve 
kontrol etmek yerine sayının asal sayı olup olmadığını matematik işlemleriyle anlayabilirsin 😉

Örnek çıktı aşağıdaki gibi olmalıdır 🤗
>Bir sayi girin: 17
>17 asal bir sayidir.

>>Bir sayi girin: 10
>10 asal bir sayi degildir.
"""

sayi = int(input("Bir sayi giriniz: "))

#for dongusu ile
if sayi > 1:
    for i in range(2,sayi):
        if(sayi % i == 0 ):
            print(f"{sayi}, asal sayi değildir")
            break
    else:
        print(f"{sayi}, asal bir sayidir.")
else:
   print(f"{sayi}, asal sayi değildir.")

#while dongusu
# if sayi > 1:
#     i = 2
#     kontrol = 0
#     while (i < sayi):
#         if(sayi % i == 0):
#             kontrol+=1
#         i+=1

#     if(kontrol!=0):
#         print(f"{sayi}, asal sayi değildir.")
#     else:
#         print(f"{sayi}, asal bir sayidir.")

# else:
#     print(f"{sayi}, asal sayi değildir.")