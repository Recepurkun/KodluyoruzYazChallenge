#kütüphaneler
import time
import datetime
import locale
locale.setlocale(locale.LC_ALL, 'turkish')

"""
🙌🏼 Easy: Kullanıcının doğum tarihini alarak kaç yaşında olduğunu bulan bir algoritma yazmanızı istiyorum.
"""
dogum_tarihi = input("Lutfen dogum tarihinizi giriniz(Gun/Ay/Yil): ")
suanki_zaman = datetime.datetime.now()

tarih = datetime.datetime.strptime(dogum_tarihi, "%d %m %Y")

yas = (suanki_zaman.year - tarih.year)

# Doğum günü henüz geçmediyse yaş bir azalt
if tarih.month > suanki_zaman.month or (tarih.month == suanki_zaman.month and tarih.day > suanki_zaman.day ):
    yas-=1

print("Yaşiniz:",yas)