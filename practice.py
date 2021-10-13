import random

def guess (x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}? "))
        if guess > random_number:
            print("try again, number to high")
        elif guess < random_number:
            print("try again, number to low")
    print(f"wow, its correct {random_number}")

guess(10)