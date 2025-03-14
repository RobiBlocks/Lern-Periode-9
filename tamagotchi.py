import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk

def GUI():
    window = tk.Tk()

    window.geometry("800x350")
    window.title("Pinguin Tamagotchi")
    window.bind("<KeyPress>", shortcut)

    buttonFrame = tk.Frame(window)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=3)
    buttonFrame.columnconfigure(2, weight=1)
    buttonFrame.rowconfigure(0, weight=1)
    buttonFrame.rowconfigure(1, weight=1)
    buttonFrame.rowconfigure(2, weight=1)
    buttonFrame.rowconfigure(3, weight=1)

    helloMessage = tk.Label(buttonFrame, text="Dein eigenes Tamagotchi!", font=('Arial', 16))
    helloMessage.grid(row=1, column=1, columnspan=2, sticky="we")

    image = tk.PhotoImage(file="pinguin.png")
    image = image.subsample(2, 2)
    imageTamagotchi = tk.Label(buttonFrame, image=image)
    imageTamagotchi.grid(row=1, rowspan=3, column=1, sticky="nswe")
    
    buttonStreicheln = tk.Button(buttonFrame, text="Streicheln", font=('Arial', 12), bg="#ffff00", height=5, command=pet)
    buttonStreicheln.grid(row=1, column=0, sticky="we")

    buttonFeed = tk.Button(buttonFrame, text="Füttern", font=('Arial', 12), bg="#ff3c00", height=5, command=feed)
    buttonFeed.grid(row=2, column=0, sticky="we")

    buttonSleep = tk.Button(buttonFrame, text="Schlafen", font=('Arial', 12), bg="#008cff", height=5, command=sleep)
    buttonSleep.grid(row=3, column=0, sticky="we")


    global LoveProgressbar
    LoveProgressbar = ttk.Progressbar(buttonFrame, length=200, mode="determinate", value=10)
    LoveProgressbar.grid(row=1, column=3, sticky="we")

    global HungerProgressbar
    HungerProgressbar = ttk.Progressbar(buttonFrame, length=200, mode="determinate", value=40)
    HungerProgressbar.grid(row=2, column=3, sticky="we")

    global TirednessProgressbar
    TirednessProgressbar = ttk.Progressbar(buttonFrame, length=200, mode="determinate", value=60)
    TirednessProgressbar.grid(row=3, column=3, sticky="we")

    buttonFrame.pack(fill="x", padx=20, pady=20)

    window.mainloop()

def pet():
    updateProgressbar(LoveProgressbar, 10)
    # messagebox.showinfo(title="Nachricht", message="Du hast es gestreichelt")

def feed():
    updateProgressbar(HungerProgressbar, 10)
    # messagebox.showinfo(title="Nachricht", message="Du hast es gefüttert")

def sleep():
    updateProgressbar(TirednessProgressbar, 10)
    # messagebox.showinfo(title="Nachricht", message="Es ist eingeschlafen")

def updateProgressbar(progressbar, addValue):
    value = progressbar["value"] + addValue
    progressbar["value"] = value

def shortcut(event):
    if event.state == 12 and event.keysym == "p":
        pet()
    if event.state == 12 and event.keysym == "f":
        feed()
    elif event.state == 12 and event.keysym == "s":
        sleep()

GUI()