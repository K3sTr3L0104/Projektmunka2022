import random
#Projektmunka
#Reszese: Nagy Eniko es Karakas Oliver Roland
#Feladat: LOTTÓ
#Fájl megnyitás olvasásra (Nagy Enikő):

file=open("lottoszamok.txt" "r")

#Első sor kiíratása (Nagy Enikő):
file.readline()
#Ötös Lottó számok generálása: (Karakas Roland):
lottoszam1= random.randint(1,100)
lottoszam2= random.randint(1,100)
lottoszam3= random.randint(1,100)
lottoszam4= random.randint(1,100)
lottoszam5= random.randint(1,100)
#Alap pénzösszeg beállítása (Nagy Enikő):

alapPenz=5000




#Lottószelvény választása, illetve annak az ára levonása (Karakas Roland):
OtosLotto = 500
print("Ötös lottó ára: 500 Ft")
hanyatKersz = int(input("Hány ötös lottó jegyet szeretnél venni:"))
for i in range(hanyatKersz):
    alapPenz = alapPenz-OtosLotto
print("A lottószelvény vásárlása után ennyi pénzed maradt:", alapPenz,"Ft")
#Bekérni a felhasználó nevét, korát (Nagy Enikő):
nev=input("Add meg a nevedet:")
kor=input("Add meg az életkorod:")







#Ha nem elég idős, akkor ne engedje lottózni (Nagy Enikő):
if kor<18:
   print("nem lottózhat")
else:
   print("lottózhat")






#Bekérni a felhasználótól 5 számot (Nagy Enikő):

lista = []
for i in range(5):
    szam=input("Adjon meg egy lottószámot:")
    lista.append(szam)








#Megnézni, hogy hány találata van (Karakas Roland, Nagy Enikő):








#Feltételek,ciklusok létrehozása (Nagy Eniko, Karakas Roland):















#Új fájlba íratni a versenyző nevét, és hogy hány számot talált el (Karakas Roland):





#Az új fájból kiíratni a versenyző nevét, és a helyes találatokat, és hogy melyik lottószelvényt választotta (Karakas Roland, Nagy Enikő):
