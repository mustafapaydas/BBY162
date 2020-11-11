 al = input("Sayı Giriniz: ")
  bul = len(str(al))
  say = 0
  for i in range(bul):
    say = say + int(al[i]) ** int(bul)
  if say == al:
    print("{} armstrong sayısıdır".format(al))
  else:
    print("{} armstrong sayısı değildir.".format(al))
