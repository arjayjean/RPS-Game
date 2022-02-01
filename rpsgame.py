import random
import os
import time

# DELAY TIME
def delay(x):
    time.sleep(x)


# CLEAR CONSOLE
def clear(): 
    os.system("clear")


# RPS CADENCE
def rps(*cadence):
    for rps in cadence:
        clear()
        print(f'{rps}')
        delay(.5)


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
    print("GET READY!")
    delay(5)
    clear()

intro()


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
        delay(.5) 
        clear()

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
        

        # HOW TO WIN
        p1wins = playersChoices + ": " + p1 + " Wins!"
        cpuWins = playersChoices + ": CPU Wins!"
        tieGame = playersChoices + ": It's a TIE!!"


        # PLAYER 1 WINS
        if playersChoices == "R vs S":
            print(p1wins)
            p1Points += 1
            delay(3)
            clear()
        elif playersChoices == "S vs P":
            print(p1wins)
            p1Points += 1
            delay(3)
            clear()
        elif playersChoices == "P vs R":
            print(p1wins)
            p1Points += 1
            delay(3)
            clear()

        # CPU WINS
        elif playersChoices == "S vs R":
            print(cpuWins)
            cpuPoints += 1
            delay(3)
            clear()
        elif playersChoices == "P vs S":
            print(cpuWins)
            cpuPoints += 1
            delay(3)
            clear()
        elif playersChoices == "R vs P":
            print(cpuWins)
            cpuPoints += 1
            delay(3)
            clear()

        # WHEN A TIE OCCURS
        elif playersChoices == "S vs S":
            print(tieGame)
            delay(3)
            clear()
        elif playersChoices == "P vs P":
            print(tieGame)
            delay(3)
            clear()
        elif playersChoices == "R vs R":
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

        score()

rpsGame()
