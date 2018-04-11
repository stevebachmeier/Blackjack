def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        next_move = input("Hit or stand? Type 'h' or 's': ")
        if (next_move[0].lower() == "h"):
            hit(deck,hand)
            print("\n")
            break
        elif (next_move[0].lower() == "s"):
            print("\n")
            print("You chose to stand. Dealer's turn: ")
            playing = False
            break
        else:
            print("\n")
            print("ERROR: improper input!")
            print("\n")
            continue