print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
küsimus = input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if küsimus =="1":
    try:
        pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
        mass = float(input("Sisesta oma kehakaal kilogrammides: "))
        print(pikkus, mass)
        kmi = mass / ((pikkus*0.01)**2)
        print(f"{nimi}! Sinu keha indeks on: {round(kmi, 1)}")
        if kmi < 16:
            vastus = "Tervisele ohtlik alakaal"
        elif 16 <= kmi < 19:
            vastus = "Alakaal"
        elif 20 <= kmi <= 25:
            vastus = "Normaalkaal"
        elif 26 <= kmi <= 30:
            vastus = "Ülekaal"
        elif 31 <= kmi <= 35:
            vastus = "Rasvumine"
        elif 36 <= kmi <= 40:
            vastus = "Tugev rasvumine"
        elif kmi > 40:
            vastus = "Tervisele ohtlik rasvumine"
        print(f"KMI vastus: {vastus}")
    except:
        print("Palun sisesta kehtivad numbrid! Pikkus peab olema täisarv ja kaal reaalarv.")
elif küsimus =="0":
    print("Kahju! See on väga kasulik info!")
else:
    print("Vale sisend! Palun sisesta 0 või 1.")
print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")
