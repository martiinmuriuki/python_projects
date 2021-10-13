import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess > random_number:
            print(f"guess again! {guess} is too high!!")
        elif guess < random_number:
            print(f"the guess again! {guess} is too low!!")


    print(f"wow, congrats!! {random_number} is correct")


def computer_guess(x):
    low = 1 
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low=high
        feedback = input(f"Is {guess} too high (h), too low low (l), correct(c)").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1 
        
    print(f"wow! the computer has guessed your number , {guess}, correctly")

guess(10)
computer_guess(1000)