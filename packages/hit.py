def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()