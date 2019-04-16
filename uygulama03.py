import random
import sys

adamCan = 5

kelime = ["kaplan" "aslan", "belgesel", "ayak", "ayakkabı", "hastane", "okul", "elektrik",
 "tahta", "makine", "kelime", "ceviz", "araba", "baklava", "kundura"]

kelime_tahmie = []
gizli_kelime = random.choice(kelime)
kelime_uzunluğu = len(gizli_kelime)
alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
harf_boyutu = []


def tanım():

    for karakter in gizli_kelime:
        kelime_tahmin.append("-")

    print("Tahmin edeceğin kelime", kelime_uzunluğu, "karakter")

    print("A-Z arasında bir harf seçmelisin\n\n")

    print(kelime_tahmin)



def tahmin():
    tahmin_edilen = 0

    while tahmin_edilen < 6:


        tahmin = input("Bir harf yaz\n").lower()


        if not tahmin in alfabe:
            print("A ve Z arasında bir harf yaz!")
        elif tahmin in harf_boyutu:
            print("Bu harfi zaten seçtin!")
        else:

            harf_boyutu.append(tahmin)
            if tahmin in gizli_kelime:
                print("Doğru!")
                for x in range(0, kelime_uzunluğu):
                    if gizli_kelime[x] == tahmin:
                        kelime_tahmin[x] = tahmin
                        print(kelime_tahmin)

                if not '-' in kelime_tahmin:
                    print("Bravo!")
                    break
            else:
                print("Üzgünüm! yanlış harf")
                tahmin_edilen += 1
                if tahmin_edilen == 10:
                    print("Üzgünüm, kaybettin! cevap:",         gizliKelime)


tanım()
tahmin()
