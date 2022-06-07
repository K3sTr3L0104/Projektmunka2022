import random
#Projektmunka
#Reszese: Nagy Eniko es Karakas Oliver Roland
#Feladat: LOTTÓ
#Fájl megnyitás olvasásra (Nagy Enikő):

file=open("lottoszamok.txt","r")

#Első sor kiíratása (Nagy Enikő):
print(file.readline())
#Ötös Lottó számok generálása: (Karakas Roland):
lottoszam1= random.randint(1,100)
lottoszam2= random.randint(1,100)
lottoszam3= random.randint(1,100)
lottoszam4= random.randint(1,100)
lottoszam5= random.randint(1,100)
print(lottoszam1)
print(lottoszam2)
print(lottoszam3)
print(lottoszam4)
print(lottoszam5)
#Alap pénzösszeg beállítása (Nagy Enikő):

alapPenz=5000

#lottónyeremények kiírása(Nagy Enikő):
print("2 találatos nyeremény összege:15.000Ft")
print("3 találatos nyeremény összege:50.000Ft")
print("4 találatos nyeremény összege:50.0000Ft")
print("5 találatos nyeremény összege:15.000000Ft")

#Lottószelvény választása, illetve annak az ára levonása (Karakas Roland):

OtosLotto = 500
print("Ötös lottó ára: 500 Ft")
hanyatKersz = int(input("Hány ötös lottó jegyet szeretnél venni:"))
for i in range(hanyatKersz):
    alapPenz = alapPenz-OtosLotto
print("A lottószelvény vásárlása után ennyi pénzed maradt:", alapPenz,"Ft")


#Bekérni a felhasználó nevét, korát (Nagy Enikő):

nev=input("Add meg a nevedet:")
kor=int(input("Add meg az életkorod:"))







#Ha nem elég idős, akkor ne engedje lottózni (Nagy Enikő):
if kor<18:
   print("nem lottózhat")
else:
   print("lottózhat")






#Bekérni a felhasználótól 5 számot (Nagy Enikő):

bekert_szam1=int(input("Adj meg egy számot:"))
bekert_szam2=int(input("Adj meg egy számot:"))
bekert_szam3=int(input("Adj meg egy számot:"))
bekert_szam4=int(input("Adj meg egy számot:"))
bekert_szam5=int(input("Adj meg egy számot:"))








#Megnézni, hogy hány találata van (Karakas Roland, Nagy Enikő):
lista = []
talalatok = 0
if bekert_szam1 == lottoszam1 or bekert_szam1 == lottoszam2 or bekert_szam1 == lottoszam3 or bekert_szam1 == lottoszam4 or bekert_szam1 == lottoszam5:
   talalatok = talalatok + 1
   lista.append(bekert_szam1)

if bekert_szam2 == lottoszam1 or bekert_szam2 == lottoszam2 or bekert_szam2 == lottoszam3 or bekert_szam2 == lottoszam4 or bekert_szam2 == lottoszam5:
   talalatok = talalatok + 1
   lista.append(bekert_szam2)

if bekert_szam3 == lottoszam1 or bekert_szam3 == lottoszam2 or bekert_szam3 == lottoszam3 or bekert_szam3 == lottoszam4 or bekert_szam3 == lottoszam5:
   talalatok = talalatok + 1
   lista.append(bekert_szam3)

if bekert_szam4 == lottoszam1 or bekert_szam4 == lottoszam2 or bekert_szam4 == lottoszam3 or bekert_szam4 == lottoszam4 or bekert_szam4 == lottoszam5:
   talalatok = talalatok + 1
   lista.append(bekert_szam4)

if bekert_szam5 == lottoszam1 or bekert_szam5 == lottoszam2 or bekert_szam5 == lottoszam3 or bekert_szam5 ==  lottoszam4 or bekert_szam5 == lottoszam5:
   talalatok = talalatok + 1
   lista.append(bekert_szam5)

print("Neked összesen", talalatok,"találatod van!")
#Feltételek,ciklusok létrehozása (Nagy Eniko, Karakas Roland):















#Új fájlba íratni a versenyző nevét, korát, és hogy hány számot talált el, illetve hogy mennyit nyert (Karakas Roland):
file1 = open("talalatok.txt", "w", encoding="utf_8")
file1.write(nev)
file1.write(str(kor))
file1.write(str(talalatok))
file1.write(mennyitNyert)



#Az új fájból kiíratni a versenyző nevét, és a helyes találatokat (Karakas Roland, Nagy Enikő):
