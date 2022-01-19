import random
import os
import time

# DELAY TIME
def delay(x):
    time.sleep(x)


# CLEAR CONSOLE
def clear(): 
    os.system("clear")


# RPS COUNTDOWN
def rps():
    clear()
    print("Rock...")
    delay(.5)
    print("Paper...")
    delay(.5)
    print("Scissors...")
    delay(.5)
    clear()
    print("SHOOT!!!")
    delay(1)
    clear()


# PLAYERS
cpu = "CPU"
p1 = ""

# PLAYER 1'S NAME CONTAINER
player1 = []


# GAME INTRO
def intro():
    clear()
    delay(1)
    print("Welcome to Rock, Paper, Scissors!")
    delay(3)
    clear()
    delay(2)


    # PLAYER 1
    p1 = input("What is your name?: ")
    player1.append(p1)

    clear()
    delay(2)

    # GREETINGS
    print("Nice to meet you " + p1 + "!")
    delay(3)
    clear()


    # INSTRUCTIONS
    delay(2)
    print("During this game, you will be playing against the " + cpu + ".")
    delay(4)
    clear()

    delay(2)
    print("The two of you will each randomly choose one of three choices...")
    delay(4)
    clear()

    delay(2)
    print("Rock = R\n")
    delay(1)
    print("Paper = P\n")
    delay(1)
    print("Scissors = S")
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
            print(player1[0] + ": " + str(p1Points))
            print(cpu + ": " + str(cpuPoints))
            delay(3)
            clear()


        # ROCK, PAPER, SCISSORS FUNCTION
        rps()


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
        p1wins = playersChoices + ": " + player1[0] + " Wins!"
        cpuWins = playersChoices + ": " + cpu + " Wins!"
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
            print(player1[0] + " is the CHAMPION\n")
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()
            break
        elif cpuPoints == 2:
            print(cpu + " is the CHAMPION\n")
            score()
            print("Thank you for playing! See you next time!")
            delay(3)
            clear()
            break

        score()

rpsGame()
