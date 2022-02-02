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
def rpsGame():
    # CHOICES
    choices = ["R", "P", "S"]


    # PLAYER'S POINTS
    p1Points = 0
    cpuPoints = 0


    while p1Points or cpuPoints != 2:
        
        # SCOREBOARD
        def score():
            print("Score:\n")
            print(p1 + ": " + str(p1Points))
            print("CPU: " + str(cpuPoints))
            delay(3)
            clear()


        # ROCK, PAPER, SCISSORS FUNCTION
        rps('Rock...', 'Paper...', 'Scissors...', 'SHOOT!!!')  

        # PLAYER'S CHOICES
        p1Choice = ""
        cpuChoice = ""
        playersChoices = ""

        cpuChoice = random.choice(choices)
        
        print("Rock, Paper, or Scissors?")
        p1Choice = input().upper()
        

        playersChoices = p1Choice + " vs " + cpuChoice

        clear()
        delay(2)
        

        # PLAYER'S WINNING PRESENTATION
        p1wins = playersChoices + ": " + p1 + " Wins!"
        cpuWins = playersChoices + ": CPU Wins!"
        tieGame = playersChoices + ": It's a TIE!!"


        #HOW PLAYER'S WIN OR IF THERE IS A TIE
        howP1wins = ["R vs S", "S vs P", "P vs R"]
        howCpuWins = ["S vs R", "P vs S", "R vs P"]
        ifTie = ["S vs S", "P vs P", "R vs R"]

        # HOW PLAYER 1 WINS
        for wP1 in howP1wins: 
            if playersChoices == wP1:
                print(p1wins)
                p1Points += 1
                delay(3)
                clear()
        
        # HOW CPU WINS
        for wCpu in howCpuWins:
            if playersChoices == wCpu:
                print(cpuWins)
                cpuPoints += 1
                delay(3)
                clear()
            
        # WHEN A TIE OCCURS
        for aTie in ifTie:
            if playersChoices == aTie:
                print(tieGame)
                delay(3)
                clear()


        # CHAMPION ANNOUNCEMENT
        if p1Points == 2:
            print(p1 + " is the CHAMPION\n")
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()
            break
        elif cpuPoints == 2:
            print("CPU is the CHAMPION\n")
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()
            break


        # OVERALL SCORE
        score()

rpsGame()
