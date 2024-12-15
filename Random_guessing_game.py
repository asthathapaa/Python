import random

def num_guessing_game():
    print("This is Astha's Number guessing game!")
    num = random.randint(1,15)
    attempt = 0

    while True:
        try:
            guess = int(input("No betn 1 to 15:"))
            attempt +=1
            if guess < num:
                print("To low ! Try again")
            elif guess >num:
                print("To high ! Once again")
            else:
                print("Congrats!!! Nice guess count:",attempt)
                break
        except ValueError:
            print("please enter valid number")

num_guessing_game()
