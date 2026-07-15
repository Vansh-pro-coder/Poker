import random
import deck as dk


class cards:
#-------------------------------------------------X--------------------------------------------

    def shuffle():
        random.shuffle(dk.deck.rating)
        print("cards are shuffled successfully")
        return cards.rating
    
#-------------------------------------------------X--------------------------------------------

    def random_card_selection(self):
        self.card_no = random.choice(dk.deck.rating)
        self.suit = random.choice(dk.deck.suits)
        #print(f"Your card is {self.card_no} of {self.suit}")
        return self.card_no, self.suit#this will make a tuple. use a tuple unpacking to use it

#-------------------------------------------------X--------------------------------------------

    def random_card_selection_pop(self):
            random.shuffle(dk.deck.rating)
            random.shuffle(dk.deck.suits)
           # self.c_1=dk.rating.pop()
            return dk.deck.rating.pop(),dk.deck.suits.pop()

#-------------------------------------------------X--------------------------------------------

    def __init__(self):
        self.player_name = []

#-------------------------------------------------X--------------------------------------------


    def drawCards(self,cards_to_draw):
        self.player_name=[]
        for i in range(cards_to_draw):
            self.player_name.append(cards.random_card_selection_pop(self))
        #print(self.player_name)
        return self.player_name
         














#random_card=cards.random_card_selection(cards)

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