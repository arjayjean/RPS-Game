from email import message
import os
import time
import random

# CLEAR CONSOLE
def clear(): 
    os.system("clear")


# DELAY TIME
def delay(x):
    time.sleep(x)
    

# PLAYER'S NAME CONTAINER
clear()
delay(2)
P1 = input("What is your name?: ")
CPU = "CPU"


# GAME INTRO
def intro():
    clear()
    delay(1)
    
    
    # SCREEN MESSAGES FUNCTION
    def messages(msg, sec1, sec2):
        delay(sec1)
        print(msg)
        delay(sec2)
        clear()
    
    
    # WELCOME SCREEN
    messages(f'Welcome to Rock, Paper, Scissors, {P1}!', 0, 3)


    # INSTRUCTIONS
    messages("During this game, you will be playing against the CPU.", 2, 3)

    messages("The two of you will each randomly choose one of three choices...", 2, 3)

    delay(2)

    def picks(*options):
        for pick in options:
            print(f'{pick}\n')
            delay(1)

    picks('Rock = R', 'Paper = P', 'Scissors = S')
    delay(2)
    clear()
    

    # BEST 2 OUT OF 3 MESSAGE
    messages("Best 2 out of 3 WINS!!!", 2, 3)


    # WAITING SCREEN
    messages("LOADING...", 0, 10)
    clear

    # PREP SCREEN
    messages("GET READY!!!", 0, 5)
    

intro()


# RPS CADENCE
def rps(*cadence):
    for rps in cadence:
        clear()
        print(f'{rps}')
        delay(.5)
    delay(1) 
    clear()


# THE GAME FUNCTION
def rps_game():

    # CHOICES
    choices = ["R", "P", "S"]


    # PLAYER'S POINTS
    p1_points = 0
    cpu_points = 0


    while p1_points or cpu_points != 2:
        
        # SCOREBOARD
        def score():
            print("Score:\n")
            print(f'{P1}: {str(p1_points)}')
            print(f'{CPU}: {str(cpu_points)}')
            delay(3)
            clear()


        # ROCK, PAPER, SCISSORS FUNCTION
        rps('Rock...', 'Paper...', 'Scissors...', 'SHOOT!!!')  

        # PLAYER'S CHOICES
        p1_choice = ""
        cpu_choice = ""
        players_choices = ""

        cpu_choice = random.choice(choices)
        
        print("Rock, Paper, or Scissors?")
        p1_choice = input().upper()
        

        players_choices = f'{p1_choice} vs {cpu_choice}'

        clear()
        delay(2)
        

        # PLAYER'S WINNING OR A TIE PRESENTATION
        def who_won(winner):
            print(f'{players_choices}: {winner} Wins!')

        def tie_game():
            print(f'{players_choices}: It is a TIE!!')


        #HOW PLAYER'S WIN OR IF THERE IS A TIE
        how_p1_wins = ["R vs S", "S vs P", "P vs R"]
        how_cpu_wins = ["S vs R", "P vs S", "R vs P"]
        if_tie = ["S vs S", "P vs P", "R vs R"]

        # HOW PLAYER 1 WINS
        for w_p1 in how_p1_wins: 
            if players_choices == w_p1:
                who_won(P1)
                p1_points += 1
                delay(3)
                clear()
        
        # HOW CPU WINS
        for w_cpu in how_cpu_wins:
            if players_choices == w_cpu:
                who_won(CPU)
                cpu_points += 1
                delay(3)
                clear()
            
        # WHEN A TIE OCCURS
        
        for a_tie in if_tie:
            if players_choices == a_tie:
                tie_game()
                delay(3)
                clear()


        def champion(champ):
            print(f'{champ} is the CHAMPION\n')
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()


        # CHAMPION ANNOUNCEMENT
        if p1_points == 2:
            champion(P1)
            break
        elif cpu_points == 2:
            champion(CPU)
            break


        # OVERALL SCORE
        score()

rps_game()
