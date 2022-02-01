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
howP1wins = ["S vs x", "P vs r", "R vs s"]


# HOW PLAYER 1 WINS
for p in howP1wins:
    print(p)
    
