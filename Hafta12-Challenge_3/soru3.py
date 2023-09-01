"""
💪🏻Hard: Bir sınıfta 30 öğrenci bulunmaktadır. Öğrencilerden kaç farklı şekilde 4 kişi seçilebilir?😀
🗝️ Bu problemi çözen kodu yazmanı istiyorum🤗
"""
import math

toplam_ogrenci = 30  #? Toplam öğrenci sayısı
secilecek_ogrenci = 4 #? Seçilecek öğrenci sayısı
secim_sayisi = math.comb(toplam_ogrenci, secilecek_ogrenci) #? Kombinasyon hesabı
print(f"{toplam_ogrenci} öğrenciden {secilecek_ogrenci} kişi {secim_sayisi} farklı şekilde seçilebilir")