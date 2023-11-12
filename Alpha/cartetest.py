import tkinter as tk
import random
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.geometry("1800x900")
fenetre['background'] = 'green'

# Dictionnaires pour les correspondances de hauteur et de couleur
cartes_hauteur = {1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "T", 11: "V", 12: "D", 13: "R"}
cartes_color = {"P": "P", "C": "C", "T": "T", "K": "K"}

class Carte():
    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur
        self.imageCarte = None  # Variable pour stocker l'image
        self.pos=[0,0]

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
        label.grid(row=self.pos[0]+1, column=self.pos[1]+1, padx=10 )  # Utilisation de grid pour l'affichage horizontal

pioche=[]
# Créer un jeu de 52 cartes avec des codes
for couleur in ["P", "C", "T", "K"]:
    for hauteur in range(1, 14):
        code_carte = cartes_hauteur[hauteur] + cartes_color[couleur]
        pioche.append(code_carte)
random.shuffle(pioche)
croupier=[]
joueur=[]
print(pioche)

# Créer un bouton pour piocher une carte
bouton_piocher = tk.Button(fenetre, text="Piocher une carte", command=1+1)
bouton_piocher.grid(row=5)

fenetre.mainloop()
