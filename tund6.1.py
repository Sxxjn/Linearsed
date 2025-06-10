import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_est_rus(sona):
    if sona in sonastik:
        return sonastik[sona]
    else:
        return "Sõna ei leitud!"

def tolgi_rus_est(sona):
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sõna ei leitud!"

def lisa_sona():
    est = input("Sisesta eesti sõna: ")
    rus = input("Sisesta vene tõlge: ")
    sonastik[est] = rus
    print("Lisatud!")

def paranda_sona():
    est = input("Millist sõna soovid muuta? ")
    if est in sonastik:
        uus_rus = input("Sisesta uus vene tõlge: ")
        sonastik[est] = uus_rus
        print("Muudetud!")
    else:
        print("Sõna ei leitud!")

def testi_teadmisi():
    kogus = min(3, len(sonastik))
    valitud = random.sample(list(sonastik.keys()), kogus)
    for est in valitud:
        vastus = input(f"Kuidas on vene keeles '{est}'? ")
        if vastus == sonastik[est]:
            print("Õige!")
        else:
            print(f"Vale! Õige vastus on: {sonastik[est]}")

def main():
    while True:
        print("\nVali tegevus:")
        print("1 - Eesti -> Vene")
        print("2 - Vene -> Eesti")
        print("3 - Lisa sõna")
        print("4 - Paranda sõna")
        print("5 - Testi teadmisi")
        print("6 - Välju")
        valik = input("Valik: ")

        if valik == '1':
            est = input("Sisesta eesti sõna: ")
            print(tolgi_est_rus(est))
        elif valik == '2':
            rus = input("Sisesta vene sõna: ")
            print(tolgi_rus_est(rus))
        elif valik == '3':
            lisa_sona()
        elif valik == '4':
            paranda_sona()
        elif valik == '5':
            testi_teadmisi()
        elif valik == '6':
            print("Head aega!")
            break
        else:
            print("Vale valik!")

if __name__ == "__main__":
    main()
