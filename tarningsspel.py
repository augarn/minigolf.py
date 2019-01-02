# coding=UTF-8
from math import *
import random

# Sum of dice throws
real_sum = 0

# Value of dice throw
throw_value = 0

# User-guessed sum of dice throws
sum_guess = 0

# Username 
name = ""

# main program sequence
def sequence():
    welcome()
    greet_user(get_name())
    intermission()
    throw_dice()
    result()
    thank_user()
    
# welcome user
def welcome():
    print("-" * 50)
    print("Hej och välkommen till mitt tärningsspel!")
    print("-" * 50)

# get name
def get_name():
    global name
    name = input("Vem är det som vill spela? ")
    return name

# greet user
def greet_user(user):
    print(str(user) + ", vad roligt att du vill vara med att spela!")

def intermission():
    global sum_guess
    print("Vi kommer nu att slå 3 st tärningskast")
    sum_guess = input("Vad tror du att summan av tärningskasten blir? ")

# Throw dice 
def throw_dice():
    global throw_value
    global real_sum
    for i in range(3):
        throw_value = random.randint(1, 6)
        print("Tärningskast " + str(i + 1) + " visar: " + str(throw_value))
        real_sum += throw_value

# Print result
def result():
    print("-" * 50)
    print("Summan av tärningskasten är: " + str(real_sum))
    print("Du gissade på: " + str(sum_guess))
    print("Skillnaden mellan din gissning och resultatet är: " + str(abs(real_sum-int(sum_guess))))
    print("Hoppas att du är nöjd med din gissning!")
    print("-" * 50)

# Thank user
def thank_user():
    print("Tack " + str(name) + ", för din medverkan!")

# Run main program loop
sequence()