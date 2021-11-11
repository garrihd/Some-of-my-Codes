# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions


import random


def name_to_number(name):
    if name == "rock":
        name = 0
        return(name)
    if name == "Spock":
        name = 1
        return (name)
    if name == "paper":
        name = 2
        return (name)
    if name == "lizard":
        name = 3
        return (name)
    if name == "scissors":
        name = 4
        return (name)

def number_to_name(number):
    if number == 0:
        number = "rock"
        return number
    if number == 1:
        number = "Spock"
        return number
    if number == 2:
        number = "paper"
        return number
    if number == 3:
        number = "lizard"
        return number
    if number == 4:
        number = "scissors"
        return number
def rpsls(player_choice):
    int_player_choice = name_to_number(player_choice)
    print("Player chooses",player_choice)
    int_computer = random.randrange(0, 5)
    computer = number_to_name(int_computer)
    print("Computer chooses", computer)
    print("")
    if ((int_player_choice - int_computer) % 5) == 0:
        print("No one wins")
    if ((int_player_choice - int_computer) % 5) == 1:
        print("Player wins")

    if ((int_player_choice - int_computer) % 5) == 2:
        print("Player wins")

    if ((int_player_choice - int_computer) % 5) == 3:
        print("Computer wins")

    if ((int_player_choice - int_computer) % 5) == 4:
        print("Computer wins")








rpsls("rock")
print("")
rpsls("Spock")
print("")
rpsls("lizard")
print("")
rpsls("paper")
print("")
rpsls("scissors")


print("")
print("")
print("")



print ("The number" , (name_to_number("rock")), "equates to the string, \"rock\" ")
print ("The number" , (name_to_number("Spock")), "equates to the string, \"Spock\" ")
print ("The number" , (name_to_number("paper")), "equates to the string, \"paper\" ")
print ("The number" , (name_to_number("lizard")), "equates to the string, \"lizard\" ")
print ("The number" , (name_to_number("scissors")), "equates to the string, \"scissors\" ")




