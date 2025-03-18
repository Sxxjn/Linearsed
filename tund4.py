#Töö 4.4
#1
from string import *
vokaali=["a", "e", "u", "o", "i", "ü", "õ", "ä", "ö"]
konsonanti= "qwrtpsdfghjklzxcvbnm"
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("Sisend sõna või lause: ").lower()
tekst_list=list(tekst)

for s in tekst_list:
    if s in vokaali:
        v+=1
    elif s in konsonanti:
        k+=1
    elif s in numbrid:
        n+=1
    elif s in märkid:
        m+=1
    elif s==" ":
        t+=1
    print(f"Vokaali: {v} \nKonsonanti: {k} \nNumbrid: {n} \nMärkid: {m} \nTühik: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")
    if s in vokaali:
            v+=1
    elif s in konsonanti:
        k+=1
    print(f"Vokaali: {v} \nKonsonanti: {k}")

    #2






# sõne="Programmeerimine"
# print(sõne)
# list_sõne=list(sõne)
# print(list_sõne)
# print(f"Viies täht: {list_sõne[4]}")
# print(f"Sõnes on {len(sõne)} t")
# elemendid=[]
# for i in range(5):
#     elemendid.append(input(f"{i+1}. element: "))
# print(elemendid)
# for e in elemendid:
#     print(e)

# #extend
# list_sõne.extend(elemendid)
# print(list_sõne)
# print(elemendid)

# #insert
# elemendid.insert(0,"A")
# print(elemendid)

# #remove
# elemendid.remove("A")

# #pop
# elemendid.pop(0)
# elemendid.pop()
# print(elemendid)

# #index
# ind=list_sõne.index("r")
# print(f"Täht r on {ind}-indeksiga")

# #count
# k=list_sõne.index("r")
# print(f"Täht r on {k} korda sõnas {sõne}")

# #reverse
# list_sõne.reverse()
# print(list_sõne)

# #copy
# list_sõne2=list_sõne.copy()

# #clear
# list_sõne2.clear()
# print(list_sõne2)






