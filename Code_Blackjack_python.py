import random

# Define the card values
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
}

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = sum(card_values[card['rank']] for card in hand)
    num_aces = sum(1 for card in hand if card['rank'] == 'A')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

# Function to display a player's hand
def display_hand(player, hand):
    print(f"{player}'s Hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total Value: {calculate_hand_value(hand)}")

# Initialize the game
player_hand = [random.choice(deck), random.choice(deck)]
dealer_hand = [random.choice(deck), random.choice(deck)]

# Display the initial hands
display_hand("Player", player_hand)
display_hand("Dealer", [dealer_hand[0]])

# Main game loop
while True:
    # Player's turn
    action = input("Do you want to 'hit' or 'stand'? ").lower()
    if action == 'hit':
        player_hand.append(random.choice(deck))
        display_hand("Player", player_hand)
        if calculate_hand_value(player_hand) > 21:
            print("Player busts. Dealer wins.")
            break
    elif action == 'stand':
        break
    else:
        print("Invalid input. Please enter 'hit' or 'stand'.")

# Dealer's turn
display_hand("Dealer", dealer_hand)
while calculate_hand_value(dealer_hand) < 17:
    dealer_hand.append(random.choice(deck))
    display_hand("Dealer", dealer_hand)

# Determine the winner
player_value = calculate_hand_value(player_hand)
dealer_value = calculate_hand_value(dealer_hand)
if player_value > 21:
    print("Player busts. Dealer wins.")
elif dealer_value > 21:
    print("Dealer busts. Player wins.")
elif player_value > dealer_value:
    print("Player wins.")
elif dealer_value > player_value:
    print("Dealer wins.")
else:
    print("It's a tie!")

