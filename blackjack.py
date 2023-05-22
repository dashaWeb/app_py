import random, sys
#https://inventwithpython.com/bigbookpython/appendixb.html
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADER = chr(9824)
CLUBS = chr(9827)

BACKSIDE = 'backside'

def main():
    print('''Blackjack
    Rules:
        Try to get as close to 21 without going over.
        Fings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points. 
        Cards 2 throungh 10 are worth their face value.
        (H)it to take another card. 
        (S)tand to stop taking cards. 
        On your first play, you can (D)ouble down to increase your bet 
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player. 
        The dealer stops hitting at 17. 
        ''')
    money = 5000
    while True:
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money. ")
            print("Thanks for playing!")
            sys.exit()
        
        print('Money: ', money)
        # bet = getBet(money)

def getBet(maxBet):
    while True:
        print('How much do you bet? (1 - {}, or QUIT)'.format(maxBet))
        bet = input('> ')
        if bet == 'QUIT':
            print("Thanks for playing!")
            sys.exit()

        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


    