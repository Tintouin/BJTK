import tkinter as tk
import random
from PIL import Image, ImageTk

fenetre = tk.Tk()
fenetre.geometry("1800x900")
fenetre['background']='green'



class Carte():
    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur
        self.imageCarte = None  # Variable pour stocker l'image

    def __repr__(self):
        dicolor = {"P": " de Pique", "C": " de Coeur", "T": " de Trèfle", "K": " de Carreau"}
        dichauteur = {1: "As", 2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq", 6: "Six", 7: "Sept", 8: "Huit", 9: "Neuf", 10: "Dix"}
        return dichauteur[self.hauteur] + dicolor[self.couleur]

    def image(self, parent, resize_factor=1):
        fichier = "Cards/" + str(self.hauteur) + self.couleur + ".png"
        image = Image.open(fichier)
        
        # Redimensionner l'image avec un facteur non entier
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

    def __repr__(self):
        return str(self.paquets)

    def est_vide(self):
        """Renvoie un booléen égal à True si le paquet ne contient aucune carte et False sinon."""
        return len(self.paquets) == 0

    def taille(self):
        """ Renvoie le nombre de cartes contenues dans un paquet de cartes."""
        return len(self.paquets)

    def battre(self):
        """Permet de battre le paquet de cartes, avec la fonction shuffle de la bibliothèque random."""
        random.shuffle(self.paquets)


carte = Carte(7, "C")
print(carte)
paquet = PaquetDeCarte([Carte(10, "P"), Carte(2, "T"), Carte(1, "P")])
print(paquet)
paquet.est_vide()
print(paquet)
carte.image(fenetre, resize_factor=0.3)  # Vous pouvez ajuster le facteur de redimensionnement ici



fenetre.mainloop()
