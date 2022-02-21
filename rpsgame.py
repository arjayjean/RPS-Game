import os
import time
import random

# CLEAR CONSOLE
def clear(): 
    os.system("clear")

# DELAY TIME
def delay(sec):
    time.sleep(sec)
    
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
    def screen(message, sec1, sec2):
        delay(sec1)
        print(message)
        delay(sec2)
        clear()
    
    # WELCOME SCREEN
    screen(f'Welcome to a game of Rock, Paper, Scissors, {P1}!', 0, 3)

    # INSTRUCTIONS
    screen("During this game, you will be playing against the CPU.", 2, 3)

    screen("The two of you will each randomly choose one of three choices...", 2, 3)

    delay(2)

    def option(pick):
        print(f'{pick}\n')
        delay(1)

    options = [option(pick) for pick in ['Rock = R', 'Paper = P', 'Scissors = S']]
    delay(2)
    clear()

    # BEST 2 OUT OF 3 MESSAGE
    screen("Best 2 out of 3 WINS!!!", 2, 3)

    # WAITING SCREEN
    screen("LOADING...", 0, 10)
    clear

    # PREP SCREEN
    screen("GET READY!!!", 0, 5)
    
#intro()


# THE GAME FUNCTION
def rps_game():
    # PLAYER'S POINTS
    p1_points = 0
    cpu_points = 0

    winner = False
    while winner != True:
        
        # SCOREBOARD
        def score():
            print("Score:\n")
            print(f'{P1}: {str(p1_points)}')
            print(f'{CPU}: {str(cpu_points)}')
            delay(3)
            clear()

        # ROCK, PAPER, SCISSORS COUNT OFF
        def cadence(rps):
            clear()
            print(f'{rps}')
            delay(.5)

        count_off = [cadence(sign) for sign in ['Rock...', 'Paper...', 'Scissors...', 'SHOOT!!!']]
        delay(1) 
        clear()

        # CPU'S CHOICE
        cpu_choices = ["R", "P", "S"]
        cpu_choice = random.choice(cpu_choices)
        
        #PLAYER 1'S CHOICE
        print("Rock, Paper, or Scissors?")
        p1_choice = input().upper()
        
        # PLAYER'S CHOICES CONTAINER
        players_choices = f'{p1_choice} vs {cpu_choice}'

        clear()
        delay(2)

        # PLAYER'S WINNING OR A TIE PRESENTATION
        def who_won(choice, player):
            print(f'{choice}: {player} Wins!')
            delay(3)
            clear()

        def present_tie(choice):
            print(f'{choice}: It is a TIE!!')
            delay(3)
            clear()

        # HOW PLAYER'S WIN OR IF THERE IS A TIE GAME
        how_p1_wins = ["R vs S", "S vs P", "P vs R"]
        how_cpu_wins = ["S vs R", "P vs S", "R vs P"]
        tie_game = ["S vs S", "P vs P", "R vs R"]

        # HOW PLAYER 1 WINS
        for how_p1_won in how_p1_wins: 
            if players_choices == how_p1_won:
                who_won(how_p1_won, P1)
                p1_points += 1

        # # HOW CPU WINS
        for how_cpu_won in how_cpu_wins:
            if players_choices == how_cpu_won:
                who_won(how_cpu_won, CPU)
                cpu_points += 1


        # # WHEN A TIE OCCURS
        for tie in tie_game:
            if players_choices == tie:
                present_tie(tie)

        # p1_wins = [who_won(how_p1_won, P1, p1_points) for how_p1_won in how_p1_wins if players_choices == how_p1_won]
        # cpu_wins = [who_won(how_cpu_won, CPU, cpu_points) for how_cpu_won in how_cpu_wins if players_choices == how_cpu_won]
        # tied_up = [present_tie(tie) for tie in tie_game if players_choices == tie]

        # CHAMPION ANNOUNCEMENT
        def champion(champ):
            print(f'{champ} is the CHAMPION\n')
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()

        if p1_points == 2:
            winner = True
            champion(P1)
        elif cpu_points == 2:
            winner = True
            champion(CPU)

        # OVERALL SCORE
        score()

rps_game()
