import random

# attempts starts at 0
attempts_list = []
def whats_my_score():
    if len(attempts_list) <= 0:
        print("The high score is yours for the taking")
# start with some questions
def start_this_show():
    random_number = int(random.randint(1, 100))
    print("Welcome to my squid game")
    player_name = input("What is your name? ")
    wanna_play = input("Hi, {}, would you like to play with me? Yes/No ".format(player_name))
    attempts = 0
    whats_my_score()
    # start of the game
    while wanna_play == "yes":
        try:
            # picking a number
            your_guess = input("Pick a number between 1 and 100 ")
            if int(your_guess) < 1 or int(your_guess) > 100:
                # pick out of range
                raise ValueError("pick a number in the correct range")
            # first guess right answer
            if int(your_guess) == random_number:
                print("Nice job you got it!")
                attempts += 1
                # pull attempts
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                # keep going
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                whats_my_score()
                random_number = int(random.randint(1, 100))
                # choose no to stop playing
                if play_again.lower() == "no":
                    print("Okay bye")
                    break
                # number is higher
            elif int(your_guess) < random_number:
                print("Number higher")
                attempts += 1
                # number is lower
            elif int(your_guess) > random_number:
                print("Number is lower")
                attempts += 1
                # error msg
        except ValueError:
            print("Well that was not right")
    else:
        print("Okay bye")


start_this_show()
