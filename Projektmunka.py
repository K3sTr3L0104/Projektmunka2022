import random
#Projektmunka
#Reszese: Nagy Eniko es Karakas Oliver Roland
#Feladat: LOTTÓ
#Fájl megnyitás olvasásra (Nagy Enikő):

file=open("uj szöveges dokumentum.txt" "r")

#Első sor kiíratása (Nagy Enikő):
for sor in file:
    print(sor)
file.seek(0,0)
sor1=file.readline().strip()


#Lottó számok generálása: (Karakas Roland):
lottoszam1= random.randint(1,100)
lottoszam2= random.randint(1,100)
lottoszam3= random.randint(1,100)
lottoszam4= random.randint(1,100)
lottoszam5= random.randint(1,100)
#Alap pénzösszeg beállítása (Nagy Enikő):






#Lottószelvény választása, illetve annak az ára levonása (Karakas Roland):








#Bekérni a felhasználó nevét, korát, születési évét (Nagy Enikő):
nev=input("Add meg a nevedet:")
kor=input("Add meg az életkorod:")
szulev=input("Add meg a születési éved:")







#Ha nem elég idős, akkor ne engedje lottózni (Nagy Enikő):






#Bekérni a felhasználótól 5 számot (Nagy Enikő):










#Megnézni, hogy hány találata van (Karakas Roland, Nagy Enikő):








#Feltételek,ciklusok létrehozása (Nagy Eniko, Karakas Roland):















#Új fájlba íratni a versenyző nevét, és hogy hány számot talált el (Karakas Roland):





#Az új fájból kiíratni a versenyző nevét, és a helyes találatokat, és hogy melyik lottószelvényt választotta (Karakas Roland, Nagy Enikő):
