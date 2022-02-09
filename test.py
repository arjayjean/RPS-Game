import os
import time
import random

# DELAY TIME
def delay(x):
    time.sleep(x)


# CLEAR CONSOLE
def clear(): 
    os.system("clear")

clear()

#-------------------------------------------------------

# PLAYER'S POINTS
p1_points = 0
cpu_points = 0

P1 = "Arjay"
CPU = 'CPU'


# SCOREBOARD
def score():
    print("Score:\n")
    print(f'{P1}: {str(p1_points)}')
    print(f'{CPU}: {str(cpu_points)}')
    delay(3)
    clear()


# CPU'S CHOICE
cpu_choices = ["S", "R", "P"]
cpu_choice = random.choice(cpu_choices)


#PLAYER 1'S CHOICE
print("Rock, Paper, or Scissors?")
p1_choice = input().upper()


# PLAYER'S CHOICES CONTAINER
players_choices = f'{p1_choice} vs {cpu_choice}'

clear()
delay(2)


def who_won(choice, winner, point):
    print(f'{choice}: {winner} Wins!')
    point += 1
    delay(3)
    clear()

def present_tie(tie):
    print(f'{tie}: It is a TIE!!')
    delay(3)
    clear()


how_p1_wins = ["R vs S", "S vs P", "P vs R"]
how_cpu_wins = ["S vs R", "P vs S", "R vs P"]
tie_game = ["S vs S", "P vs P", "R vs R"]

# HOW PLAYER 1 WINS
# for how_p1_won in how_p1_wins: 
#     if players_choices == how_p1_won:
#         who_won(P1)
#         p1_points += 1
#         delay(3)
#         clear()

# HOW CPU WINS
p1_w = [who_won(how_p1_won, P1, p1_points) for how_p1_won in how_p1_wins if players_choices == how_p1_won]
cpu_w = [who_won(how_cpu_won, CPU, cpu_points) for how_cpu_won in how_cpu_wins if players_choices == how_cpu_won]
tied_up = [present_tie(tie) for tie in tie_game if players_choices == tie]

# for how_cpu_won in how_cpu_wins:
#     if players_choices == how_cpu_won:
#         who_won(CPU)
#         cpu_points += 1
#         delay(3)
#         clear()
    
# WHEN A TIE OCCURS

# for tie in tie_game:
#     if players_choices == tie:
#         present_tie()
#         delay(3)
#         clear()
score()