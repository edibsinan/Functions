# 1. Bir Sayının Karesini Hesaplama
# Fonksiyon yazmadan ve yazarak bir sayının karesini hesaplayan bir fonksiyon oluşturun.
# Soru:
# Verilen bir sayının karesini hesaplayan bir fonksiyon yazınız.
#  Eğer hiçbir argüman verilmezse, 
# varsayılan olarak 10'un karesini döndürsün.
# Ekstra: Üç farklı sayıyı çarpan bir fonksiyon yazınız 
# ve en az bir argüman belirtmeden çağırın.
#
 
# def sayinin_karesi(x):
#     sonuc = x ** 2
#     # print(sonuc + 1)
#     return sonuc
# print(sayinin_karesi(5) + 1)

# 2. İki Sayıyı Toplama
# İki sayıyı toplamak için bir fonksiyon oluşturun.
# Soru:
# topla(a, b) adında bir fonksiyon yazınız. 
# Bu fonksiyon, iki sayıyı toplamalı ve sonucu döndürmelidir.

# def toplama(s1, s2):
#     return s1 + s2
# label = toplama(1, 2)
# print(label)



# 3. Faktöriyel Hesaplama
# Bir sayının faktöriyelini hesaplayan bir fonksiyon yazınız.
# Soru:
# factorial(number) adlı bir fonksiyon yazınız. 
# Bu fonksiyon verilen sayının faktöriyelini hesaplamalıdır. 0 için 1 döndürmelidir.
# def factorial(number):
#     if number == 0:
#         return 1
#     else:
#         sonuc = 1
#         for i in range(1, number+1):
#             sonuc = sonuc * i
#         return sonuc
# print(factorial(5))

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return factorial(n-1) * n
# print(factorial(5))


# 4. Listede En Büyük Sayıyı Bulma
# Bir liste içindeki en büyük sayıyı bulan bir fonksiyon yazınız.
# Soru:
# en_buyuk_sayi(liste) adlı bir fonksiyon oluşturun.
# Bu fonksiyon verilen bir listenin içindeki en büyük sayıyı döndürmelidir.
# Örnek Girdi: [2, 3, 1, 7, 4, 2]
# Beklenen Çıktı: 7
# def en_buyuk_sayi(liste):
#     bSayi = liste[0]
#     for i in range(1, len(liste)):
#         if bSayi<liste[i]:
#             bSayi = liste[i]
#     return bSayi
# print(en_buyuk_sayi([2, 3, 1, 7, 4, 2]))



# 5. Emeklilik Yaşı Hesaplama
# Kullanıcının yaşı ve cinsiyetine göre emekliliğe kalan yılı hesaplayan 
# bir fonksiyon yazınız.
# Soru:
# emeklilik_yasi_hesapla(kadinMi, yas) fonksiyonunu yazınız.
# Eğer kişi kadınsa, emeklilik yaşı 55.
# Eğer kişi erkekse, emeklilik yaşı 63.
# Kişi emekli olmuşsa, 'Zaten emekli' döndürün.
# def yas_hesaplama(dogum_yili):
#    return 2025 - dogum_yili  # Varsayım: Güncel yıl 2025

# def emeklilik_yasi_hesaplama(dogum_yili, cinsiyet, isim):
#    yas = yas_hesaplama(dogum_yili)
#    if cinsiyet.upper() == "E":  # Erkek için kontrol
#        emeklilik_yasi = 63
#    elif cinsiyet.upper() == "K":  # Kadın için kontrol
#        emeklilik_yasi = 55
#    else:
#        print("Geçersiz cinsiyet girdiniz. Lütfen 'K' veya 'E' giriniz.")
#        return
#    kalan_yil = emeklilik_yasi - yas
#    if kalan_yil > 0:
#        print(f"Merhaba {isim}, emekliliğinize {kalan_yil} yıl kaldı.")
#    else:
#        print(f"Merhaba {isim}, zaten emekli oldunuz!")

