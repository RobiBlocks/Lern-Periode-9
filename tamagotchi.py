import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import ttk
import random
import sys

window = tk.Tk()

def startGame():
    # Fenstergröße
    width = 1000
    height = 500

    # Berechne die Position, um das Fenster zu zentrieren
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_pos = (screen_width // 2) - (width // 2)
    y_pos = ((screen_height - 100) // 2) - (height // 2)
    
    window.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
    window.title("Pinguin Tamagotchi")
    window.bind("<KeyPress>", shortcut)

    buttonFrame = tk.Frame(window)
    buttonFrame.columnconfigure(0, weight=1)
    buttonFrame.columnconfigure(1, weight=2)
    buttonFrame.columnconfigure(2, weight=1)
    buttonFrame.rowconfigure(0, weight=1)
    buttonFrame.rowconfigure(1, weight=1)
    buttonFrame.rowconfigure(2, weight=1)
    buttonFrame.rowconfigure(3, weight=1)

    image = tk.PhotoImage(file="pinguin.png")
    image = image.subsample(2, 2)
    imageTamagotchi = tk.Label(buttonFrame, image=image)
    imageTamagotchi.grid(row=1, rowspan=3, column=1, sticky="nswe")

    buttonStreicheln = tk.Button(buttonFrame, text="Streicheln", font=('Arial', 12), bg="#ffff00", height=8, command=pet)
    buttonStreicheln.grid(row=1, column=0, sticky="we")

    buttonFeed = tk.Button(buttonFrame, text="Füttern", font=('Arial', 12), bg="#ff3c00", height=8, command=feed)
    buttonFeed.grid(row=2, column=0, sticky="we")

    buttonSleep = tk.Button(buttonFrame, text="Schlafen", font=('Arial', 12), bg="#008cff", height=8, command=sleep)
    buttonSleep.grid(row=3, column=0, sticky="we")

    global LoveProgressbar
    LoveProgressbar = ttk.Progressbar(buttonFrame, mode="determinate", value=100)
    LoveProgressbar.grid(row=1, column=2, sticky="we")

    global HungerProgressbar
    HungerProgressbar = ttk.Progressbar(buttonFrame, mode="determinate", value=100)
    HungerProgressbar.grid(row=2, column=2, sticky="we")

    global TirednessProgressbar
    TirednessProgressbar = ttk.Progressbar(buttonFrame, mode="determinate", value=100)
    TirednessProgressbar.grid(row=3, column=2, sticky="we")

    buttonFrame.pack(fill="x", padx=20, pady=20)

    window.after(1000, gameCycle)
    window.mainloop()

def gameCycle():
    generateIllness()
    lowerStats()
    window.after(1000, gameCycle)

def pet():
    addValueToProgressbar(LoveProgressbar, 15)

def feed():
    addValueToProgressbar(HungerProgressbar, 20)

def sleep():
    messagebox.showinfo(title="Nachricht", message="Dein Pinguin ist eingeschlafen")
    addValueToProgressbar(TirednessProgressbar, 30)

def addValueToProgressbar(progressbar, addValue):
    if progressbar["value"] <= 100:
        value = progressbar["value"] + addValue
        if value > 100:
            value = 100
        progressbar["value"] = value

def removeValueFromProgressbar(progressbar, removeValue):
    value = progressbar["value"] - removeValue
    progressbar["value"] = value

def lowerStats():
    
    if LoveProgressbar["value"] == 0:
        messagebox.showerror(title="Tod", message="Dein Pinguin ist wegen Liebesentzug gestroben!")
        sys.exit()  # Beendet das Skript

    elif HungerProgressbar["value"] == 0:
        messagebox.showerror(title="Tod", message="Dein Pinguin ist verhungert!")
    elif TirednessProgressbar["value"] == 0:
        messagebox.showerror(title="Tod", message="Dein Pinguin ist durch Müdigkeit gestroben!")

def generateIllness():
    # 1 - Einsamkeitssanfall
    # 2 - Hungeranfall
    # 3 - Müdigkeitsanfall
    rnd = random.randint(1, 20)
    if rnd == 1:  
        removeValueFromProgressbar(LoveProgressbar, 10)
        removeValueFromProgressbar(HungerProgressbar, 2)
        removeValueFromProgressbar(TirednessProgressbar, 1)
    elif rnd == 2:
        removeValueFromProgressbar(LoveProgressbar, 3)
        removeValueFromProgressbar(HungerProgressbar, 10)
        removeValueFromProgressbar(TirednessProgressbar, 2)
    elif rnd == 3:
        removeValueFromProgressbar(LoveProgressbar, 3)
        removeValueFromProgressbar(HungerProgressbar, 2)
        removeValueFromProgressbar(TirednessProgressbar, 10)
    else:
        removeValueFromProgressbar(LoveProgressbar, 3)
        removeValueFromProgressbar(HungerProgressbar, 2)
        removeValueFromProgressbar(TirednessProgressbar, 1)

def shortcut(event):
    if event.state == 12 and event.keysym == "p":
        pet()
    if event.state == 12 and event.keysym == "f":
        feed()
    elif event.state == 12 and event.keysym == "s":
        sleep()

startGame()