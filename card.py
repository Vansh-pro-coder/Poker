import random
import deck as dk

# class deck:
#     rating =["Ace","Two","Three",
#         "Four","Five","Six","Seven",
#         "Eight","Nine","Ten",
#         "jack","Queen","King"
#             ]
#     suits=["hearts","Diamonds","Clubs","Spades"]
#     suit={
#         "Hearts":{"colour":"Red", "symbol":"♥"},
#         "Diamonds":{"colour":"Red", "symbol":"♦"},
#         "Clubs":{"colour":"Red", "symbol":"♣"},
#         "Spades":{"colour":"Red", "symbol":"♠"}
#     }

class cards:
    rating =["Ace","Two","Three",
        "Four","Five","Six","Seven",
        "Eight","Nine","Ten",
        "jack","Queen","King"
            ]
    suit={
        "Hearts":{"colour":"Red", "symbol":"♥"},
        "Diamonds":{"colour":"Red", "symbol":"♦"},
        "Clubs":{"colour":"Red", "symbol":"♣"},
        "Spades":{"colour":"Red", "symbol":"♠"}
    }
    def shuffle():
        random.shuffle(dk.deck.rating)
        print("cards are shuffled successfully")
        return cards.rating
    def random_card_selection(self):
        self.card_no = random.choice(dk.deck.rating)
        self.suit = random.choice(dk.deck.suits)
        print(f"Your card is {self.card_no} of {self.suit}")
        return self.card_no and self.suit
random_card=cards.random_card_selection(cards)

# print("type 1 to draw a random card from deck")
# k=int(input("Tell your response:- ")) 
    
# memory = random_card
# if k ==2:
#     print(f"drawn card was {cards.random_card_selection(cards)}")

#print(card_1)
#print(cards.shuffle())#
#print(k)

    
#     13 Hearts ♥
# 13 Diamonds ♦
# 13 Clubs ♣
# 13 Spades ♠

    # hearts=[
    #     "Ace♥","Two","Three",
    #     "Four","Five","Six","Seven",
    #     "Eight","Nine","Ten"
    #     "jack","Queen","King"
    #         ]
    # Diamonds=[
    #     "Ace","Two","Three",
    #     "Four","Five","Six","Seven",
    #     "Eight","Nine","Ten"
    #     "jack","Queen","King"
    #         ]
    # Clubs=[
    #     "Ace","Two","Three",
    #     "Four","Five","Six","Seven",
    #     "Eight","Nine","Ten"
    #     "jack","Queen","King"
    #         ]
    # Spades=[
    #     "Ace","Two","Three",
    #     "Four","Five","Six","Seven",
    #     "Eight","Nine","Ten"
    #     "jack","Queen","King"
    #         ]