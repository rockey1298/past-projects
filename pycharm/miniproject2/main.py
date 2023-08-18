import random

random_number = random.randint(1, 3)
computer_roll = int


def printing(random_number, user_id):
    print("random number :", random_number, "user id: ", user_id)


def roll():
    user_roll = input("r , p , or s")
    user_id = int
    if user_roll == "r":
        user_id = 1
    elif user_roll == "p":
        user_id = 2
    else:
        user_id = 3
    if user_id == computer_roll:
        print("draw!")
    if user_id == 1 and random_number == 2 or user_id == 2 and random_number == 3 or user_id == 3 and random_number == 1:
        print("you lost!")
    else:
        print("you won!")
    return user_id, user_roll


def start():
    while True:
        while True:
            u = input(" r p s ")
            if u != "r" or "p" or "s":
                print("try again")
            else:
                break
            if user_roll == "r":
                user_id = 1
            elif user_roll == "p":
                user_id = 2
            else:
                user_id = 3
            if user_id == computer_roll:
                print("draw!")
            if user_id == 1 and random_number == 2 or user_id == 2 and random_number == 3 or user_id == 3 and random_number == 1:
                print("you lost!")
            else:
                print("you won!")


printing(random_number, roll())
start()


