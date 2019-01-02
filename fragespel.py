# Coding="UTF-8"
import sys

"""Menu"""
state = ""

"""amount of questions answered"""
amount_questions_answered = 0

"""amount of questions answered correct"""
amount_questions_answered_correct = 0

def run():   
    """Main program sequence"""
    menu()
    if state == "1":
        question_game()
    elif state == "2":
        statistics()
    elif state == "3":
        sys.exit()
    else:
        print("felaktigt menyval, försök igen.")
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
    print_label("Meny")
    print("Val:")
    print("1. Frågespel")
    print("2. Statistik")
    print("3. Avsluta")
    state = input("Ditt val: ")

def question(question_text, answer_text):
    """Method which prints the question and check if the user answer is correct with answer argument
    @param question_text the question which the users is to answer
    @param question_answer the correct answer to the question
    """
    global amount_questions_answered
    global amount_questions_answered_correct
    print(str(question_text))
    input_answer = input("Ditt svar: ")
    if(input_answer.lower() == answer_text.lower()):
        print("Korrekt svar, snyggt jobbat!")
        amount_questions_answered += 1
        amount_questions_answered_correct += 1
        return
    elif(input_answer != answer_text):
        print("Tyvärr, angivet svar är felaktigt")
        amount_questions_answered += 1
        question(question_text, answer_text)

def question_game():
    """This is the question game section of the program. The user will answer all the available questions before returning to the main menu"""
    print_label("Välkommen till frågespelet!")
    question("Vilken är Skånes största stad?", "Malmö")
    question("Vilken tal är störst, 2 eller 5?", "5")
    run()

def statistics():
    """This is the statistics part of the program. The user can check amount of questions answered and how many of those questions that are incorrectly answered"""
    print_label("Välkommen till statistik!")
    print("Du har svarat på " + str(amount_questions_answered) + " frågor")
    print("Du har svarat fel " + str(amount_questions_answered - amount_questions_answered_correct) + " gånger")
    run()
run()