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
#Ellenőrző kiíratások
#print(lottoszam1)
#print(lottoszam2)
#print(lottoszam3)
#print(lottoszam4)
#print(lottoszam5)
#Alap pénzösszeg beállítása (Nagy Enikő, Karakas Roland):
alapPenz=5000
print("A pénztárcádban ennyi pénz található:", alapPenz)
#lottónyeremények kiírása(Nagy Enikő):
ketTalalat = 15000
haromTalalat = 50000
negyTalalat = 500000
otTalalat = 15000000
print("2 találatos nyeremény összege:15.000Ft")
print("3 találatos nyeremény összege:50.000Ft")
print("4 találatos nyeremény összege:500.000Ft")
print("5 találatos nyeremény összege:15.000.000Ft")
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
   exit()
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
#Új fájlba íratni a versenyző nevét, korát, és hogy hány számot talált el, illetve hogy mennyit nyert (Karakas Roland):
file1 = open("talalatok.txt", "w", encoding="utf_8")
file1.write(nev)
file1.write(str(kor))
file1.write(str(talalatok))
#Feltételek,ciklusok létrehozása (Nagy Eniko, Karakas Roland):

if talalatok == 2:
   alapPenz=alapPenz+15000
   file1.write(ketTalalat)
if talalatok == 3:
   alapPenz=alapPenz+50000
   file1.write(str(haromTalalat))
if talalatok == 4:
   alapPenz=alapPenz+500000
   file1.write(str(negyTalalat))
if talalatok == 5:
   alapPenz=alapPenz+15000000
   file1.write(str(otTalalat))

#Az új fájból kiíratni a versenyző nevét, és a helyes találatokat (Karakas Roland, Nagy Enikő):
file2 = open("talalatok.txt" ,"r", encoding="utf_8")
for i in file2:
   print(file2.readline())
