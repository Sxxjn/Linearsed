from tkinter import *
from tkinter import messagebox

k = 0

def vajutatud(event):
    global k
    k += 1
    nupp.config(text=f"Kliki mind {k} korda")

def tuhista(event):
    sisestus.delete(0, END)

def text_to_label(event):
    if sisestus.get() != "":
        pealkiri.config(text=sisestus.get())


aken = Tk()
aken.title("Teema 8")
aken.geometry("600x400")
aken.configure(bg="lightblue")
aken.resizable(width=False, height=False)

aken.attributes("-alpha", 0.9)


pealkiri = Label(aken, text="Tere tulemast!\n Teema nr 8. Tkinter", bg="blue", fg="green", font=("Arial", 20))
nupp = Button(aken, text="Kliki mind", bg="red", fg="white", font=("Arial", 15),
              command=lambda: messagebox.showinfo("Teema 8", "Tere tulemast Tkinteri maailma!"))
nupp.bind("<Button-3>", vajutatud)

sisestus = Entry(aken, bg="white", font=("Arial", 15), fg="black")
sisestus.insert(0, "Kirjuta siia tekst")
sisestus.bind("<FocusIn>", tuhista)
sisestus.bind("<Return>", text_to_label)

pealkiri.pack(pady=256)
nupp.pack(pady=20)
sisestus.pack(pady=20)
aken.mainloop()
