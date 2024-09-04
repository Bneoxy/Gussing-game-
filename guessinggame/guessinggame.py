from random import *
from random import randint
from datetime import *
import sys
def main():
    print(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number."
    )
    chance = is_valid()
    random_number = randint(1,100)
    user_guess(random_number=random_number,chance=chance)
    while True:
        random_number = randint(1,100)
        try:
            playagain = str(input("Do you wana waste your time again(y/n): "))
        except:
            sys.exit("Fuck off")
        if playagain == "y":
            chance = is_valid()
            user_guess(random_number=random_number,chance=chance)
        else:
            sys.exit("Fuck off")

    
def is_valid():
    while True:
        ask_def = input(""""
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
                            
Enter your choice: """)
        if ask_def == "1":
            chance = 10
            return chance
        elif ask_def == "2":
            chance = 5
            return chance
        elif ask_def == "3":
            chance = 3
            return chance
        else:
            print("You have to enter a valid number")
            continue
def user_guess(random_number,chance):
    time_pattern = "%H:%M:%S"
    starting_time = datetime.now()
    total = 0
    while True:
        if int(total) == int(chance):
            print("Your chance of attempt is over")
            break
        try:
            userguess = int(input("Whats your guess: "))
        except ValueError:
            print("Enter number")
            continue
        if int(userguess) > int(random_number):
            print(f"Incorrect! The number is less than {userguess}")
            total += 1
            continue
        elif int(userguess) < int(random_number):
            print(f"Incorrect! The number is more than {userguess}")
            total += 1
            continue
        else:
            finish_timer = datetime.now()
            formatted_starttime = starting_time.strftime(time_pattern)
            formatted_finishtime = finish_timer.strftime(time_pattern)
            parsed_starttime = datetime.strptime(formatted_starttime, time_pattern)
            parsed_finishtime = datetime.strptime(formatted_finishtime, time_pattern)
            wastedtime = parsed_finishtime - parsed_starttime
            print(f"Congratulations! You guessed the correct number in {total} attempts and wasted your time: {wastedtime} .")
            break
 
if __name__ =="__main__":
    main()
    