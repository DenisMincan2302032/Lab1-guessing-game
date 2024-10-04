import random
#setting up variables
#number generation
def play_single_round():
    attempts = 0 
    generator = random.randint(1,100)
    userguess = None
    global max_attempts
    max_attempts = 10
    while userguess != generator and attempts<10:
    #attempts setup, only gives 10 attempts
        print("You will have 10 attempts to guess the correct number")
        attempts = attempts + 1
        max_attempts = max_attempts - 1
        #erorr handling for invalid values, will raise an error and return
        #to start of loop
        try:
            userguess = int(input())
        except ValueError:
            print("That's not a valid input. Enter a number.")
            attempts = attempts - 1
            max_attempts = max_attempts + 1
            continue      
    #guessing game logic, will stop at 10 attempts
        if attempts == 10:
            print("Ran out of guesses")
            print("The Correct Number is", generator)
        if userguess < generator:
            print("Too low")
            print("You have", max_attempts, "attempts left")
        if userguess > generator:
            print("Too high")
            print("You have", max_attempts, "attempts left")
        if userguess == generator:
            print("Correct")
            print("It took you", attempts, "attempts to guess correctly")

def play_game():
    #variable setup for loop
    #total rounds set to 4 to only allow 3 rounds
    #total score setup, addition of max_attempts for score
    total_rounds = 4
    total_score = 0
    for x in range(total_rounds):
        if x == 0:
            print("Welcome to the guessing game.")
            print("You will have 3 rounds of this game to guess the magic number, which is from 1-100.")
        if x == 1:
            print("Welcome to round 1.")
            play_single_round()
            total_score = max_attempts + total_score
            print("Your total score is", total_score)
        if x == 2:
            print("Welcome to round 2.")
            play_single_round()
            total_score = max_attempts + total_score
            print("Your total score is", total_score)
        if x == 3:
            print("Welcome to round 3.")
            play_single_round()
            print("Game over. No more rounds")
            total_score = max_attempts + total_score
            total_score = total_score / 3
            print("Your total score is", total_score)
            if total_score <= 7:
                print("Excellent guessing skills")
            if 7 <= total_score <= 9:
                print("Good job!")
            else:
                print("Better luck next time")






if __name__ == "__main__":
    play_game()

    