# # Kullanıcı girişi
# dogum_yili = int(input("Lütfen doğum yılınızı giriniz: "))
# cinsiyet = input("Lütfen cinsiyetinizi giriniz (K/E): ")
# isim = input("Lütfen adınızı yazınız: ")
# Fonksiyonu çağır
# emeklilik_yasi_hesaplama(1995, 'e', 'mehmet')


# 6. Recursive Faktöriyel Hesaplama
# Faktöriyel hesaplamasını bir döngü yerine özyineleme (recursion) kullanarak yapınız.
# Soru:
# recursive_factorial(number) fonksiyonunu yazınız. 
# Bu fonksiyon özyineleme ile faktöriyel hesaplamalıdır.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return factorial(n-1) * n
# print(factorial(5))


# 7. Kelimeleri Ters Çevirme
# Bir metindeki her kelimeyi ters çeviren bir sistem oluşturun.
# Soru:
# kelimelere_ayir(metin): Verilen metni kelimelere ayıran bir fonksiyon yazınız.
# kelimeleri_ters_cevir(kelimeler): Kelimeleri ters çeviren bir fonksiyon yazınız.
# yeni_metin_olustur(ters_kelimeler): 
# Ters çevrilmiş kelimelerle yeni bir metin oluşturun.
# Örnek Girdi: "Ali ata bak"
# Beklenen Çıktı: "ilA ata kab"
# def kelimere_ayir(metin):
#     return metin.split(' ')
# words = kelimere_ayir('ali ata bak')
# def kelimeleri_ters_cevir(kelimeler):
#     return [kelime[::-1] for kelime in kelimeler]
# tersKelimeler = kelimeleri_ters_cevir(words)
# def yeni_metin_olustur(ters_kelimeler):
#     return " ".join(ters_kelimeler)
# print(yeni_metin_olustur(tersKelimeler))


# 8. Kelime Frekansı Hesaplama
# Bir metindeki kelimelerin kaç kez geçtiğini hesaplayan bir fonksiyon yazınız.
# Soru:
# kelime_frekansi(metin) adlı bir fonksiyon yazınız.
# Örnek Girdi: "bu bir test bu sadece bir test"
# Beklenen Çıktı: {'bu': 2, 'bir': 2, 'test': 2, 'sadece': 1}
# def kelime_frekansi(metin):
#     kelimeler = metin.split(' ')
#     frekans = {}
#     for kelime in kelimeler:
#         kelime1 = kelime.lower()
#         if kelime1 in frekans:
#             frekans[kelime1] += 1
#         else:
#             frekans[kelime1] = 1
#     return frekans
# print(kelime_frekansi("bu bir test bu sadece bir test"))

# 9. Lambda ile Toplama
# Anonim (lambda) fonksiyonlar kullanarak işlemler yapınız.
# Soru:
# İki sayıyı toplayan bir lambda fonksiyonu oluşturun.

# toplama = lambda x, y: x + y
# sonuc = toplama(1, 2)
# print(sonuc)



# # Verilen bir sayının karesini hesaplayan bir lambda fonksiyonu yazınız.
# karesi = lambda x: x ** 2
# print(karesi(5))



# 10. Bir Listenin Ortalamasını Hesaplama
# Verilen bir listenin ortalamasını hesaplayınız.
# Soru:
# Örnek Girdi: [1, 5, 10, 2, 20]
# Beklenen Çıktı: 7.6
# def ortalama(liste):
#     ortalama1 = sum(liste) / len(liste)
#     return ortalama1
# print(ortalama([1, 5, 10, 2, 20]))
# ortalamaLambda = lambda liste: sum(liste) /len(liste)
# print(ortalamaLambda([1, 5, 10, 2, 20]))

# 11. Lambda ile Filtreleme İşlemleri
# Bir liste üzerinde lambda ile filtreleme yapınız.
# Soru:
# Bir listede sadece tek sayıları filtreleyen bir lambda ifadesi yazınız.
# Negatif sayıları filtreleyen bir lambda ifadesi yazınız.
# Örnek Girdi: [-1, 4, 8, 14, -5]
# Beklenen Çıktı: [-1, -5]
# liste = [1, 5, 10, 2, 20]
# tekSayilar = filter(lambda x: x%2 != 0, liste)

