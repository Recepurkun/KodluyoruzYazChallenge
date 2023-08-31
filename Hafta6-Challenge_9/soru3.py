"""
💪🏻Hard: Kullanıcıdan bir cümle girmesini ve bu cümlenin içinde ikileme olup olmadığını bulan bir kod parçası yazmanızı istiyorum.😀(Not: burada ikilemeleri sadece arka arkaya yazılmış aynı kelimeler olarak düşünmenizi istiyorum.)

🗝️     Kullanıcı metin: at ağır ağır ilerliyordu.
         Cevap: ikilime kullandınız.
         Kullanıcı metin: Yürüyerek gidiyorduk.
         Cevap: İkileme bulunamadı.
"""

def ikilem_bul(kullaniciMetin):
    kelimeler = kullaniciMetin.lower().split()
    for i in range(len(kelimeler)-1):
        if kelimeler[i] == kelimeler[i+1]:
            return "İkileme kullandiniz"
    return "İkileme bulunamadi"

metin = input("Bir metin giriniz: ")
cevap = ikilem_bul(metin)
print(cevap)