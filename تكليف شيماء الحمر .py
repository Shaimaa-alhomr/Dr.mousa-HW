import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)


player1_hand = deck[:26]
player2_hand = deck[26:]


rounds = 0
while player1_hand and player2_hand and rounds < 1000
    rounds += 1
    card1 = player1_hand.pop(0)
    card2 = player2_hand.pop(0)

    print(f"Round {rounds}:")
    print(f"Player 1: {card1}")
    print(f"Player 2: {card2}")

    if ranks.index(card1[0]) > ranks.index(card2[0]):
        print("Player 1 wins this round!")
        player1_hand.extend([card1, card2])
    elif ranks.index(card1[0]) < ranks.index(card2[0]):
        print("Player 2 wins this round!")
        player2_hand.extend([card1, card2])
    else:
        print("War!")

print("Game Over!")
if len(player1_hand) > len(player2_hand):
    print("Player 1 wins!")
elif len(player1_hand) < len(player2_hand):
    print("Player 2 wins!")
else:
    print("It's a tie!")