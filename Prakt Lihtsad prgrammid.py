from math import *
# from datetime import *
# from calendar import *
# from time import strtime
# tana=date.today()
# print(f"Tere! Täna on {tana}")
# # 27/12/2022
# tana1 = tana.strftime("%d/%m/%Y")
# print(tana1)
# # December 27, 2022
# tana2 = tana.strftime("%B %d, %Y")
# print(tana2)
# # 12/27/22
# tana3 = tana.strftime("%m/%d/%y")
# print(tana3)
# # Dec-27-2022
# tana4 = tana.strftime("%b-%d-%Y")
# print(tana4)
# päev=tana.day
# kuu=tana.month
# aasta=tana.year
# print(f"Päev om {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
# paevad=monthrange(2025,2[1])
# onjaanud=paevad-päev
# print(f"Kuu lõpuni on jäänud {onjaanud} päevad")

# päevad_aastal=(date(aasta,12 ,31) - tana).days
# print(f"Kuni aasdta lõpuni on jäänud {päevad_aastal} päevad")

# try: 
#     sünniüäev=input("Sünnipäev:")#YYYY-MM-DD
#     sü=datetime.strptime(sünnipäev, "%Y-%m-%d")
#     print(sp)
#     vanus_aastades=tana.year-sp.year
#     vanus kuudes=vanus_aastades*12
#     print(f"Vastus: Vanus {vanus_aastades} aastad")
# except:
#     print("Sa pead YYYY-MM-DD format kasutada sisestamisel.")

#     #Ülesanne 2
#     #sulgude kasutamine
#     print("a=3 + 8 / (4-2) * 4")
#     a=3 + 8 / (4-2) * 4
#     print(a)
#     print("a=(3 + 8)/ (4 - 2) * 4")
#     a=(3 + 8) / (4 - 2) * 4
#     print (a)

#Ülesanne 3
try:
    R=float(input("Sisesta R, kus R on ringi raadius"))
     # == võrdub, != ei võrdu, < rohkem, > vähem, <=, >=
    if R<=0: 
         print("Nulliga ja negatiivseta arvudega ei ole mõtte töötada!!!")
    else: 
          Ringi_S=round(pi*R**2)   
          Ringi_P=round(2*pi*R)
          Ruudsu_S=2*R*2*R
          Ruudu_P=4*2*R
          print(f"Ringi_S= {Ringi_S}\nRingi_P= {Ringi_P}\nRuudsu_S= {Ruudsu_S}\nRuudu_P= {Ruudu_P}")
except:
    print("Sisesta ainult arvud!!!")
