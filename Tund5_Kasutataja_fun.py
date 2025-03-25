from operator import truediv


def arithmetic(arv1: float, arv2:float, tehe: str):
    """
    Funktsioon töötab nagu lihtme kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    kui sisend ei ole järjendis [+,-,/,*], siis tagastab sõne "Tundmatu tehe"
    :perem float arv1: Sisend ujukomaarv tüübina
    :perem float arv2: Sisend ujukomaarv tüübina
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