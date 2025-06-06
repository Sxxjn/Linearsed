sonastik = {'koer': 'собака','kass': 'кошка','maja': 'дом','auto': 'машина','päike': 'солнце'}
def tolgi_est_rus(sona):
    if sona in sonastik:
        return sonastik[sona]
    else:
        return "Sõna ei leitud sõnastikust."

def tolgi_est_rus(sona):
    return sonastik.get(sona, "Sõna ei leitud sõnastikust!")

def tolgi_rus_est(sona):
    for est, rus in sonastik.items():
        if rus == sona:
            return est
    return "Sõna ei leitud sõnastikust!"

def lisa_sona():
    est = input("Sisesta uus sõna eesti keeles: ").strip()
    rus = input("Sisesta selle sõna vene tõlge: ").strip()
    sonastik[est] = rus
    print("Sõna lisatud!")

def paranda_sona():
    est = input("Sisesta sõna eesti keeles, mida soovid parandada: ").strip()
    if est in sonastik:
        uus_rus = input(f"Praegune tõlge on '{sonastik[est]}'. Sisesta uus vene tõlge: ").strip()
        sonastik[est] = uus_rus
        print("Tõlge on parandatud!")
    else:
        print("Sõna ei leitud sõnastikust.")

def testi_teadmisi():
    print("Testi teadmisi alustatakse!")
    sonad = list(sonastik.items())

    if sonad:
        correct = 0
        for est, rus in sonad:
            vastus = input(f"Sisesta vene tõlge sõnale '{est}': ").strip().lower()
            if vastus == rus.lower():
                print("Õige!")
                correct += 1
            else:
                print(f"Vale! Õige vastus on: {rus}")
        print(f"Test lõppenud! Sinu tulemus: {correct / len(sonad) * 100:.2f}%")
    else:
        print("Sõnastik on tühi, testi ei saa teha.")