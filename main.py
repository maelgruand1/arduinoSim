import tkinter as tk
import designer

# Création de la fenêtre principale
root = tk.Tk()
root.geometry("800x800")
root.title("Simulator Arduino")

def simulateurArduino(master):
    canvas = tk.Canvas(master, width=400, height=300)
    canvas.pack()

def openWindow():
    # Exemple de fonction pour ouvrir une nouvelle fenêtre
    new_window = tk.Toplevel(root)
    new_window.geometry("400x400")
    new_window.title("New Editor Window")
    label = tk.Label(new_window, text="Bienvenue dans l'éditeur")
    label.pack()

# Appel de la fonction simulateurArduino
simulateurArduino.mainloop
simulateurArduino(root)

# Création du bouton pour ouvrir une nouvelle fenêtre
button = tk.Button(root, text="Open Editor", command=openWindow)
button.pack()

# Lancer la boucle principale de l'application
root.mainloop()
