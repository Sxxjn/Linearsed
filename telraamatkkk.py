from tkinter import *

def avage_uue_kontakti_aken():
    uus_aken = Toplevel(aken)
    uus_aken.title("Lisa uus kontakt")
    uus_aken.geometry("400x300")

    nimi_label = Label(uus_aken, text="Nimi:", font=("Arial", 12))
    nimi_label.pack(pady=5)

    nimi_entry = Entry(uus_aken, font=("Arial", 12))
    nimi_entry.pack(pady=5)

    email_label = Label(uus_aken, text="E-mail:", font=("Arial", 12))
    email_label.pack(pady=5)

    email_entry = Entry(uus_aken, font=("Arial", 12))
    email_entry.pack(pady=5)

    telefon_label = Label(uus_aken, text="Telefon:", font=("Arial", 12))
    telefon_label.pack(pady=5)

    telefon_entry = Entry(uus_aken, font=("Arial", 12))
    telefon_entry.pack(pady=5)

    lisa_button = Button(uus_aken, text="Lisa kontakt", bg="green", fg="white", font=("Arial", 12))
    lisa_button.pack(pady=10)

def avage_otsi_kontakti_aken():
    otsing_aken = Toplevel(aken)
    otsing_aken.title("Otsi kontakt")
    otsing_aken.geometry("400x200")

    otsi_label = Label(otsing_aken, text="Sisesta nimi:", font=("Arial", 12))
    otsi_label.pack(pady=5)

    otsi_entry = Entry(otsing_aken, font=("Arial", 12))
    otsi_entry.pack(pady=5)

    otsi_button = Button(otsing_aken, text="Otsi", bg="blue", fg="white", font=("Arial", 12))
    otsi_button.pack(pady=10)

def avage_kustuta_kontakti_aken():
    kustuta_aken = Toplevel(aken)
    kustuta_aken.title("Kustuta kontakt")
    kustuta_aken.geometry("400x200")

    nimi_label = Label(kustuta_aken, text="Sisesta nimi:", font=("Arial", 12))
    nimi_label.pack(pady=5)

    nimi_entry = Entry(kustuta_aken, font=("Arial", 12))
    nimi_entry.pack(pady=5)

    kustuta_button = Button(kustuta_aken, text="Kustuta", bg="red", fg="white", font=("Arial", 12))
    kustuta_button.pack(pady=10)

def avage_paranda_kontakti_aken():
    paranda_aken = Toplevel(aken)
    paranda_aken.title("Paranda kontakt")
    paranda_aken.geometry("400x200")

    nimi_label = Label(paranda_aken, text="Sisesta nimi:", font=("Arial", 12))
    nimi_label.pack(pady=5)

    nimi_entry = Entry(paranda_aken, font=("Arial", 12))
    nimi_entry.pack(pady=5)

    paranda_button = Button(paranda_aken, text="Paranda", bg="orange", fg="white", font=("Arial", 12))
    paranda_button.pack(pady=10)

def avage_sorteeri_kontakti_aken():
    sorteeri_aken = Toplevel(aken)
    sorteeri_aken.title("Sorteeri kontakt")
    sorteeri_aken.geometry("400x200")

    sorteeri_label = Label(sorteeri_aken, text="Sisesta sorteerimise valik (nimi/email/telefon):", font=("Arial", 12))
    sorteeri_label.pack(pady=5)

    sorteeri_entry = Entry(sorteeri_aken, font=("Arial", 12))
    sorteeri_entry.pack(pady=5)

    sorteeri_button = Button(sorteeri_aken, text="Sorteeri", bg="purple", fg="white", font=("Arial", 12))
    sorteeri_button.pack(pady=10)

def avage_saada_kiri_aken():
    saada_aken = Toplevel(aken)
    saada_aken.title("Saada kiri")
    saada_aken.geometry("400x200")

    kellele_label = Label(saada_aken, text="Kellele:", font=("Arial", 12))
    kellele_label.pack(pady=5)

    kellele_entry = Entry(saada_aken, font=("Arial", 12))
    kellele_entry.pack(pady=5)

    saada_button = Button(saada_aken, text="Saada kiri", bg="yellow", fg="white", font=("Arial", 12))
    saada_button.pack(pady=10)

aken = Tk()
aken.title("Telefoniraamat")
aken.geometry("600x600")
aken.configure(bg="lightblue")
aken.resizable(width=False, height=False)

frame = Frame(aken, bg="lightblue")
frame.pack(expand=True)

lisa_button = Button(frame, text="Lisa uus kontakt", command=avage_uue_kontakti_aken, bg="green", fg="white", font=("Arial", 12))
lisa_button.pack(pady=10)

otsi_button = Button(frame, text="Otsi kontakt", command=avage_otsi_kontakti_aken, bg="blue", fg="white", font=("Arial", 12))
otsi_button.pack(pady=10)

kustuta_button = Button(frame, text="Kustuta kontakt", command=avage_kustuta_kontakti_aken, bg="red", fg="white", font=("Arial", 12))
kustuta_button.pack(pady=10)

paranda_button = Button(frame, text="Paranda kontakt", command=avage_paranda_kontakti_aken, bg="orange", fg="white", font=("Arial", 12))
paranda_button.pack(pady=10)

sorteeri_button = Button(frame, text="Sorteeri kontakt", command=avage_sorteeri_kontakti_aken, bg="purple", fg="white", font=("Arial", 12))
sorteeri_button.pack(pady=10)

saada_button = Button(frame, text="Saada kiri", command=avage_saada_kiri_aken, bg="yellow", fg="white", font=("Arial", 12))
saada_button.pack(pady=10)

aken.mainloop()
