import tkinter as tk
import random
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.geometry("1800x900")
fenetre['background'] = 'green'

class Carte():
    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur
        self.imageCarte = None  # Variable pour stocker l'image

    def __repr__(self):
        dicolor = {"P": " de Pique", "C": " de Coeur", "T": " de Trèfle", "K": " de Carreau"}
        dichauteur = {1: "As", 2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq", 6: "Six", 7: "Sept", 8: "Huit", 9: "Neuf", 10: "Dix"}
        return dichauteur[self.hauteur] + dicolor[self.couleur]

    def image(self, parent, resize_factor=0.3):
        fichier = "Cards/" + str(self.hauteur) + self.couleur + ".png"
        image = Image.open(fichier)
        width, height = image.size
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)
        image_resized = image.resize((new_width, new_height), Image.ANTIALIAS)
        self.imageCarte = ImageTk.PhotoImage(image_resized)
        label = tk.Label(parent, image=self.imageCarte)
        label.image = self.imageCarte  # Garder une référence à l'image
        label.pack()

class PaquetDeCarte():
    def __init__(self, paquets):
        self.paquets = paquets

    def est_vide(self):
        return len(self.paquets) == 0

    def taille(self):
        return len(self.paquets)

    def battre(self):
        random.shuffle(self.paquets)

def piocher_carte():
    if paquet.paquets:
        carte_au_hasard = random.choice(paquet.paquets)
        carte_au_hasard.image(fenetre, resize_factor=0.3)
        paquet.paquets.remove(carte_au_hasard)

# Créer un bouton pour piocher une carte
bouton_piocher = tk.Button(fenetre, text="Piocher une carte", command=piocher_carte)
bouton_piocher.pack()

paquet = PaquetDeCarte([Carte(1, "P"), Carte(2, "T"), Carte(3, "C")])

fenetre.mainloop()


fenetre.mainloop()
