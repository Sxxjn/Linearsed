#Töö 4.4
#1 
from string import *
vokaali=["a","o","i","e","u","ü","õ","ä","ö"]
konsonanti="qwrtypsdfghjklzxcvbnm"
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("Sisend (sõna või lause): ").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
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
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")

#2
#2.1
nimed=[]
for a in range (5): #Запрос пяти имён у пользователя.
    nimi=input("Sisesta nimi: ")
    nimed.append(nimi)
nimed.sort() #Сортировка в порядке убывания
print(nimed)
print(nimed[-1]) #Отдельно вывод последнего введённого имени
muuda=input("Kas soovite nimi muuta? jah/ei ").lower() #Спросить если хотите поменять имя.
if muuda == "jah": #Если да, то
    vana_nimi=input("Mis nimi te soovite muuta?: ") #Спросить какое имя заменить
    if vana_nimi in nimed:
        uus_nimi=input("Sisesta uus nimi: ") #Спросить новое имя
        ind=nimed.index(vana_nimi)
        nimed[ind]=uus_nimi
        nimed.sort() #Повторная сортировка по алфавиту
        print(f"Uuendatud nimed: {nimed}") #Показать обновлённый список имён.
    else:
        print("Sellist nime loendis ei ole") #Если имени нет в списке, то выводит сообщение, что такого имени там нет.
else:
    print("ok") #Если человек не хочет изменять имя, то написать ОК

#2.2
kord_opilased=["Juhan","Kati","Mario","Mario","Mati","Mati"] 
print(kord_opilased) #Показывается несколько имён, среди них есть повторяющиеся.
opilased=list(set(kord_opilased))  #Удаление дублирующихся имён
print(opilased) #Вывод имён без повторов

#2.3
vanus=5,13,25,9,20,17,11,10,8,24
print(vanus) #вывод возрастов
min_vanus=min(vanus) #Показывает самый минимальный из этого списка
print(f"\nKõige noorem on {min_vanus}")
max_vanus=max(vanus) #максимальный возраст из списка
print(f"Kõige vanem on {max_vanus}")
summa=sum(vanus) #Сумма всех возрастов
print(f"Vanuste summa on {summa}")
keskmine=summa/len(vanus) #средний возраст
print(f"Keskmine vanus on {keskmine}")

#3
sisend=[8,12,25,38,67,15,48] 
for number in sisend: #Используем значения чисел в списке и создаём гистограмму, используя звезды.
    print('*' *number)

#4
region={"1":"Tallinn","2":"Narva, Narva-Jõesuu","3":"Kohtla-Järve","4":"Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","5":"Tartu linn", "6":"Tartumaa, Põlvamaa, Võrumaa, Valgamaa","7":" Viljandimaa, Järvamaa, Harjumaa, Raplamaa","8": "Pärnumaa","9":"Läänemaa, Hiiumaa, Saaremaa"} #Список со значениями, если 1 то Таллинн, если 2 то Нарва, Нарва-Йыесуу, если 3 то Кохтла-Ярве и т.д.
post_indeks=input("Sisestage postiindeks: ") #Просит ввести индекс
if post_indeks.isdigit() and len(post_indeks) == 5: #проверяет что состоит только из цифр и длина только 5 цифр
    maakond=region.get(post_indeks[0]) #смотрит какой первый символ вводит пользователь и проверяет в словаре.
    print(f"Teie postiindeks kuulub piirkonda: {maakond}") #выводит к какому региону относится индекс
    if post_indeks[0] in ["1","2","3"]:
        print("Olge kodus") #если индекс начинается с 1,2 или 3, то говорит остаться дома
    else:
        print("Kandke maske!") #на все остальные говорит носить маску
else:
    print("Vigane sisend!") #если такого региона нет в словаре,то ошибка ввода

#5
sisend=input("Sisestage numbrid komadega eraldatult: ")
numbrid=(int(input(f"Sisestage {i+1}. number: ")) for i in range(int(input("Mitu numbrit soovite sisestada?: "))))
if(numbrid)>2:
    print("Listis peab olema vähemalt 2 elementi!")
    exit()
n=int(input("Mitu elementi soovite vahetada?: "))
if n>len(numbrid)//2:
    print("Vahetatavate elementide arv ei saa olla suurem kui pool listi pikkusest!")
    exit()
pikkus=len(numbrid)
for i in range(n):
    numbrid[i], numbrid[pikkus-1-i]=numbrid[pikkus-1-i], numbrid[i]

print("Muutunud list:", numbrid)

#ülesanne 11
import string
n=int(input("Sisestage tähtede arv: ")) #Запрашиваем количество букв
tähed=list(string.ascii_lowercase[:n]) #добавляются в список все строчные буквы английского алфавита, берётся столько символов сколько введёт пользователь
korduvad_tähed=[] #создаём список с повторяющимися буквами
for i in range(n):
    korduvad_tähed.append(tähed[i]*(i+1)) #в цикле повторяется, в зависимости от позиции и добавляется в список
print("Järjend:", tähed) #буквы которые мы используем
print("Teine järjend:", korduvad_tähed) #те же буквы, но повторяются взависимости от позиции

#12
import random

numbers=[random.randint(1, 100) for _ in range(10)]
print("Algne nimekiri", numbers)

min_value=min(numbers)
max_value=max(numbers)

min_index=numbers.index(min_value)
max_index=numbers.index(max_value)

numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print("Muudetud loend", numbers)



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






