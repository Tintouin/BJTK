import random
import tkinter as tk

class CardGame:
    def __init__(self, master):
        self.master = master
        master.title("Black Jack")
        master.geometry("640x480")
        master.configure(bg="green")

        self.result_text = tk.StringVar()
        self.result = tk.Label(master, textvariable=self.result_text)
        self.result.grid(row=0, column=0, columnspan=3)

        self.card_frame = tk.Frame(master, relief="sunken", borderwidth=1, bg="black")
        self.card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

        self.dealer_score_label = tk.IntVar()
        tk.Label(self.card_frame, text="Dealer", bg="black", fg="white").grid(row=0, column=0)
        tk.Label(self.card_frame, textvariable=self.dealer_score_label, bg="black", fg="white").grid(row=1, column=0)

        self.dealer_card_frame = tk.Frame(self.card_frame, bg="black")
        self.dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

        self.player_score_label = tk.IntVar()
        tk.Label(self.card_frame, text="Player", bg="black", fg="white").grid(row=2, column=0)
        tk.Label(self.card_frame, textvariable=self.player_score_label, bg="black", fg="white").grid(row=3, column=0)

        self.player_card_frame = tk.Frame(self.card_frame, bg="black")
        self.player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

        self.button_frame = tk.Frame(master)
        self.button_frame.grid(row=3, column=1, columnspan=3, sticky='w')

        self.player_button = tk.Button(self.button_frame, text="Hit", command=self.deal_player, padx=8)
        self.player_button.grid(row=0, column=0)

        self.dealer_button = tk.Button(self.button_frame, text="Stay", command=self.deal_dealer, padx=5)
        self.dealer_button.grid(row=0, column=1)

        self.reset_button = tk.Button(self.button_frame, text="New Game", command=self.new_game)
        self.reset_button.grid(row=0, column=2)

        self.shuffle_button = tk.Button(self.button_frame, text="Shuffle", command=self.shuffle, padx=2)
        self.shuffle_button.grid(row=0, column=3)

        self.cards = []
        self.load_images()
        self.deck = list(self.cards) + list(self.cards) + list(self.cards)
        self.shuffle()

        self.dealer_hand = Hand(self.dealer_card_frame)
        self.player_hand = Hand(self.player_card_frame)

    def load_images(self):
        suits = ['heart', 'club', 'diamond', 'spade']
        face_cards = ['jack', 'queen', 'king']

        if tk.TkVersion >= 8.6:
            extension = 'png'
        else:
            extension = 'ppm'

        for suit in suits:
            for card in range(1, 11):
                name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
                image = tk.PhotoImage(file=name)
                self.cards.append((card, image, ))

            for card in face_cards:
                name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
                image = tk.PhotoImage(file=name)
                self.cards.append((10, image, ))

    def _deal_card(self, hand):
        next_card = self.deck.pop(0)
        self.deck.append(next_card)
        tk.Label(hand.frame, image=next_card[1], relief="raised").pack(side="left")
        return next_card

    def score_hand(self, hand):
        score = 0
        ace = False
        for next_card in hand.cards:
            card_value = next_card[0]
            if card_value == 1 and not ace:
                ace = True
                card_value = 11
            score += card_value
            if score > 21 and ace:
                score -= 10
                ace = False
        return score

    def deal_dealer(self):
        dealer_score = self.score_hand(self.dealer_hand)
        while 0 < dealer_score < 17:
            self.dealer_hand.add_card(self._deal_card(self.dealer_hand))
            dealer_score = self.score_hand(self.dealer_hand)
            self.dealer_score_label.set(dealer_score)

        player_score = self.score_hand(self.player_hand)
        if player_score > 21:
            self.result_text.set("Dealer wins!")
        elif dealer_score > 21 or dealer_score < player_score:
            self.result_text.set("Player wins!")
        elif dealer_score > player_score:
            self.result_text.set("Dealer wins!")
        else:
            self.result_text.set("Draw!")

    def deal_player(self):
        self.player_hand.add_card(self._deal_card(self.player_hand))
        player_score = self.score_hand(self.player_hand)

        self.player_score_label.set(player_score)
        if player_score > 21:
            self.result_text.set("Dealer Wins!")

    def initial_deal(self):
        self.deal_player()
        self.dealer_hand.add_card(self._deal_card(self.dealer_hand))
        self.dealer_score_label.set(self.score_hand(self.dealer_hand))
        self.deal_player()

    def new_game(self):
        self.dealer_card_frame.destroy()
        self.dealer_card_frame = tk.Frame(self.card_frame, bg="green")
        self.dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

        self.player_card_frame.destroy()
        self.player_card_frame = tk.Frame(self.card_frame, bg="green")
        self.player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

        self.result_text.set("")

        self.dealer_hand = Hand(self.dealer_card_frame)
        self.player_hand = Hand(self.player_card_frame)

        self.initial_deal()

    def shuffle(self):
        random.shuffle(self.deck)

    def play(self):
        self.initial_deal()
        self.master.mainloop()

class Hand:
    def __init__(self, frame):
        self.frame = frame
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

if __name__ == "__main__":
    root = tk.Tk()
    game = CardGame(root)
    game.play()
