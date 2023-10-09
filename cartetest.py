import tkinter as tk

class Carte():
    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur
        self.imageCarte = None  # Variable pour stocker l'image

    def __repr__(self):
        dicolor={"P":" de Pique","C":" de Coeur","T":" de Trèfle","K":" de Carreau"}
        dichauteur={1:"As",2:"Deux",3:"Trois",4:"Quatre",5:"Cinq",6:"Six",7:"Sept",8:"Huit",9:"Neuf",10:"Dix"}
        return dichauteur[self.hauteur] + dicolor[self.couleur]

    def image(self):
        fichier = "big/" + str(self.hauteur) + self.couleur + ".png"
        fenetre = tk.Tk()
        fenetre.geometry('135x192+1000+400')
        self.imageCarte = tk.PhotoImage(file=fichier)  # Stocker l'image dans la variable
        label = tk.Label(fenetre, image=self.imageCarte)
        label.pack()
        fenetre.mainloop()

class PaquetDeCarte():
    def __init__(self,paquets):
        self.paquets=paquets
    def __repr__(self):
        return str(self.paquets)

        
carte = Carte(7, "C")
print(carte)
paquet=PaquetDeCarte([Carte(10,"P"),Carte(2,"T"),Carte(1,"P")])
print(paquet)
carte.image()








# import tkinter as tk

# class Carte():
#     def __init__(self,hauteur,couleur):
#         self.hauteur=hauteur
#         self.couleur=couleur
#     def __repr__ (self):
#         return str(self.hauteur)+self.couleur
#     def image(self):
#         fichier="U:/Pixel-Poker-Playing-Cards-main/Pixel-Poker-Playing-Cards-main/big/7K.png"
#         #fichier="big/"+str(self.hauteur)+self.couleur+".png"
#         fenetre=tk.Tk()
#         fenetre.geometry('135x192+1000+400')
#         image_carte=tk.PhotoImage(file=fichier)
#         label=tk.Label(fenetre,image=image_carte)
#         label.pack()
#         fenetre.mainloop()

        
# carte= Carte(7,"R")
# print(carte)
# carte.image()