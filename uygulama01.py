#soru_1
puan = 0
cevaplar = ['c','a', 'b', 'c', 'a']
soru_1 = "Balıklıgöl aşağıdaki illerimizden hangisine aittir? \n A)Bursa B)Mardin C)Şanlıurfa"
cevap = input(soru_1 +   "\nLütfen cevap giriniz : ")
if cevaplar[0] == cevap.lower():
    print("Doğru şıkkı işaretlediniz")
    puan += 1
else:
    print("Üzgünüm yanlış şıkkı işaretlediniz. Biraz daha genel kültür çalışmalısınız")

input("Diğer soru için enter\'a basın")

#soru2
soru_2 = "Türkiye Cumhuriyeti\' nin ilk cumhurbaşkanı kimdir \nA)Mustafa Kemal Atatürk B)İsmet İnönü C)Fevzi Çakmak"
cevap = input(soru_2 +   "\nLütfen cevap giriniz: ")
if cevaplar[1] == cevap.lower():
    print("Doğru şıkkı işaretlediniz.")
    puan += 1
else:
    print("Yanlış şıkkı işaretlediniz. Biraz daha Yakın Tarih çalışmalısınız")

input("Diğer soru için enter\'a basın")


#soru_3
soru_3 = "Çanakkale Zaferi hangi savaşta kazanılmıştır? \n A)Balkan Savaşları B)I.Dünya Savaşı C)Kurtuluş Savaşı"
cevap = input(soru_3 +   "\nLütfen cevap giriniz: ")
if cevaplar[2] == cevap.lower():
    print("Doğru şıkkı işaretlediniz")
    puan += 1
else:
    print("Yanlış şıkkı işaretlediniz. Biraz daha Tarih çalışmalısınız")

input("Diğer soru için enter\'a basın")

#soru_4
soru_4 = "Güneş sisteminde Güneşe en yakın gezegen hangisidir? \n A)Dünya B)Venüs C)Merkür"
cevap = input(soru_4 +   "\nLütfen cevap giriniz: ")
if cevaplar[3] == cevap.lower():
    print("Doğru şıkkı işaretlediniz")
    puan += 1
else:
    print("Yanlış şıkkı işaretlediniz. Biraz daha Fen Bilimleri çalışmalısınız")

input("Diğer soru için enter\'a basın")

#soru_5
soru_5 = "Aşağıdakilerden hangisi Yaşar Kemal\'in eseridir \n A)İnce Memed B)Ekmek Kavgası C)Karartma Geceleri"
cevap = input(soru_5 +   "\nLütfen cevap giriniz: ")
if cevaplar[4] == cevap.lower():
    print("Doğru şıkkı işaretlediniz")
    puan += 1
    if puan == 5:
        print("Başarılı " + " " + str(puan * 20))
    elif puan == 4:
        print("İyi" + " " + str(puan * 20))
    elif puan == 3:
        print("Orta" + " " + str(puan * 20))
    elif puan == 2:
        print("Kötü" + " " + str(puan * 20))
    elif puan == 1:
        print("Çok Kötü" + " " + str(puan * 20))
    elif puan == 0:
        print("Berbat" + " " + str(puan * 20))




else:
    print("Yanlış şıkkı işaretlediniz. Biraz daha Edebiyat çalışmalısınız")
    if puan == 5:
        print("Başarılı " + " " + str(puan * 20))
    elif puan == 4:
        print("İyi")
    elif puan == 3:
        print("Orta" + " " + str(puan * 20))
    elif puan == 2:
        print("Kötü" + " " + str(puan * 20))
    elif puan == 1:
        print("Çok Kötü" + " " + str(puan * 20))
    elif puan == 0:
        print("Berbat" + " " + str(puan * 20))