#Näidised
# a=0
# while a==0:
#     print(a)
#     a=int(input("a: "))
# while True:
#     print(a)
#     a=int(input("a: "))
#     if a==100: break
# for i in range(0,10,1):
#     print(f"{i}. samm")
# print()
# for i in range(1,11,1):
#     print(f"{i}. samm")


#Ülesanne 1
#1. variant
# try:
#     nimi=input("Sisesta oma nimi: ") 
# except:
#     print("Viga!!")
# try:
#     korda=int(input("Mitu korda? ")) #korda.isnumeric()  print(f"Ole tervitatud, {nimi}, {i+1} korda.")
#     for i in range(korda):
#         print(f"Ole tervitatud, {nimi}, {i+1} korda.")
# except:
#     print("Viga!!")
#2. variant
# while True:
#     try:
#         nimi=input("Sisesta oma nimi: ")
#         if nimi.isalpha()==True: break 
#     except:
#         print("Viga!!")
# while True:
#     try:
#         korda=int(input("Mitu korda? ")) #korda.isnumeric()
#         if korda>0: break
#     except:
#         print("Viga!")
# print("while true")
# i=0
# while True:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i} korda.")
#     if i==korda: break
# print("while tingimusega")
# i=0
# while i<korda:
#     i+=1
#     print(f"Ole tervitatud, {nimi}, {i} korda.")

#Ülesanne 2
# summa=0
# j=0
# while True:
#     while True:
#         try:
#             a=float(input("a: "))
#             break
#         except:
#             print("Viga!")
#     summa+=a
#     j+=1
#     if j==10: break
# print(f"Arvude summa: {summa}")
# #-------
# summa = 0
# while True:
#     number = input("Sisesta arv (vajuta Enter lõpetamiseks)")
#     if number == "": break
#     try:
#         number=float(number)
#         summa += number
#     except:
#         print("Viga!")
#     print(f"Arvude summa: {summa}")

#Ülesanne 4
# for i in range(1,11,1):
#     print(i)
# print("Korrutustabel 1-10:")
# for i in range(1,11,1):
#     for j in range(1,11,1):
#         print(f"{i} x {j} = {i*j}")

#Ülesanne 5
N=int(input("N: "))
for j in range(N):
    for i in range(N):
        if i==j or i==N-j:
            print("X",end=" ")
        else:
            print("O",end=" ")
    print()
print()