# print(list(tekSayilar))

# def tekSayilar1(sayi):
#     return sayi%2 == 1
# liste = [1, 5, 10, 2, 20]
# tekSayilar = list(filter(tekSayilar1, liste))
# print(tekSayilar)
# liste = [-1, 4, 8, 14, -5]
# def negatifSayi(sayi):
#     return sayi < 0
# negatifSayilar1 = list(filter(negatifSayi, liste))

# negatifSayilar = list(filter(lambda sayi: sayi<0, liste))
# print(negatifSayilar)

# 12. Reduce ile Liste İşlemleri
# Bir listedeki elemanlara toplama ve çarpma işlemi uygulayınız.
# Soru:
# Bir listenin elemanlarının toplamını ve çarpımını reduce kullanarak hesaplayınız.
# Listedeki en büyük sayıyı reduce ile bulunuz.
# Örnek Girdi: [1, 5, 3, 9, 2]
# Beklenen Çıktı:
# Toplam: 20
# Çarpım: 270
# En Büyük: 9

# from functools import reduce

# toplam = reduce(lambda x, y: x+y, [1, 5, 3, 9, 2])
# print(toplam)
# carpma = reduce(lambda x, y: x*y, [1, 5, 3, 9, 2])
# print(carpma)
# enbuyuk = reduce(lambda x, y: x if x>y else y, [1, 5, 3, 9, 2])
# print(enbuyuk)

# 13. Fibonacci Dizisi Oluşturma
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, verilen bir sayı kadar 
# Fibonacci dizisi elemanını bir liste olarak döndürsün. 
# Örneğin, fibonacci(10) çağrıldığında 10 elemanlı bir Fibonacci dizisi üretmelidir.



# 14. Bir Sayının Asal Olup Olmadığını Kontrol Etme
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir sayının asal olup olmadığını kontrol etsin 
# ve sonuç olarak True (asal) veya False (asal değil) döndürsün. 
# Örneğin, asal_mi(29) çağrıldığında True, asal_mi(10) çağrıldığında False döndürmelidir.
# def asal_mi(sayi):
#     if sayi < 2:
#         return False
#     for i in range(2, sayi):
#         if sayi % i == 0:
#             return False
#     return True
# print(asal_mi(2))


# Soru: Bir e-ticaret sitesinde, kullanıcının sepetindeki ürünlerin 
# toplam fiyatını hesaplayan ve 
# varsa indirimleri uygulayan bir Python fonksiyonu yazın.
# Fonksiyon adı: sepet_hesapla(sepet, indirim_kodu)
# Parametreler:
# sepet: Bir sözlük, her anahtar ürün adını ve değer olarak ürünün fiyatını içeren.
# indirim_kodu: Bir string, belirli indirim kodlarını içeren 
# ("INDIRIM10" %10 indirim, "INDIRIM20" %20 indirim).
# Beklenen Çıktı: Fonksiyon toplam fiyatı hesaplamalı ve 
# varsa indirimi uygulamalıdır. Örneğin, eğer sepet şu şekildeyse:
# sepet = {
#     'laptop': 1500,
#     'kulaklik': 200,
#     'mouse': 50
# }
# ve indirim kodu "INDIRIM10" ise, sepet_hesapla(sepet, "INDIRIM10") 
# fonksiyonu 1575 sonucunu döndürmelidir (1750'den %10 indirim uygulandıktan sonra).
# ornekSepet = {
#     'laptop': 1500,
#     'kulaklik': 200,
#     'mouse': 50
# }
# def sepet_hesapla(sepet, indirim_kodu):
#     toplam = 0
#     for _, value in sepet.items():
#         toplam += value
#     if indirim_kodu == 'INDIRIM10':
#         toplam = toplam - (toplam * 0.10)
#         return toplam 
#     elif indirim_kodu == 'INDIRIM20':
#         return toplam * 0.80
#     else:
#         return 'Hatali indirim kodu'
# print(sepet_hesapla(ornekSepet, indirim_kodu='INDIRIM10'))
# def sepet_hesapla(sepet, indirim_kodu):
#     toplam = sum(sepet.values())
#     if indirim_kodu == 'INDIRIM10':
#         sonuc = toplam - (toplam * 0.10)
#     elif indirim_kodu == 'INDIRIM20':
#         sonuc = toplam * 0.80
#     else:
#         return 'Hatali indirim kodu'
#     return sonuc
# print(sepet_hesapla(ornekSepet, indirim_kodu='INDIRIM10'))

