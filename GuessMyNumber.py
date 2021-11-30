"""This program is made to guess the number
thought by the computer by the person who is
playing the game"""

#importing the random function
import random
#main function
def main():
    #generating a secret number for the computer
    secret_number = random.randint(1,99)
    print("I am thinking of a number between 1 and 99")
    #user enters the input
    user_guess = int(input("Enter your guess to know my secret number:"))
    while user_guess != secret_number:
        if user_guess < secret_number:
            print("Your guess is lower than my secret number !")
        else:
            print("Your guess is higher than my secret number !")
        print("")
        user_guess = int(input("Enter a new guess:"))
    print("Hurray !!! You did it !")
    print("The secret number is :",secret_number)

if __name__ == "__main__":
    main()