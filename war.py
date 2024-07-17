import random

class Card:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def __lt__(self, other):
        return Card.values.index(self.value) < Card.values.index(other.value)
    
    def __eq__(self, other):
        return Card.values.index(self.value) == Card.values.index(other.value)

class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop(0) if self.cards else None

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw_card(self):
        return self.hand.pop(0) if self.hand else None
    
    def add_cards(self, cards):
        self.hand.extend(cards)

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.deal_cards()
    
    def deal_cards(self):
        while self.deck.cards:
            self.player1.add_cards([self.deck.draw()])
            self.player2.add_cards([self.deck.draw()])
    
    def play_round(self):
        input("Press Enter to draw cards...")
        p1_card = self.player1.draw_card()
        p2_card = self.player2.draw_card()
        
        if not p1_card or not p2_card:
            return
        
        print(f"{self.player1.name} plays: {p1_card}")
        print(f"{self.player2.name} plays: {p2_card}")
        
        if p1_card > p2_card:
            print(f"{self.player1.name} wins the round")
            self.player1.add_cards([p1_card, p2_card])
        elif p2_card > p1_card:
            print(f"{self.player2.name} wins the round")
            self.player2.add_cards([p1_card, p2_card])
        else:
            print("War!")
            self.handle_war(p1_card, p2_card)
    
    def handle_war(self, p1_card, p2_card):
        war_pile = [p1_card, p2_card]
        
        for _ in range(1):
            if self.player1.hand:
                war_pile.append(self.player1.draw_card())
            if self.player2.hand:
                war_pile.append(self.player2.draw_card())
        
        p1_card = self.player1.draw_card()
        p2_card = self.player2.draw_card()
        
        if not p1_card or not p2_card:
            return
        
        print(f"War cards: {self.player1.name} plays: {p1_card} and {self.player2.name} plays: {p2_card}")
        
        if p1_card > p2_card:
            print(f"{self.player1.name} wins the war")
            self.player1.add_cards(war_pile + [p1_card, p2_card])
        elif p2_card > p1_card:
            print(f"{self.player2.name} wins the war")
            self.player2.add_cards(war_pile + [p1_card, p2_card])
        else:
            print("Another war!")
            self.handle_war(p1_card, p2_card)
    
    def is_game_over(self):
        return not self.player1.hand or not self.player2.hand
    
    def get_winner(self):
        if len(self.player1.hand) > len(self.player2.hand):
            return self.player1.name
        elif len(self.player2.hand) > len(self.player1.hand):
            return self.player2.name
        else:
            return "It's a tie!"

def main():
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    game = Game(player1_name, player2_name)
    
    try:
        while not game.is_game_over():
            game.play_round()
    except KeyboardInterrupt:
        player1_cards = len(game.player1.hand)
        player2_cards = len(game.player2.hand)
        if player1_cards > player2_cards:
            print(f"\nThe game was ended with no winner but {game.player1.name} has more cards in his hand")
        elif player2_cards > player1_cards:
            print(f"\nThe game was ended with no winner but {game.player2.name} has more cards in his hand")
        else:
            print("\nThe game was ended with no winner and both players have an equal number of cards")
    else:
        print(f"Game over! Winner: {game.get_winner()}")

if __name__ == "__main__":
    main()
