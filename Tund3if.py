#Näidised
# #Ainult positiivsed arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0:
#     print(f"Korutis võrdub: {a*b}")

# #Kas a on paaris või paaritu arv?
# a=float(input("A: "))
# if a%2 and a!=0:
#     print(f"Arv {a} on paaris")
# elif:
#     print(f"Arv {a} on märamatu")
# else:
#     print(f"Arv {a} on paaritu")

#Ema-robot 5-, 4-, 3-, 2-, 1-
# try:
#     hinne=int(input("Mis hinne sai täna koolis?"))
#     if hinne in range(1,6):
#         print("Hinne")
#         if hinne==5:
#             print("VH")
#         elif hinne==4:
#             print("H")
#         elif hinne==3:
#             print("R")
#         else:
#             print("MR")
#     else:
#         print("Ei ole hinne")
# except Exception as e:
#     print("Viga:", e)


# nimi="PYTON"
# print(nimi.isupper())


#Ülesanne 1
nimi=input("Mis su nimi on?")
if nimi=="JUKU":
    print("Lähme kinno")
    vanus=int(input("Kui vana sa oled?"))
    if 0<vanus<6:
        print("Tasuta")
    elif 6<=vanus<=14:
        print("Lastepilet")
    elif 14<=vanus<=65: 
        print("Täispilet")
    elif 65<=vanus<=100:
        print("Sooduspilet")
    elif vanus<=0 or vanus>=100:
        print("Viga andmega")
else:
    print("Ma olen hõivatud! Mino kinno ise!")


#Ülesanne 2
nimed=["Ruslan","Bohdan","Robert"]
nimi1=input("Sisesta esimene nimi ")
nimi2=input("Sisesta teine nimi ")
nimi3=input("Sisesta kolmasj nimi ")
if nimi1 in nimed and nimi2 in nimed and nimi3  in nimed and nimi1!=nimi2 and nimi2!=nimi3 and nimi2!=nimi3:
    print("Pinginnabrid")
else:
    print("Ei ole pinginaabrid")

#Ülesanne 3
try:
    a = float(input("Sisesta pikkus: "))
    b = float(input("Sisesta laius: "))
    #--------
    S = a * b
    soov = input("Kas sa tahad remondi teha?: ")
    if soov.lower() == "jah":
        print("Remont")
        hind = float(input("Hind: "))
        #--------
        koguhind = S * hind
        print(f"Sul on vaja {koguhind} eur")
    elif soov.lower() == "ei":
        print("Head aega!")
    else:
        print("Palun sisesta jah või ei!")
except:
    print("Pikkus, laius ja hind peavad olema numbrid!")

#Ülesanne 4
alghind=float(input("Sisesta toode alghind: "))
if alghind>700:
    soodus=alghind=0.70
    print(f"Soodus hind on {soodus} eurot.")
else: print("Soodustus ei kehti")

#Ülesanne 5
try:
    temp=float(input("Mis temperatuur praegu on?"))
    if temp<18:
        print("Tuba on külm, tõsta temperatuuri")
    else:
        print("Toatemperatuur on sobiv")
except:
    print("Viga!!")

#Ülesanne 6
try:
    pikkus=float(input("Sisesta oma pikkus: "))
    if pikkus<160:
        print("Sa oled lühike(((")
    elif 160<=pikkus<180:
        print("Sa oled keskmine")
    elif 180<=pikkus:
        print("Sa oled pikk!!!")
except:
    print("Viga!")

#Ülesanne 7
try:
    sugu=input("Sa oled mees või naine? ")
    pikkus=float(input("Sisesta pikkus: "))
    if sugu=="mees":
        if pikkus<160:
             print("Sa oled lühike(((")
        elif 160<=pikkus<180:
             print("Sa oled keskmine")
        elif 180<=pikkus:
             print("Sa oled pikk!!!")
    if sugu=="naine":
        if pikkus<150:
             print("Sa oled lühike(((")
        elif 150<=pikkus<170:
             print("Sa oled keskmine")
        elif 170<=pikkus:
             print("Sa oled pikk!!!")
except:
    print("Viga!")

# Ülesanne 12
try:
    hind=float(input("Kui palju toode maksab?"))
    if hind>10:
        soodus1=round(hind*0.80, 2)
        print(f"Hind soodushinnaga on {soodus1} eurot")
    else:
        soodus2=round(hind*0.90, 2)
        print(f"Hind soodushinnaga on {soodus2} eurot")
except:
    print("Viga!")



