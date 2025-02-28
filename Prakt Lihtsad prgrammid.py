from datetime import *
tana=date.today()
print(f"Tere! Täna on {tana}")
# 27/12/2022
tana1 = tana.strftime("%d/%m/%Y")
print(tana1)
# December 27, 2022
tana2 = tana.strftime("%B %d, %Y")
print(tana2)
# 12/27/22
tana3 = tana.strftime("%m/%d/%y")
print(tana3)
# Dec-27-2022
tana4 = tana.strftime("%b-%d-%Y")
print(tana4)
päev=tana.day
kuu=tana.month
aasta=tana.year
print(f"Päev om {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
paevad=monthrange(2025,2[1])
onjaanud=paevad-päev
print(f"Kuu lõpuni on jäänud {onjaanud} päevad")

päevad_aastal=(date(aasta,12 ,31) - tana).days
print(f"Kuni aasdta lõpuni on jäänud {päevad_aastal} päevad")

try: 
    sünniüäev=input("Sünnipäev:")#YYYY-MM-DD
    sü=datetime.strptime(sünnipäev, "%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus kuudes=vanus_aastades*12
    print(f"Vastus: Vanus {vanus_aastades} aastad")
except:
    print("Sa pead YYYY-MM-DD format kasutada sisestamisel.")

    #Ülesanne 2
    #sulgude kasutamine
    print("a=3 + 8 / (4-2) * 4")
    a=3 + 8 / (4-2) * 4
    print(a)
    print("a=(3 + 8)/ (4 - 2) * 4")
    a=(3 + 8) / (4 - 2) * 4
    print (a)
