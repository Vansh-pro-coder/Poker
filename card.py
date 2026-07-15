import random
import deck as dk
#import player
import store as st


class cards:
#-------------------------------------------------X--------------------------------------------
    def __init__(self):
        self.player_name = []
        

    def shuffle():
        random.shuffle(dk.deck)
        print("cards are shuffled successfully")
        return cards.rating
    
#-------------------------------------------------X--------------------------------------------

    # def random_card_selection():
    #     self.card_no = random.choice(dk.deck)
    #     self.suit = random.choice(dk.deck)
    #     #print(f"Your card is {self.card_no} of {self.suit}")
    #     return self.card_no, self.suit#this will make a tuple. use a tuple unpacking to use it

#-------------------------------------------------X--------------------------------------------

    def random_card_selection_pop():
            random.shuffle(dk.deck)            
           # self.c_1=dk.rating.pop()
            return dk.deck.pop()

#-------------------------------------------------X--------------------------------------------


#-------------------------------------------------X--------------------------------------------

    @staticmethod
    def card_will_be_drawn_1_time_only():
        return cards.random_card_selection_pop()
    def drawCards(cards_to_draw):
         for i in range(cards_to_draw):
              st.player.append(cards.card_will_be_drawn_1_time_only())
         














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