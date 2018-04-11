class Deck():
		 
	def __init__(self):
		self.deck = []  # start with an empty list
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
    
	def __str__(self):
		deck_comp = ""
		for card in self.deck:
			deck_comp += "\n" + card.__str__()
		return "The deck has: " + "\n" + deck_comp

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		dealt_card = self.deck.pop()
		return dealt_card