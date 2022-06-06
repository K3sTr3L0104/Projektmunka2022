import random
#Projektmunka
#Reszese: Nagy Eniko es Karakas Oliver Roland
#Feladat: LOTTÓ
#Fájl megnyitás olvasásra (Nagy Enikő):

file=open("lottoszamok.txt" "r")

#Első sor kiíratása (Nagy Enikő):
file.readline()

#Lottó számok generálása: (Karakas Roland):
lottoszam1= random.randint(1,100)
lottoszam2= random.randint(1,100)
lottoszam3= random.randint(1,100)
lottoszam4= random.randint(1,100)
lottoszam5= random.randint(1,100)
#Alap pénzösszeg beállítása (Nagy Enikő):






#Lottószelvény választása, illetve annak az ára levonása (Karakas Roland):








#Bekérni a felhasználó nevét, korát (Nagy Enikő):
nev=input("Add meg a nevedet:")
kor=input("Add meg az életkorod:")







#Ha nem elég idős, akkor ne engedje lottózni (Nagy Enikő):
if kor<18:
   print("nem lottózhat")
else:
   print("lottózhat")






#Bekérni a felhasználótól 5 számot (Nagy Enikő):










#Megnézni, hogy hány találata van (Karakas Roland, Nagy Enikő):








#Feltételek,ciklusok létrehozása (Nagy Eniko, Karakas Roland):















#Új fájlba íratni a versenyző nevét, és hogy hány számot talált el (Karakas Roland):





#Az új fájból kiíratni a versenyző nevét, és a helyes találatokat, és hogy melyik lottószelvényt választotta (Karakas Roland, Nagy Enikő):
