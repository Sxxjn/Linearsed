from Tund5_Kasutataja_fun import *

#1
while True:
    try:
        a=float(input("Arv1: "))
        break
    except:
        print("Viga! Sisesta arv")
while True:
    try:
        b=float(input("Arv2: "))
        break
    except:
        print("Viga! Sisesta arv")
while True:
    try:
        t=input("Tehe: ")
        break
    except:
        print("Viga! Sisesta (/);(*);(+);(-)")
vastus=arithmetic(a,b,t)
print(vastus)


# 2
aasta=int(input("Mis aasta tahad kontrollida: "))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigasta")
    else:
        print(f"{aasta} ei ole liigasta")

#3 square() kasutaimine
#Kontroll while True ja try except
while True:
    try:
        a=float(input("Ruudu külje pikkus: "))
        break
    except:
        print("Viga! Sisesta arv")
S,P,d=square(a)
print(f"Ruudu pindala on {S}, ümbermõõt on {P} ja diagonaal on {d}")

#4
while True:
        try:
            a=int(input("Kuu number: "))
            break
        except:
            print("Viga! Sisesta arv")
vastus=season(a)
print(vastus)

#5
while True:
    try:
        aastad=int(input("Sisesta aasta: "))
        break
    except:
        print("Viga! Sisesta arv")
while True:
    try:
        summa=float(input("Sisesta summa:"))
        break
    except:
        print("Viga! Sisesta arv")
vastus=bank(aastad,summa)
print(f"lõpus tagastab {bank} eurot")

#6
if is_prime():
    print("True")
else:
    print("False")

#7
try:
    päev=int(input("Sisesta päev: "))
    kuu=int(input("Sisesta kuu: "))
    aasta=int(input("Sisesta aasta: "))
    v=date(päev,kuu,aasta)
    print(v)
except:
    print("viga!")