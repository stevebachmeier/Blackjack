def player_busts(chips):
    print("You bust!")
    chips.lose_bet()

def player_wins(chips):
    print("You win!")
    chips.win_bet()

def dealer_busts(chips):
    print("The dealer busts!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("The dealer wins!")
    chips.lose_bet()
    
def push():
    print("It's a push!")