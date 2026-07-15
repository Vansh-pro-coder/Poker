player=[]

class Store_data:
    def __init__(self, name, chips=1000):
        self.name = name
        self.cards = []
        self.chips = chips
        self.current_bet = 0
        self.folded = False
    
    def show_details():
        for i in range(len(player)):
            print(player.name, player.chips, player.cards)