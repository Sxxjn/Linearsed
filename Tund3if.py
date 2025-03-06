# #Ainult positiivsed arvud korrutame
# a=float(input("A: "))
# b=float(input("B: "))
# if a>0 and b>0:
#     print(f"Korutis võrdub: {a*b}")

# #Kas a on paaris või paaritu arv?
# if a%2 and a!=0:
#     print(f"Arv {a} on paaris")
# elif:
#     print(f"Arv {a} on märamatu")
# else:
#     print(f"Arv {a} on paaritu")

#Ema-robot 5-, 4-, 3-, 2-, 1-
try:
    hinne=int(input("Mis hinne sai täna koolis?"))
    if hinne in range(1,6):
        print("Hinne")
        if hinne==5:
            print("VH")
        elif hinne==4
            print("R")
        else:
            print("MR")
    else:
        print("Ei ole hinne")
except Exception as e:
    print("Viga:", e)





