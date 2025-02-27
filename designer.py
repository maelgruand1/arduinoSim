import tkinter as tk

class SimulateurArduino:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=300)
        self.canvas.pack()

# Création de la fenêtre principale
window = tk.Tk()
simulateur = SimulateurArduino(window)
simulateur.mainloop()
