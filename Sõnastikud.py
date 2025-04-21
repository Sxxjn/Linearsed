from random import *
from sõnastikud_fn import *


# Peamine menüü ja tsükkel
def main():
    while True:
        print("\nTere tulemast eesti-vene sõnastikku!")
        print("Valikud: \n1 - Tõlgi eesti -> vene\n2 - Tõlgi vene -> eesti\n3 - Lisa uus sõna\n4 - Paranda sõna\n5 - Testi teadmisi\n6 - Välju")
        
        valik = input("Tee oma valik: ")
        
        if valik == '1':
            sona = input("Sisesta sõna eesti keeles: ")
            print(f"Tõlge vene keelde: {tolgi_est_rus(sona)}")
        elif valik == '2':
            sona = input("Sisesta sõna vene keeles: ")
            print(f"Tõlge eesti keelde: {tolgi_rus_est(sona)}")
        elif valik == '3':
            lisa_sona()
        elif valik == '4':
            paranda_sona()
        elif valik == '5':
            tee_knowlege_test()
        elif valik == '6':
            print("Head aega!")
            break
        else:
            print("Vale valik! Palun vali uuesti.")


if __name__ == "__main__":
    main()