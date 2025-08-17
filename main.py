import random
import sys
name = input("Tell us your name! ").capitalize().strip()
print(f"Hey {name} welcome to the game!")

def play_again():
    play_game = input(f"Good game {name}! Play again(Y/N)? ").strip()
    if play_game.lower() in ["n", "no"]:
        print("Thanks for playing!")
        sys.exit()
    else:
        number_guesser()

def game_logic(numb):
    tries = 0
    while True:
        try:
            usr_gs = int(input("Guess the number: "))
            tries += 1
            if usr_gs == numb:
                if tries == 1:
                    print(f"Amazing! and guessed it in {tries} tries")
                    break
                else:
                    print(f"You win and guessed it in {tries} tries")
                    break  
            else:
                if usr_gs < numb: print("Oh no! Try higher")         
                if usr_gs > numb: print("Oh no! Try lower")
        except ValueError:
                print("Please enter only numbers")
    play_again()       

def number_guesser():
        while True:    
            try:
                uppr_lmt = int(input("Enter upper limit number: "))
                if uppr_lmt <= 0:
                    print("Upper limit must be greater than 0. Don't break the game")
                else:
                    numb = random.randint(0, uppr_lmt)
                    game_logic(numb) 
            except ValueError:
                print("Please enter only numbers")

number_guesser()
