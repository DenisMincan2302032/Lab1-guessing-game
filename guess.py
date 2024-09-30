import random
#welcoming message
print("Hello and welcome to my guessing game")
#setting up variables
#number generation
generator = random.randint(1,100)
userguess = None
attempts = 0
#while loop setup
while userguess != generator and attempts<10:
    #attempts setup, only gives 10 attempts
    attempts = attempts + 1
    #user inputs
    userguess = int(input("Please guess the random number from 1-100:"))
    attempts = attempts + 1
    #guessing game logic, will stop at 10 attempts
    if attempts == 10:
        print("Ran out of guesses")
    if userguess < generator:
        print("Too low")
    if userguess > generator:
        print("Too high")
    if userguess == generator:
        print("Correct")
    





