from operator import truediv


#1
def arithmetic(arv1: float, arv2:float, tehe: str):
    """
    Funktsioon töötab nagu lihtme kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    kui sisend ei ole järjendis [+,-,/,*], siis tagastab sõne "Tundmatu tehe"
    :param float arv1: Sisend ujukomaarv tüübina
    :param float arv2: Sisend ujukomaarv tüübina
    :rtype: varMääramata tüüp (float või srt)
    """
    if tehe in["+", "-", "/", "*"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tunndmatu tehe"
    return vastus


# 2
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui aasta on liigaasta ja False kui aasta on tavaline aasta
    :param int aasta:Sisend kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

#3
def square(külg:float)->any:
    """"Ruudu pindala, ümbermõõdu ja diagonaali leidmine
    :param float külg: Sisend kasutajalt
    :rtype: float S,P,d
    """

    S=külg**2
    P=4*külg
    d=round((2)**(1/2)*külg)
    return S,P,d

#4
def season(param:int)->str:
    """Funktsioon tagastab (talv, kevad, suvi või sügis)
    On vaja kirjutada kuu number 1-12
    :param kuu number: Sisend in range (1,13)
    :rtype: int season
    """
    if param in [1,2,12]:
     H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="Sügis"
    return H

#5
def bank(summa:float, aastad:int,)->float:
    """Funktsioon arvutab summa, mis on saadud intressi arvelt
    :param float summa: Sisend kasutajalt
    :param int aastad: Sisend kasutajalt
    :rtype: float summa
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa

# Ülesanne 6
from random import *
def is_prime(a=randint(1,10000))->bool:
    """ 
    funktsioon is_prime, mis võtab 1 argumendi – arvu vahemikus 0 kuni 1000, ja tagastab tõene, kui see on algarvuline, ja False, kui see on algväärtus.
    :param
    :param
    :rtype:
    """
    print(a)
    v=True 
    for jagaja in range(2,a):
        if a%jagaja==0:
            v=False
    return v

#Ülesanne 7 
def date(päev:int,kuu:int,aasta:int)->bool:
    """
    Kuupäeva funktsioon, millel on 3 argumenti: päev, kuu ja aasta. Tagasta True, kui selline kuupäev on meie kalendris olemas, ja False muul juhul.
    :param
    :param
    :param
    """
    if päev in range(1,32) and kuu in[1,3,5,7,8,10,12] and aasta>0:
        y=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,31) and kuu in[4,6,9,11] and aasta>0:
        v=True
    else:
        v=False
    return v