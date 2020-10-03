import random
suits = ("diamonds", "hearts", "spades", "club")
ranks = ("two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace")
value = {"two": 2, "three":3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 11, "queen": 12, "king": 13, "ace": 14}


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = value[self.rank]

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def shuffle(self):
        return random.shuffle(self.deck)

    def pop_card(self):
        return self.deck.pop()


class Player:
    def __init__(self):
        self.all_cards = []

    def add_card(self, card):
        if isinstance(card, list):
            self.all_cards.extend(card)
        else:
            self.all_cards.append(card)

    def pop_card(self):
        return self.all_cards.pop(0)

    def __len__(self):
        return len(self.all_cards)


deck = Deck()
deck.shuffle()

print(len(deck.deck))
player_one = Player()
player_two = Player()

for x in range(26):
    player_one.add_card(deck.pop_card())
    player_two.add_card(deck.pop_card())

player_one_on_table = []
player_two_on_table = []

# logic of game play
r = 0
game_on = True
while game_on:
    r += 1
    print(f"Round {r}")
    if len(player_one.all_cards) == 0:
        print("Player 1 out of cards, player 2 wins")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player 2 out of cards,player 1 wins!")
        game_on = False
        break

    player_one_on_table = []
    player_two_on_table = []

    player_one_on_table.append(player_one.pop_card())
    player_two_on_table.append(player_two.pop_card())

    if player_one_on_table[-1].value > player_two_on_table[-1].value:
        player_one.add_card(player_two_on_table[-1])
        player_one.add_card(player_one_on_table[-1])
    elif player_two_on_table[-1].value > player_one_on_table[-1].value:
        player_two.add_card(player_two_on_table[-1])
        player_two.add_card(player_one_on_table[-1])
    elif player_one_on_table[-1].value == player_two_on_table[-1].value:
        at_war = True
        while at_war:
            if len(player_one.all_cards) < 10:
                print("Player 2 wins!")
                game_on = False
                break
            elif len(player_two.all_cards) < 10:
                print("Player 1 wins!")
                game_on = False
                break
            else:
                for i in range(10):
                    player_one_on_table.append(player_one.pop_card())
                    player_two_on_table.append(player_two.pop_card())

                if player_one_on_table[-1].value > player_two_on_table[-1].value:
                    player_one.add_card(player_two_on_table)
                    player_one.add_card(player_one_on_table)
                    at_war = False
                    #break
                elif player_two_on_table[-1].value > player_one_on_table[-1].value:
                    player_two.add_card(player_one_on_table)
                    player_two.add_card(player_two_on_table)
                    at_war = False
                    #break
