# from random import randint *
from math import *
from random import randint
#Ülesanne 1
# nimi=input("mis on sinu nimi?: ")
# vanus=int(input("Kui vana sa oled?: "))

# print(f"Tere, maailm! Tervitran sind {nimi} Sa oled {vanus} aastat vana.")
# print("Tere, maailm! Tervitran sind", nimi, "Sa oled", vanus,"aastat vana")
# print("Tere, maailm! Tervitran sind"+nimi+"Sa oled"+str(vanus)+"aastat vana")

# Ülesanne 2



# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print(f"Muutuja {vanus} on {type(vanus)} tüübi")
# print(f"Muutuja {eesnimi} {type(eesnimi)} tüübi")
# print(f"Muutuja {pikkus} on {type(pikkus)} tüübi")
# print(f"Muutuja {kas_käib_koolis} on {type(kas_käib_koolis)} tüübi")

# #Ülesanne 3



# kommidearv=randint(1,100)
# print(f"Laual on {kommidearv} kommid")
# kommidvõtnud=int(input("Mitu kommi tahad ära võtta?"))
# onjäänud=kommidearv-kommidvõtnud
# print(f"Laual on jäänud {onjäänud} komme")

#Ülesanne 4
# ümbermõõt=int(input("Kui suur on ümbermõõt?: "))
# läbimõõt=ümbermõõt//pi
# print(f"läbimõõt on +f{läbimõõt}")

#Ülesanne 5

N = float(input("Sisesta ristküliku pikkus (N): "))
M = float(input("Sisesta ristküliku laius (M): "))
diagonaal = sqrt(N**2 + M**2)
print(f"Diagonaal on: {diagonaal}")


# #Ülesanne 6
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = teppikus / aeg

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

#Ülesanne 7
# a1=randint(0,100)
# a2=randint(0,100)
# a3=randint(0,100)
# a4=randint(0,100)
# a5=randint(0,100)
# keskmine=(a1+a2+a3+a4+a5)/5
# print(f"Arvud olid: {a1}, {a2}, {a3}, {a4},{a5}. Nende keskmine on {keskmine}. ")

#Ülesanne 8
# tekst=""" 
#     @..@
#    (----)
#   ( \__/ )
#   ^^ "" ^^  """
#   print(tekst)

# print("    @..@")
# print("   (----)")
# print("  ( \__/ )")
# print("""  ^^ "" ^^""") 

#Ülesanne 9
# a=randint(1,100)
# b=randint(1,100)
# c=randint(1,100)
# P=(a+b+c)
# print(f"Arvud olid: {a}, {b}, {c}. Periimetr on {P}")

#Ülesanne 10

# P=randint(2, 6)
# hind=12.90*1.1
# koos=(hind/P)
# print(f"Pitsa maksab 12.90 eurot, sõbrad jätsid 10% jootraha. Seal oli {P} sõpra, igaüks maksis {koos} eurot.")