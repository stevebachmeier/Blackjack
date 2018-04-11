def show_all(player,dealer):
    print("\n")
    print("DEALER'S HAND:")
    for card in dealer.cards:
        print(f"  < {card} >")
    print(f"Total: {dealer.value}")
    print("\n")
    
    print("YOUR HAND:")
    for card in player.cards:
        print(f"  < {card} >")
    print(f"Total: {player.value}")