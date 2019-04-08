sorular = ["Balıklıgöl aşağıdaki illerimizden hangisine aittir?",\
            "Türkiye Cumhuriyeti\' nin ilk cumhurbaşkanı kimdir?",\
            "Çanakkale Zaferi hangi savaşta kazanılmıştır?",\
            "Güneş sisteminde Güneşe en yakın gezegen hangisidir?",\
            "Aşağıdakilerden hangisi Yaşar Kemal\'in eseridir?"]

puan = 0

cevaplar = ['c','a', 'b', 'c', 'a']

cevap_A = ["Adana",\
           "Mustafa Kemal Atatürk",\
           "Balkan Savaşları",\
           "Mars",\
           "İnce Memed"]

cevap_B = ["Bursa",\
           "Fevzi Çakmak",\
           "I. Dünya Savaşı",\
           "Jüpiter",\
           "Falaka"]

cevap_C = ["Şanlıurfa",\
           "İsmet İnönü",\
           "Kurtuluş Savaşı",\
           "Merkür",\
           "Ekmek Kavgası"]

for i in range(len(sorular)):

    print("Soru "+str(i+1)+":"+sorular[i])
    print("A) " + cevap_A[i])
    print("B) " + cevap_B[i])
    print("C) " + cevap_C[i])

    cevap = input("Cevabınızı giriniz:")
    if(cevaplar[i] == cevap.lower()):
        print("Tebrikler")
        puan += 3
    else:
        print("Üzgünüm! Daha çok çalışmalısınız")
        puan -=1

print("Puanınız: "+str(puan*100/15))







