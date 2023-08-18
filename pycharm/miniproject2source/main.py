import random

user_wins = 0
computer_wins = 0
draw_wins = 0

options =["rock", "paper", "scissors"]
while True:
    user_input = input("Rock paper scissors, or press q to quit").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    computer_pick = options[random_number]
    print("computer picked :", computer_pick,".")

    if user_input == "rock" and computer_pick == "scissors" or user_input == "paper" and computer_pick == "rock" or user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("Its a draw!")
        draw_wins += 1
    else:
        print("you lost!")
        computer_wins += 1

print("Good game! you won", user_wins, "times. Computer won", computer_wins, "times. You drew the game", draw_wins, "times.")
