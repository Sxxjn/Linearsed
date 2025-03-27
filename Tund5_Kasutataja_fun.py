from operator import truediv


# #1
# def arithmetic(arv1: float, arv2:float, tehe: str):
#     """
#     Funktsioon töötab nagu lihtme kalkulaator
#     + - liitmine
#     - - lahutamine
#     * - korrutamine
#     / - jagamine
#     kui sisend ei ole järjendis [+,-,/,*], siis tagastab sõne "Tundmatu tehe"
#     :param float arv1: Sisend ujukomaarv tüübina
#     :param float arv2: Sisend ujukomaarv tüübina
#     :rtype: varMääramata tüüp (float või srt)
#     """
#     if tehe in["+", "-", "/", "*"]:
#         if arv2==0 and tehe=="/":
#             vastus="DIV/0"
#         else:
#             vastus=eval(str(arv1)+tehe+str(arv2))
#     else:
#         vastus="Tunndmatu tehe"
#     return vastus


# #2
# def is_year_leap(aasta:int)->bool:
#     """Liigaasta leidmine
#     Tagastab True, kui aasta on liigaasta ja False kui aasta on tavaline aasta
#     :param int aasta:Sisend kasutajalt
#     :rtype: bool tõeväärsuses formaadis tulemus
#     """
#     if aasta%4==0:
#         v=True
#     else:
#         v=False
#     return v

# #3
# def square(külg:float)->any:
#     """"Ruudu pindala, ümbermõõdu ja diagonaali leidmine
#     :param float külg: Sisend kasutajalt
#     :rtype: float S,P,d
#     """

#     S=külg**2
#     P=4*külg
#     d=round((2)**(1/2)*külg)
#     return S,P,d

# #4
# def season(param:int)->str:
#     """Funktsioon tagastab (talv, kevad, suvi või sügis)
#     On vaja kirjutada kuu number 1-12
#     :param kuu number: Sisend in range (1,13)
#     :rtype: int season
#     """
#     if param in [1,2,12]:
#      H="Talv"
#     elif param in [3,4,5]:
#         H="Kevad"
#     elif param in [6,7,8]:
#         H="Suvi"
#     else:
#         H="Sügis"
#     return H

#5
def bank(summa:float, aastad:int, intress:float)->float:
    """Funktsioon arvutab summa, mis on saadud intressi arvelt
    :param float summa: Sisend kasutajalt
    :param int aastad: Sisend kasutajalt
    :param float intress: Sisend kasutajalt
    :rtype: float summa
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa