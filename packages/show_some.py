def show_some(player,dealer):
    print("\n")
    print("DEALER'S HAND:")
    print("  < ??????????? >")
    print(f"  < {dealer.cards[1]} >")
    print("\n")
    
    print("YOUR HAND:")
    for card in player.cards:
        print(f"  < {card} >")