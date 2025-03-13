from random import *
#Näidised
# a=0
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# for i in range(0,10,1):
#     print(f"{i}. samm")
# print()
# for i in range(1,11,1):
#     print(f"{i}. samm")


#Ülesanne 1
# 1. variant
try:
    nimi=input("Sisesta oma nimi: ") 
except:
    print("Viga!!")
try:
    korda=int(input("Mitu korda? ")) #korda.isnumeric()  print(f"Ole tervitatud, {nimi}, {i+1} korda.")
    for i in range(korda):
        print(f"Ole tervitatud, {nimi}, {i+1} korda.")
except:
    print("Viga!!")
# 2. variant
while True:
    try:
        nimi=input("Sisesta oma nimi: ")
        if nimi.isalpha()==True: break 
    except:
        print("Viga!!")
while True:
    try:
        korda=int(input("Mitu korda? ")) #korda.isnumeric()
        if korda>0: break
    except:
        print("Viga!")
print("while true")
i=0
while True:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i} korda.")
    if i==korda: break
print("while tingimusega")
i=0
while i<korda:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i} korda.")


#Ülesanne 2
summa=0
j=0
while True:
    while True:
        try:
            a=float(input("a: "))
            break
        except:
            print("Viga!")
    summa+=a
    j+=1
    if j==10: break
print(f"Arvude summa: {summa}")
#-------
summa = 0
while True:
    number = input("Sisesta arv (vajuta Enter lõpetamiseks)")
    if number == "": break
    try:
        number=float(number)
        summa += number
    except:
        print("Viga!")
    print(f"Arvude summa: {summa}")


# # Ülesanne 3 
tehteid = 10
min_arv, max_arv = 1, 50
punktid = 0

for _ in range(tehteid):
    arv1 = (tehteid * 3) % (max_arv - min_arv + 1) + min_arv
    arv2 = (tehteid * 5) % (max_arv - min_arv + 1) + min_arv
    oige_vastus = arv1 + arv2
    katseid = 5
    
    while katseid > 0:
        kasutaja_vastus = int(input(f"Kui palju on {arv1} + {arv2}? "))
        
        if kasutaja_vastus == oige_vastus:
            print("Õige! Tubli!")
            punktid += 1
            break
        else:
            katseid -= 1
            if katseid > 0:
                print(f"Vale vastus. Proovi uuesti! Jäänud katseid: {katseid}")
            else:
                print(f"Kaotasid! Õige vastus oli {oige_vastus}.")

print(f"Mäng läbi! Sinu tulemus: {punktid}/{tehteid}")


#Ülesanne 4
for i in range(1,11,1):
    print(i)
print("Korrutustabel 1-10:")
for i in range(1,11,1):
    for j in range(1,11,1):
        print(f"{i} x {j} = {i*j}")


#Ülesanne 5
N=int(input("N: "))
for j in range(N):
    for i in range(N):
        if i==j or i==N-j:
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
print()


#Ülesanne 6
# 5x5 ruut tärnidest
for i in range(5):
    print("* " * 5)
print()
# Kasvav kolmnurk
for i in range(1, 6):
    print("* " * i)
print()
# Kahanev kolmnurk
for i in range(5, 0, -1):
    print("* " * i)


#Ülesanne 7
N=1
for i in range(4):
    N*=10
    N+=randint(0,9)
    print(N)


#Ülesanne 8
paaris_loendur = 0
paaritu_loendur = 0
for arv in range(1, 101):
    if arv % 2 == 0:
        print(f"{arv} - paaris")
        paaris_loendur += 1
    else:
        print(f"{arv} - paaritu")
        paaritu_loendur += 1
print(f"Paaris arvude arv: {paaris_loendur}")
print(f"Paaritute arvude arv: {paaritu_loendur}")


#Ülesanne 9
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


#Ülesanne 10
for arv in range(1, 101):
    if arv % 5 == 0:
        print(arv)