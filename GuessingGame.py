import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
empty_list_player = []
empty_list_pc = []
count = 0
game_on = True


def deal_player():
    
    card = random.choice(cards)
    empty_list_player.append(card)
        

def deal_computer():
    card_pc = random.choice(cards)
    empty_list_pc.append(card_pc)
    
    
   
def new_game():
    global empty_list_player, empty_list_pc
    empty_list_player = []
    empty_list_pc = []
    deal_player()
    deal_player()
    deal_computer()
    deal_computer()
    print("PC ", empty_list_pc[0])
    print("Person ",empty_list_player, sum(empty_list_player))
    if sum(empty_list_player) == 21:
        print("BLACK JACK !, YOU WIN !")
        return
    ask()
    print_sum()

    

def print_sum():
    print("PC ",empty_list_pc, sum(empty_list_pc))
    print("Person ", empty_list_player, sum(empty_list_player))
            
def ask():    
    question = input("Type 'y' to get another card, type 'n' to pass: ")
    if question == 'y':
        deal_player()
        print_sum()
        if check_sum_of_cards_player() > 21 :
            print("you loose")
            return
        if check_sum_of_cards_player() == 21:
            print("winner !")
            return        
        if check_sum_of_cards_player() <21 :
            ask()
    else:
        deal_computer()
        
        if check_sum_of_cards_computer() > 21 :
            print("Player wins")
            return
        if check_sum_of_cards_computer() == 21:
            print("Computer wins !")
            return        
        if check_sum_of_cards_computer() <21 :
            if check_sum_of_cards_computer() > check_sum_of_cards_player():
                print("Computer Wins!")
                return

def check_sum_of_cards_player():
    if 11 in empty_list_player and sum(empty_list_player) > 21:
        empty_list_player.remove(11)
        empty_list_player.append(1)
    return sum(empty_list_player)

def check_sum_of_cards_computer():
    if 11 in empty_list_pc and sum(empty_list_pc) > 21:
        empty_list_pc.remove(11)
        empty_list_pc.append(1)
    return sum(empty_list_pc)

def play_game():
    if ask() == 'y':
        deal_player()
        print_sum()
        if check_sum_of_cards_player() >21 :
            print("you loose")
        


new_game()        
   
    
    
