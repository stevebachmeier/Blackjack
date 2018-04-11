def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Place your bet: "))
        except:
            print("Bet must be an integer!")
            print("\n")
            continue
        else:
            if (chips.bet > chips.total):
                print(f"You only have {chips.total} chips to bet!")
                print("\n")
                continue
            elif (chips.bet == 0):
                print("You need to bet something!")
                print("\n")
                continue
            elif (chips.bet < 0):
                print("You must bet a positive number of chips!")
                print("\n")
                continue
            else:
                print(f"{chips.bet} chips bet - time to play!")
                print("\n")
                break
    return chips.bet