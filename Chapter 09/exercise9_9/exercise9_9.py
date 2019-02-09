#9. Blackjack Simulation
#Previously in this chapter you saw the card_dealer.py program that simulates cards being
#dealt from a deck. Enhance the program so it simulates a simplified version of the game of
#Blackjack between two virtual players.

#The cards have the following values:
#• Numeric cards are assigned the value they have printed on them. For example, the value
#  of the 2 of spades is 2, and the value of the 5 of diamonds is 5.

#• Jacks, queens, and kings are valued at 10.

#• Aces are valued at 1 or 11, depending on the player’s choice.

#The program should deal cards to each player until one player’s hand is worth more than
#21 points. When that happens, the other player is the winner. (It is possible that both
#players’ hands will simultaneously exceed 21 points, in which case neither player wins.) The
#program should repeat until all the cards have been dealt from the deck.

#If a player is dealt an ace, the program should decide the value of the card according to the
#following rule: The ace will be worth 11 points, unless that makes the player’s hand exceed
#21 points. In that case, the ace will be worth 1 point.
import random
def createDeck():
    value = ('Ace','2','3','4','5','6','7','8','9','Jack','Queen','King')
    suit = ('of Hearts','of Spades','of Clubs','of Diamonds')
    deck = dict()
    counter = 1
    for element in suit:
        for item in value:
            deck[item+ ' ' + element] = counter
            if counter < 10:
                counter += 1
            else:
                counter = 10
        counter = 1
    return deck

def deal_cards(a_deck):
    player1_hand = 0
    player2_hand = 0
    player1_score = 0
    player2_score = 0
    
    for count in range(len(a_deck)//2):
        card1 = random.choice(list(a_deck.keys()))
        value1 = a_deck[card1]
        del a_deck[card1]
        print(card1)
        if card1.startswith('Ace') and (11 + player1_hand) < 21:
            value1 = 11
        else:
            value1 = 1
        player1_hand += value1
        print('Player1:',player1_hand)
        card2 = random.choice(list(a_deck.keys()))
        value2 = a_deck[card2]
        del a_deck[card2]
        print(card2)
        if card2.startswith('Ace') and (11 + player2_hand) < 21:
            value2 = 11
        else:
            value2 = 1
        player2_hand += value2
        print('Player2:',player2_hand)
        if player1_hand > 21 and player2_hand > 21:
            print('No one wins')
            player1_hand = 0
            player2_hand = 0
        elif player1_hand > 21 and player2_hand <= 21:
            print('Player 2 wins')
            player2_score += 1
            player1_hand = 0
            player2_hand = 0
        elif player2_hand > 21 and player1_hand <= 21:
            print('Player 1 wins')
            player1_score += 1
            player1_hand = 0
            player2_hand = 0
        else:
            'Round Continues.'
    print('Player 1:',player1_score)
    print('Player 2:',player2_score)
    if player1_score > player2_score:
        print('Player 1 wins!')
    elif player2_score > player1_score:
        print('Player 2 wins!')
    else:
        print('It is a TIE!')
def main():
    deck = createDeck()
    deal_cards(deck)

main()
