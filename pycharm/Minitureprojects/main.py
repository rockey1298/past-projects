import random


userint = int
number_s = False
while number_s == False:
    user_num_choice = input("What would you like the maximum range to be of the number you'd like to guess?")
    if user_num_choice.isdigit():
        userint = int(user_num_choice)
        if userint > 0:
            usc = userint
            number_s = True
        else:
            print("Number needs to be greater than 0")
    else:
        print("Please enter a number ")

random_number = random.randint(0, usc)
guesses = 0
user_got = False
while user_got == False:
    guesses += 1
    useri = input("Guess a number between 0 and " + user_num_choice)
    userint = int(useri)
    if userint == random_number:
        print("Wow! Good job! You got it! You took ", guesses, " guesses to figure it out!")
        user_got = True
    if userint > random_number:
        print("You guessed too high, try again ")

    if userint < random_number:
        print("You guessed too low, try again ")
