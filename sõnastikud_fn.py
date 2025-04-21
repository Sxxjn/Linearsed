# Algne sõnastik
sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

# Tõlge eesti keelest vene keelde
def tolgi_est_rus(sona):
    return sonastik.get(sona, "Sõna ei leitud!")

# Tõlge vene keelest eesti keelde
def tolgi_rus_est(sona):
    for key, value in sonastik.items():
        if value == sona:
            return key
    return "Sõna ei leitud!"

# Uue sõna lisamine sõnastikku
def lisa_sona():
    eesti_sona = input("Sisesta uus sõna eesti keeles: ")
    vene_sona = input(f"Sisesta selle sõna vene tõlge: ")
    sonastik[eesti_sona] = vene_sona
    print("Sõna lisatud!")

# Sõna parandamine sõnastikus
def paranda_sona():
    vana_sona = input("Sisesta sõna, mida soovid parandada (eesti või vene): ")
    if vana_sona in sonastik:
        uus_sona = input(f"Anna {vana_sona} jaoks uus vene tõlge: ")
        sonastik[vana_sona] = uus_sona
        print(f"Sõna {vana_sona} on nüüd parandatud!")
    else:
        for key, value in sonastik.items():
            if value == vana_sona:
                uus_sona = input(f"Anna {vana_sona} jaoks uus eesti tõlge: ")
                sonastik[key] = uus_sona
                print(f"Sõna {vana_sona} on nüüd parandatud!")
                break
        else:
            print("Sõna ei leitud!")

# Teadmiste testimine
def testi_teadmisi():
    eesti_keelega_sona = random.choice(list(sonastik.keys()))
    vene_keelega_sona = sonastik[eesti_keelega_sona]
    vastus = input(f"Sisesta vene tõlge sõnale '{eesti_keelega_sona}': ")
    if vastus.lower() == vene_keelega_sona.lower():
        print("Õige!")
        return True
    else:
        print(f"Vale! Õige vastus on '{vene_keelega_sona}'.")
        return False

# Funktsioon teadmistestide tegemiseks
def tee_knowlege_test():
    test_count = 5  # Küsida 5 sõna
    correct_answers = 0
    for _ in range(test_count):
        if testi_teadmisi():
            correct_answers += 1
    print(f"Test lõppenud! Sinu tulemus: {correct_answers * 100 / test_count}%")
