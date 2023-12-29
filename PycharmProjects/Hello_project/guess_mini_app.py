secret_number= 9
guess_counts=0
guess_limit=3
while guess_counts < guess_limit:
    guess= int(input('Guess the secret number you have maximum of 3 guessing times: '))
    guess_counts+= 1
    if guess == secret_number:
        print("you won")
        break
else:
    print("sorry you failed")

