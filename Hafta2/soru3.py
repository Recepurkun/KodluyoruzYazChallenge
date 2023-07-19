"""
💪🏻Hard: Bir şirket, bir ürünü üretmek ve satmak için belirli bir maliyet ve satış fiyatı hesaplamaktadır. 
Şirketin bir ürün için birim maliyeti ve birim satış fiyatı verildiğinde, kaç adet ürünün satılması durumunda 
şirketin kar edeceğini bulmanı istiyorum. Sakin ol şimdi biraz daha detaylandıracağım 😀

🗝️ Bir adet cost ve price değişkeni oluşturmalısın. Bunları kullanıcıdan istemene gerek yok. Örneğin cost:100 price:150 olması 
durumunda 3 ürün satıldığında kâr edilmeye başlanmış olur. Cost price’dan her zaman düşük olmalıdır, eğer aynı veya yüksek olursa 
kâr edilemez uyarısı dönmelidir.

Örnek çıktı aşağıdaki gibi olmalıdır 🤗

Cost: 100

Price: 150

Kaç ürün satılırsa kâr edilir?: 3
"""

cost = 100 #maliyet fiyatı
price = 150 #satış fiyatı

if cost >= price:
    print("Bu fiyatlar ile kar edilemez.")
else:
    kar = price - cost
    if kar < 0:
        print("kar edilemiyor")
    else:
        adet = (cost // kar) + 1
        print("Cost:", cost)
        print("Price:", price)
        print("En az", adet, "adet satılınca kâr edilir.")

#kar şartı(300 TL gibi...) koyarak yapılan bir çözüm
# if (price >= cost):
#     adet = 1
#     kar = (price - cost) * adet
#     print(kar)
#     while kar < 300:
#         adet+=1
#         kar = (price - cost) * adet
#         if(kar >= 300):
#             print("Cost:", cost)
#             print("Price:", price)
#             print("En az", adet, "adet satılınca kâr edilir.")
#             break
#     else:
#         print("Bu fiyatlar ile kar edilemez. 1 ")
# else:
#     print("Bu fiyatlar ile kar edilemez. 2")