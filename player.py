import card as cd
import deck as dk
import store as st


participants=[]


c=cd.cards
class Player():
    def __init__(self, name, chips=1000):
        self.name = name
        self.cards = []
        self.chips = chips
        self.current_bet = 0
        self.folded = False

    def player_count():
        a=int(input("Number of players(1-6):"))
        # for i in range(a):
        #     participants_
        chips=int(input("default chips will be(1000 default):-"))
        for i in range(a):
            name=input(f"Enter player name({i+1}) :- ")
            st.player.append({"name":name,"chips":chips})   

        return a


    

    
#     def genrate_players(self,k):
#         self.player_1=[]
#         computer_2=[]
#         computer_3=[]
#         computer_4=[]
#         #for i in k:
#         if k == 2:
#             player_1=c.drawCards(generate,3)
#             computer_1=c.random_card_selection_pop(generate)
#             print(f"cards of player is:- {player_1} \ncards of computer is :-{computer_1}")
            
#         elif k==3:
#             player_1=c.random_card_selection_pop(generate)
#             computer_1=c.random_card_selection_pop(generate)
#             computer_2=c.random_card_selection_pop(generate)
#             print(player_1,computer_1,computer_2,)
            
#         elif k==4:
#             player_1=c.random_card_selection_pop(generate)
#             computer_1=c.random_card_selection_pop(generate)
#             computer_2=c.random_card_selection_pop(generate)
#             computer_3=c.random_card_selection_pop(generate)
#             print(player_1,computer_1,computer_2,computer_3)
            
#         # elif k==4:
#         #     player_1=c.drawCards(generate,3,player_1)
#         #     computer_1=c.random_card_selection_pop(generate)
#         #     computer_2=c.random_card_selection_pop(generate)
#         #     computer_3=c.random_card_selection_pop(generate)
#         #     print(player_1,computer_1,computer_2,computer_3)



    
    

        

        
#     @staticmethod
#     def playerNo():
#         k=int(input("Please tell me player numbers:"))
#         if k==4:
#             generate.genrate_players(4)
#         elif k==3:
#             generate.genrate_players(3)
#         elif k==2:
#             generate.genrate_players(2)
#         # elif k==1:
#         #     generate.genrate_players(1)

# x=generate.playerNo()