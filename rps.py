# Rock, Paper, Scissors
#   Written by: GitHub @RyanBuitenhuis

import random

def rps():

    user = input("Choose your option [rock, paper, scissors]: ")
    computer = random.choice(['rock', 'paper', 'scissors'])
    print()

    #Verification on input.
    if user == 'rock' or user == 'paper' or user == 'scissors':

        print('The user chose: ', user)
        print('The computer chose: ', computer)
        print()

        #User loses
        if user == 'rock' and computer == 'paper':
            print("The computer wins")
        elif user == 'paper' and computer == 'scissors':
            print("The computer wins!")
        elif user == 'scissors' and computer == 'rock':
            print("The computer wins!")

        # Computer loses.
        if computer == 'rock' and user == 'paper':
            print("Congratulations, you win!")
        elif computer == 'paper' and user == 'scissors':
            print("Congratulations, you win!")
        elif computer == 'scissors' and user == 'rock':
            print("Congratulations, you win!")

        #User and Computer tie.
        if user == 'rock' and computer == 'rock':
            print("It is a draw!")
        elif user == 'paper' and computer == 'paper':
            print("It is a draw!")
        elif user == 'scissors' and computer == 'scissors':
            print("It is a draw!")
    
    #End of the verification, if values don't match, force a new one.
    elif user != 'rock' or user != 'paper' or user != 'scissors':
        print("Enter a valid value!")