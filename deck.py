import store as st

deck = []

rating =["Ace","Two","Three",
        "Four","Five","Six","Seven",
        "Eight","Nine","Ten",
        "jack","Queen","King"
            ]
suits=["hearts","Diamonds","Clubs","Spades"]
for suit in suits:
    for rank in rating:
        deck.append((rank, suit))

#print(deck)