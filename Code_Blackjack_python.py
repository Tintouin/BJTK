import random
import tkinter as tk
from PIL import Image, ImageTk

class Carte():
    def __init__(self, hauteur, couleur):
        self.hauteur = hauteur
        self.couleur = couleur
        self.imageCarte = None  # Variable pour stocker l'image
        self.pos = [0, 0]

    def __repr__(self):
        dicolor = {"P": " de Pique", "C": " de Coeur", "T": " de Trèfle", "K": " de Carreau"}
        dichauteur = {1: "As", 2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq", 6: "Six", 7: "Sept", 8: "Huit", 9: "Neuf", 10: "Dix"}
        return dichauteur[self.hauteur] + dicolor[self.couleur]

    def load_image(self, parent, resize_factor=0.3):
        fichier = "cards/{}_{}.png".format(self.hauteur, self.couleur)
        image = Image.open(fichier)
        width, height = image.size
        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)
        image_resized = image.resize((new_width, new_height), Image.ANTIALIAS)
        self.imageCarte = ImageTk.PhotoImage(image_resized)
        label = tk.Label(parent, image=self.imageCarte)
        label.image = self.imageCarte  # Garder une référence à l'image
        label.grid(row=self.pos[0] + 1, column=self.pos[1] + 1, padx=10 )  # Utilisation de grid pour l'affichage horizontal

def load_cartes():
    suits = ['P', 'C', 'T', 'K']
    face_cards = [11, 12, 13]

    # Create a list to store all Carte instances
    cartes = []

    # for each suit, retrieve the image for the cards
    for suit in suits:
        # first the number cartes 1 to 10
        for hauteur in range(1, 11):
            carte = Carte(hauteur, suit)
            cartes.append(carte)

        # next the face cartes
        for hauteur in face_cards:
            carte = Carte(hauteur, suit)
            cartes.append(carte)

    return cartes

def shuffle_cartes(cartes):
    random.shuffle(cartes)

def deal_cartes(frame, cartes):
    if cartes:
        carte = cartes.pop(0)
        carte.load_image(frame)
        return carte
    else:
        return None

def score_main(hand):
    # Calculate the total score of all cartes in the list
    # Only one ace can have the value 11 and this will be reduced to 1 if the hand would bust
    score = 0
    ace = False
    for carte in hand:
        hauteur = carte.hauteur
        if hauteur == 1 and not ace:
            ace = True
            hauteur = 11
        score += hauteur
        # if we would bust, check if there is an ace and subtract 10
        if score > 21 and ace:
            score -= 10
            ace = False
    return score

def deal_dealer():
    dealer_score = score_main(dealer_hand)
    while 0 < dealer_score < 17:
        carte = deal_cartes(dealer_card_frame, cartes)
        if carte:
            dealer_hand.append(carte)
        dealer_score = score_main(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_main(player_hand)
    if player_score > 21:
        result_text.set("Le croupier gagne !")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Le joueur gagne !")
    elif dealer_score > player_score:
        result_text.set("Le croupier gagne !")
    else:
        result_text.set("Égalité !")

def deal_player():
    carte = deal_cartes(player_card_frame, cartes)
    if carte:
        player_hand.append(carte)
    player_score = score_main(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Le croupier gagne !")

def initial_deal():
    deal_player()
    carte = deal_cartes(dealer_card_frame, cartes)
    if carte:
        dealer_hand.append(carte)
    dealer_score_label.set(score_main(dealer_hand))
    deal_player()

def new_game():
    global dealer_card_frame
    global player_card_frame
    global dealer_hand
    global player_hand
    # embedded frame to hold the card images
    dealer_card_frame.destroy()
    dealer_card_frame = tk.Frame(card_frame, bg="green")
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

    # embedded frame to hold the card images
    player_card_frame.destroy()
    player_card_frame = tk.Frame(card_frame, bg="green")
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

    result_text.set("")

    # Create the list to store the dealer's and player's hands
    dealer_hand = []
    player_hand = []
    initial_deal()

def shuffle():
    shuffle_cartes(cartes)

def play():
    initial_deal()
    mainWindow.mainloop()

mainWindow = tk.Tk()

# Set up the screen and frames for the dealer and player
mainWindow.title("Black Jack")
mainWindow.geometry("640x480")
mainWindow.configure(bg="green")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=0)
mainWindow.columnconfigure(4, weight=5)
mainWindow.columnconfigure(5, weight=0)

result_text = tk.StringVar()
result = tk.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

card_frame = tk.Frame(mainWindow, relief="sunken", borderwidth=1, bg="black")
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

dealer_score_label = tk.IntVar()
tk.Label(card_frame, text="Croupier", bg="black", fg="white").grid(row=0, column=0)
tk.Label(card_frame, textvariable=dealer_score_label, bg="black", fg="white").grid(row=1, column=0)
# embedded frame to hold the card images
dealer_card_frame = tk.Frame(card_frame, bg="black")
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

player_score_label = tk.IntVar()

tk.Label(card_frame, text="Joueur", bg="black", fg="white").grid(row=2, column=0)
tk.Label(card_frame, textvariable=player_score_label, bg="black", fg="white").grid(row=3, column=0)
# embedded frame to hold the card images
player_card_frame = tk.Frame(card_frame, bg="black")
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

button_frame = tk.Frame(mainWindow)
button_frame.grid(row=3, column=1, columnspan=3, sticky='w')

player_button = tk.Button(button_frame, text="Tirer", command=deal_player, padx=8)
player_button.grid(row=0, column=0)

dealer_button = tk.Button(button_frame, text="Passer", command=deal_dealer, padx=5)
dealer_button.grid(row=0, column=1)

reset_button = tk.Button(button_frame, text="Nouvelle Partie", command=new_game)
reset_button.grid(row=0, column=2)

shuffle_button = tk.Button(button_frame, text="Mélanger", command=shuffle, padx=2)
shuffle_button.grid(row=0, column=3)

# Load cartes and shuffle them
cartes = load_cartes()
shuffle_cartes(cartes)

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

if __name__ == "__main__":
    play()