# 15. Liste Elemanlarını Çift mi Tek mi Diye Ayırma
# Soru:
# Bir liste içindeki elemanları "Çift" veya "Tek" olarak belirten bir fonksiyon yazınız. 
# Fonksiyon, liste elemanlarının sırasına göre "Çift" ya da "Tek" stringlerini 
# döndüren bir liste oluştursun. Örneğin, cift_tek_ayir([1, 2, 3, 4, 5]) 
# çağrıldığında ['Tek', 'Çift', 'Tek', 'Çift', 'Tek'] döndürmelidir.
# liste = [1, 2, 3, 4, 5]
# def cift_tek_ayir(liste):
#     return ['Cift' if x % 2 == 0 else 'Tek' for x in liste ]   
# print(cift_tek_ayir([1, 2, 3, 4, 5]))

# print(list(map(lambda x: 'Cift' if x%2 == 0 else 'Tek', liste)))
# print(list(map(lambda x: 'Çift' if x % 2 == 0 else 'Tek', liste)))




# 16. Liste Elemanlarını Çift Sayılar ve Tek Sayılar Olarak Gruplama
# Soru:
# Bir listeyi iki ayrı listeye ayıran bir fonksiyon yazınız. İlk liste sadece çift sayıları, ikinci liste ise sadece tek sayıları içermelidir. Fonksiyon bu iki listeyi bir tuple (demet) olarak döndürsün. Örneğin, gruplandir([1, 2, 3, 4, 5]) çağrıldığında ([2, 4], [1, 3, 5]) döndürmelidir.

# 17. Bir Listenin Tersini Döndürme
# Soru:
# Bir listeyi ters çeviren bir fonksiyon yazınız. 
# Örneğin, ters_cevir([1, 2, 3, 4, 5]) çağrıldığında [5, 4, 3, 2, 1] döndürmelidir.
# def ters_cevir(listem):
#     return listem[::-1]
# print(ters_cevir(listem = [1, 2, 3, 4, 5]))
# 18. Bir Listenin Ortalamasını Hesaplama
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir listenin elemanlarının aritmetik ortalamasını hesaplasın ve sonucu döndürsün. Örneğin, liste_ortalama([10, 20, 30]) çağrıldığında 20.0 döndürmelidir.
# 19. Listedeki En Küçük Elemanı Bulma
# Soru:
# Bir fonksiyon yazınız. Bu fonksiyon, bir liste içindeki en küçük elemanı döndürsün. Örneğin, en_kucuk([10, 20, 5, 15]) çağrıldığında 5 döndürmelidir.
# 20. Liste İçindeki Harflerin Frekansını Bulma
# Soru:
# Bir string içindeki harflerin frekansını hesaplayan bir fonksiyon yazınız. Fonksiyon, harfleri ve her bir harfin kaç kez tekrar ettiğini bir dictionary (sözlük) olarak döndürmelidir. Örneğin, harf_frekansi("hello world") çağrıldığında {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1} döndürmelidir.


# iki sayinin karesini alan ve onlari verilen deger ile carpan fonksiyon

# def kareToplama(ilkSayi=1, ikinciSayi=1, carpanDeger=1, export1=0):
#     if export1 == 0:
#         print('sonuc=',ilkSayi**2 * carpanDeger, ikinciSayi**2 * carpanDeger)
#     else:
#          print(ilkSayi**2 * carpanDeger, ikinciSayi**2 * carpanDeger)
# kareToplama(5,3, 3, 1)