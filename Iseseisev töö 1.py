from math import *
print("Ruudu karakteristikud")
a=int(input('Sisesta ruudu külje pikkus => '))
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=int(input("Sisesta ristküliku 1. külje pikkus => "))
c=int(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", S)
P=2*(b+c)
print("Ristküliku ümbermõõt", P)
di=sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di))
print()
print("Ringi karakteristikud")
r=int(input('Sisesta ringi raadiusi pikkus => '))
d=2*r
print("Ringi läbimõõt", d)
S=pi*r*2
print("Ringi pindala", round(S))
C=2*pi*r
print("Ringjoone pikkus", round(C))
#FIEHIOhgfoiuerbgoiub