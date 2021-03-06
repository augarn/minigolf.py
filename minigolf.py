import json
import sys
import operator

# coding UTF-8
# @author August Arnoldsson-Sukanya
# Date: 04-01-2019

def print_label(label_text):
    """
    Method prints a label in the terminal window.
    @param label_text text to print
    """ 
    print("*"*len(label_text))
    print(str(label_text))
    print("*"*len(label_text))

def menu():
    """Main menu for program."""
    print_label("Meny")
    print("1. Visa resultat")
    print("2. Registrera resultat")
    print("3. Radera resultat")
    print("4. Avsluta")
    register_menu_choice()

def register_menu_choice():
    state = input("Val: ")
    if(state == "1"):   # Visa resultat
        show_results()
    elif(state == "2"): # Registrera resultat
        register_result()
    elif(state == "3"): # Radera resultat
        remove_result()
    elif(state == "4"): # Avsluta
        sys.exit()
    else:
        print("Fel: ogiltigt menyval.")
        register_menu_choice()
        return

def register_sort_choice():
    print_label("Hur vill du sortera resultaten?")
    print("0) Namn")
    print("1) Varv 1")
    print("2) Varv 2")
    print("3) Varv 3")
    print("4) Totalt")
    print("5) Originalordning")
    while True:
        try:
            choice = int(input("Val (0-5): "))
            if(choice >= 0 and choice <= 5):
                return choice
                break
            else:
                print("Fel: ange ett värde mellan 0 och 5")
        except ValueError:
            print("Fel: ange ett värde mellan 0 och 5")

def register_sort_order_choice():
    print_label("I vilken ordning vill du sortera resultaten?")
    print("0) Fallande")
    print("1) Stigande")
 
    while True:
        try:
            sort_order_choice = int(input("Val (0-1): "))
            if(sort_order_choice >= 0 and sort_order_choice <= 1):
                return sort_order_choice
                break
            else:
                print("Fel: ange ett värde mellan 0 och 1")
        except ValueError:
            print("Fel: ange ett värde mellan 0 och 1")

def show_results():
    """Method for displaying all results in the save file"""
    config = []

    # 1. --- Load data from file and add to list structure ---
    try: # if file not empty
        with open(working_file, "r+") as json_data:
            data = json.load(json_data)
            config = data
            json_data.close()
    except json.decoder.JSONDecodeError: # file is empty
        pass
    except FileNotFoundError:
        print("Fel: filen finns ej.")
        sys.exit()
        

    # 2. --- Get sort choice from user by invoking method "register_sort_choice" ---
    choice = register_sort_choice()
    sort_order_choice = register_sort_order_choice()

    # 3. --- Print table of dictionary data in list structure ---
    print("Resultat")
    print("*"*60)
    table_template = "{name:8} {round_1:6} {round_2:6} {round_3:6} {total:5} {average:5}"
    print(table_template.format(name="NAMN", round_1="VARV 1", round_2="VARV 2", round_3="VARV 3", total="TOTAL", average="SNITT"))

    if(sort_order_choice == 0):
        sorting_order = True
    elif(sort_order_choice == 1):
        sorting_order = False

    # 4. --- Apply sorting choice --- 
    if(choice == 0): # sortera enligt namn
        sorted(config,key=operator.itemgetter('name'), reverse=sorting_order)
    elif(choice == 1): # sortera enligt varv 1
        config.sort(key=operator.itemgetter('round_1'), reverse=sorting_order)
    elif(choice == 2): # sortera enligt varv 2
        config.sort(key=operator.itemgetter('round_2'), reverse=sorting_order)
    elif(choice == 3): # sortera enligt varv 3
        config.sort(key=operator.itemgetter('round_3'), reverse=sorting_order)
    elif(choice == 4): # sortera enligt Totalt
        config.sort(key=operator.itemgetter('total'), reverse=sorting_order)
    elif(choice == 5): # sortera enligt Originalordning
        config.sort(key=operator.itemgetter('average'), reverse=sorting_order)
  
    for each_value in config: 
        print(table_template.format(**each_value))
    menu()

def register_result():
    """Method when registering a new result to our save file"""
    print_label("Lägg till resultat")

    # List which will hold existing data from save file
    config = []

    # 1. --- Get player name ---
    player_name = input("Namn: ")
    
    # 2. --- Ask user for round results. Input has to be int or user will be asked to input again ---
    while True:
        try:
            round_1 = int(input("Varv 1: "))
            break
        except ValueError:
            print("Fel, angivet värde måste vara ett heltal.")

    while True:
        try:
            round_2 = int(input("Varv 2: "))
            break
        except ValueError:
            print("Fel, angivet värde måste vara ett heltal.")

    while True:
        try:
            round_3 = int(input("Varv 3: "))
            break
        except ValueError:
            print("Fel, angivet värde måste vara ett heltal.")

    # 3. --- Load previous data first and import it to our list structure ---
    try: # if data exists in file
        with open(working_file, "r+") as json_data:
            data = json.load(json_data)
            config = data
            json_data.close()
    except: # file is empty => move on
        pass

    # 4. --- Save data in dictionary structure ---    
    player_data = {
                "name":str(player_name),
                "round_1":int(round_1),
                "round_2":int(round_2),
                "round_3":int(round_3),
                "total":int(round_1 + round_2 + round_3),
                "average":int((round_1 + round_2 + round_3)/3)
            }

    # 5. --- Add dictionary to list structure ---  
    config.append(player_data)

    # 6. --- Save list of dictionaries to ---
    with open(working_file, "w") as write_file:
        json.dump(config, write_file)
        write_file.close()

    # 7. --- Return to main menu --- 
    menu()

def remove_result():
    config = []
    # 1. --- Load data from file and add to list structure ---
    try: # if file not empty
        with open(working_file, "r+") as json_data:
            data = json.load(json_data)
            config = data
            json_data.close()
    except json.decoder.JSONDecodeError: # file is empty
        print("Fel: filen är tom.")
        menu()
        return
    except FileNotFoundError:
        print("Fel: filen finns inte.")
        menu()
        return
        
    # 2. --- Ask user for the name of the player who should be removed ---
    name_of_player = input("Ange namnet på spelaren du vill ta bort: ")
    
    # 3. --- Find the player in the list of players in "config" ---
    for idx, listings in enumerate(config):
        if listings["name"] == name_of_player:
            config.remove(listings)
            print("Ok: angiven spelare borttagen.")
            break
        elif idx == (len(config) - 1):   
            print("Fel: angiven spelare finns ej.")

    # 4. --- Update save file ---
    with open(working_file, "w") as write_file:
        json.dump(config, write_file)
        write_file.close()
    menu()

def open_file():
    global working_file
    global file
    try:
        working_file = input("Ange filnamnet med filändelsen .json inkluderad (exempelvis 'data.json' och inte enbart 'data): ")
        file = open(working_file, "r+")
        file.close()
    except FileNotFoundError:
        print("Fel, angiven fil finns inte. En ny fil med angivet namn kommer att skapas.")
        with open(working_file, 'w') as write_file:
            json.dump([],write_file)
            write_file.close()

# 1. --- Check if file exists before starting program ---
open_file() 

# 2. --- Introduce user ---
print_label("Klubbmästerskap i minigolf")       

# 3. --- Go to main menu ---
menu()