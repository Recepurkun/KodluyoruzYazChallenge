"""
🌟Medium: Kullanıcıdan bir kelime almanız gerekiyor. Bu kelimenin harflerini büyük harflere dönüştüren bir program yazmanızı istiyorum.

🗝️ C dilinde toupper() fonksiyonu harfleri büyük harfe dönüştürür.

Örnek çıktı aşağıdaki gibi olmalıdır 🤗

Orijinal kelime: Merhaba

Büyük harfli kelime: MERHABA
"""

kelime = input("Bir kelime giriniz: ")
print("Before: ",kelime)

kelime = kelime.upper()
print("After: ",kelime)