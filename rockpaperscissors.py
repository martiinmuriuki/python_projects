import random

def play():
    user = input("what is your choice?'r' for rock, 'p' for paper 's' for scissors: ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "tie"

    #p>r r>s s>p
    if winner(user, computer):
        return "you won!"

    return "you lost!"
def winner(player, opponent):
    # return true if player wins
    if (player=='r' and opponent=='s') or (player=='p'and opponent=='r') or (player=='s' and opponent=='p'):
        return True

print(play())