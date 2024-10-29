10/29/2024

# Oct 29, 2024

# The Problem Number and Description
#Program's function is suppose to place a random number for the user to estimate. 
#If the answer is wrong then the code loops until the user guesses correctly.

import random
num = random.randrange (1, 12)
guess = int(input("Enter an integer from 1 to 12: "))
if guess < num:
        print("Aw dang guess is low")
        guess = int(input("Enter an integer from 1 to 12: "))
elif guess > num:
    print("Haha No! Guess is high")
    guess = int(input("Enter an integer from 1 to 12: "))
    print ("You guessed it right! Bye!")

Revisons made:
Too many if statments confused the code. With the following corrections made the code now loops 
until the correct number is choosen.

#Flowchart
#https://drive.google.com/file/d/1FrVHObccMs5HFUgSfuSSeS7fRazzLCWv/view?usp=drive_link
