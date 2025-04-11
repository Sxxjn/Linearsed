import random

# Funktsioon nimekirjade loomiseks ja menüü kuvamiseks
def patsiendid():
    nimed = []
    D_vitamiini_sisaldus = []

    n = int(input("Sisesta patsientide arv: "))
    
    for i in range(n):
        nimi = f"Patsient_{i+1}"  # Soovi korral võib küsida kasutajalt nime
        D_vitamiin = random.randint(10, 100)  # D-vitamiini tase vahemikus 10–100

        nimed.append(nimi)
        D_vitamiini_sisaldus.append(D_vitamiin)

    # Kuvame patsiendid ja nende D-vitamiini tasemed
    print(f"\nKokku on {n} patsienti, nende D-vitamiini tasemed on järgmised:")
    for nimi, tase in zip(nimed, D_vitamiini_sisaldus):
        print(f"{nimi}: {tase}")
    
    # Menüü valikud
    while True:
        print("\nMenüü:")
        print("2. Arvuta D-vitamiini keskmine tase")
        print("3. Kuvada K patsienti kõrgeima D-vitamiini tasemega")
        print("4. Otsi patsienti nime järgi")
        print("5. Kuvada kõik patsiendid")
        print("0. Välju programmist")

        valik = input("Vali tegevus: ")


        if valik == "2":
            arvuta_keskmine(D_vitamiini_sisaldus)
        elif valik == "3":
            k = int(input("Mitu patsienti kuvada? "))
            kuva_top_k(nimed, D_vitamiini_sisaldus, k)
        elif valik == "4":
            otsing = input("Sisesta patsiendi nimi: ")
            otsi_nime_jargi(nimed, D_vitamiini_sisaldus, otsing)
        elif valik == "5":
            kuva_koik(nimed, D_vitamiini_sisaldus)
        elif valik == "0":
            print("Programmist väljutakse.")
            break
        else:
            print("Vigane valik. Proovi uuesti.")

# Kuvab patsiendid, kelle D-vitamiin < 30
def kuva_puudusega(nimed, D_vit):
    print("\nPatsiendid, kellel on D-vitamiini puudus (<30):")
    for nimi, tase in zip(nimed, D_vit):
        if tase < 30:
            print(f"{nimi}: {tase}")

# Arvutab keskmise taseme
def arvuta_keskmine(D_vit):
    if D_vit:
        keskmine = sum(D_vit) / len(D_vit)
        print(f"\nD-vitamiini keskmine tase: {keskmine:.2f}")
    else:
        print("Nimekiri on tühi.")

# Kuvab top K patsienti kõrgeima tasemega
def kuva_top_k(nimed, D_vit, k):
    koos = list(zip(nimed, D_vit))
    sorted_list = sorted(koos, key=lambda x: x[1], reverse=True)
    print(f"\nTop {k} patsiendid D-vitamiini taseme järgi:")
    for nimi, tase in sorted_list[:k]:
        print(f"{nimi}: {tase}")

# Otsib patsiendi nime järgi
def otsi_nime_jargi(nimed, D_vit, nimi_otsing):
    leitud = False
    for nimi, tase in zip(nimed, D_vit):
        if nimi.lower() == nimi_otsing.lower():
            print(f"\nLeitud: {nimi}, D-vitamiini tase: {tase}")
            leitud = True
            break
    if not leitud:
        print("Patsienti ei leitud.")

# Kuvab kõik patsiendid
def kuva_koik(nimed, D_vit):
    print("\nKõik patsiendid ja nende D-vitamiini tase:")
    for nimi, tase in zip(nimed, D_vit):
        print(f"{nimi}: {tase}")

# Käivitab programmi
patsiendid()
