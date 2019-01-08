"""
@author August Arnoldsson
date: 2018-12-16
"""

# random import required for drafting 10 unique integers in our bingo game
import random

# sys import required for terminating program
import sys

# list of players 
list_of_players = []

# list which stores the scoring results for each round played
round_results = []

# valid numbers that a player may choose
valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

def establish_players():
    amount_of_players = input("Hur många är det som vill spela? ")
    try:
        for count in range(0,int(amount_of_players)):
            player_name = input("Namn på spelare: ")
            list_of_players.append(player_name)
    except ValueError:
        print("Fel, ange ett heltal.")
        establish_players(list_of_players)
   
def run():   
    """Main program sequence"""
    menu()
    # play game
    if state == "1":
        input_values()
    # show statistics
    elif state == "2":
        statistics()
    # exit application
    elif state == "3":
        sys.exit()
    else:
        print("Felaktigt menyval, försök igen.")
        run()

def print_label(label_text):
    """Print out a given argument with horizontal line above and below text
    @param label_text the message you want to print
    """
    print("*"*50)
    print(str(label_text))
    print("*"*50)

def menu():
    """Main menu for our program where user can choose which section to use"""
    global state
    print_label("Välkommen till Bingo!")
    print("Välj ett utav alternativen:")
    print("2. Bingo")
    print("2. Statistik")
    print("3. Avsluta")
    state = input("Ditt val: ")

def input_values():
    """Function asks the user to input five unique integers within interval 1-25"""
    # list which stores the numbers each player inputs
    player_values = []

    # list which stores the numbers the current player is inputting
    input_numbers = []
    
    for each_player in list_of_players:
        while True:
            try:
                input_numbers = input("SPELARE[" + str(each_player) + "] -- Ange fem siffror [1-25] (avgränsa med , ): ")
                temp_string = input_numbers.split(",")
                control_string = []
                if(len(temp_string) == 5):
                    try:
                        for each_character in temp_string:
                            if each_character in valid_numbers and each_character not in control_string:
                                control_string.append(each_character)
                            else:
                                print("Fel, en användare har använt dublett eller värde utanför tillåtet intervall.")
                                raise ValueError()
                        break
                    except ValueError:
                        pass
                else:
                    raise ValueError()
            except ValueError:
                print("Fel, mata in 5 tal")    
                pass
        player_values.append(input_numbers.split(","))
    draft(player_values)

def draft(player_values):
    # the numbers that the AI selected
    drafted_numbers = []
    
    # current player score
    score = 0 
    
    # list which stores the scoring results for a single round
    player_scores = []
    
    """Method chooses 10 random values from the valid range and then displays it on a playfield"""
    drafted_numbers = random.sample(valid_numbers, 10)
    for i in valid_numbers:
        if(int(i)%5 != 0):
            if i in drafted_numbers:
                print("[" + i + "]", end=" ")
            elif i not in drafted_numbers:
                print(" " + i + " ", end=" ")
        elif(int(i)%5 == 0):
            if i in drafted_numbers:
                print("[" + i + "]")
            elif i not in drafted_numbers:
                print(" " + i + " ")
            print("-"*50)
    
    for idx, each_entry in enumerate(player_values):
        score = 0
        for each_value in each_entry:
            if each_value in drafted_numbers:
                score += 1
        player_scores.append(score)
        print(list_of_players[idx] + ":"  + str(score))
    results = ','.join(str(e) for e in player_scores)
    player_scores.clear()
    round_results.append(results.split(","))
    run()

def statistics():
    for each_value in round_results:
        print_label("Runda " + str((round_results.index(each_value) + 1)))
        for idx, each_result in enumerate(each_value):
            print(str(list_of_players[idx])  + ":" + str(each_result))
    run()

establish_players()
run()