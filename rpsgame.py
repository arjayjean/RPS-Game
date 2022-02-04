import random
import os
import time

# DELAY TIME
def delay(x):
    time.sleep(x)


# CLEAR CONSOLE
def clear(): 
    os.system("clear")


# PLAYER'S NAME CONTAINER
p1 = ""


# GAME INTRO
def intro():
    clear()
    delay(1)
    print("Welcome to Rock, Paper, Scissors!")
    delay(3)
    clear()
    delay(2)


    # PLAYER 1
    global p1 
    p1 = input("What is your name?: ")


    clear()
    delay(2)

    # GREETINGS
    print("Nice to meet you " + p1 + "!")
    delay(3)
    clear()


    # INSTRUCTIONS
    def instruction(x):
        delay(2)
        print(x)
        delay(4)
        clear()

    instruction("During this game, you will be playing against the CPU.")

    instruction("The two of you will each randomly choose one of three choices...")

    delay(2)

    def picks(*options):
        for pick in options:
            print(f'{pick}\n')
            delay(1)

    picks('Rock = R', 'Paper = P', 'Scissors = S')

    delay(2)
    clear()

    delay(2)
    print("Best 2 out of 3 WINS!!!")
    delay(3)
    clear()


    # WAITING SCREEN
    print("LOADING...")
    delay(10)
    clear()


    # PREP SCREEN
    print("GET READY!!!")
    delay(5)
    clear()

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
            print(p1 + ": " + str(p1_points))
            print("CPU: " + str(cpu_points))
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
        

        players_choices = p1_choice + " vs " + cpu_choice

        clear()
        delay(2)
        

        # PLAYER'S WINNING PRESENTATION
        p1_wins = players_choices + ": " + p1 + " Wins!"
        cpu_wins = players_choices + ": CPU Wins!"
        tie_game = players_choices + ": It's a TIE!!"


        #HOW PLAYER'S WIN OR IF THERE IS A TIE
        how_p1_wins = ["R vs S", "S vs P", "P vs R"]
        how_cpu_wins = ["S vs R", "P vs S", "R vs P"]
        if_tie = ["S vs S", "P vs P", "R vs R"]

        # HOW PLAYER 1 WINS
        for w_p1 in how_p1_wins: 
            if players_choices == w_p1:
                print(p1_wins)
                p1_points += 1
                delay(3)
                clear()
        
        # HOW CPU WINS
        for w_cpu in how_cpu_wins:
            if players_choices == w_cpu:
                print(cpu_wins)
                cpu_points += 1
                delay(3)
                clear()
            
        # WHEN A TIE OCCURS
        
        for a_tie in if_tie:
            if players_choices == a_tie:
                print(tie_game)
                delay(3)
                clear()


        # CHAMPION ANNOUNCEMENT
        if p1_points == 2:
            print(p1 + " is the CHAMPION\n")
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()
            break
        elif cpu_points == 2:
            print("CPU is the CHAMPION\n")
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()
            break


        # OVERALL SCORE
        score()

rps_game()
