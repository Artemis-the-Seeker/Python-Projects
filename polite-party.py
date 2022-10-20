import enum
import time
import random
import string
import sys


def typewriter(message):
    for char in message:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.1)
        time.sleep(.03)
        sys.stdout.flush()
    print('')


def print_slow(message, delay=1):
    typewriter(message)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print(f'Sorry, the answer "{response}" is invalid. Try again!')


def intro(host, victim):
    print_slow("\nThe full moon has risen.")
    print_slow(f"It is a beautiful night for a noble {host} feast, "
               f"but the host has just insulted your {victim}.")
    print_slow("The only hope of satisfaction is to return "
               "fire under the guise of proper politeness.")
    print_slow("You must deliver a perfectly plausible present of pique.\n")


def take_action(items):
    print_slow("Enter 1 to approach the host.\n"
               "Enter 2 to prowl the boutiques.\n"
               "What would you like to do?")
    response = valid_input("(Please enter 1 or 2).\n", ['1', '2'])
    if response == '1':
        gift_phase(items)
    elif response == '2':
        boutique(items)


def boutique(items):
    if 'lint' in items:
        print_slow("Many shops are closed at this time of night, "
                   "but you locate one stately bookstore.")
        print_slow("It takes careful deliberation, but soon "
                   "you select your weapon: a title so cold, "
                   "so incisive, you get a papercut.", 1)
        print_slow("Ouch!", 1)
        print_slow("It hurts - but not as badly as your foe will.")
        print_slow("It\'s time to return to the party.\n")
        items.remove('lint')
        items.append('book')
        gift_phase(items)
    else:
        print_slow("Even the bookstore has closed now, leaving "
                   "you a lone prowler in the night.", 1)
        print_slow("Get back to the party and take your revenge!\n", 1)
        take_action(items)


def gift_phase(items):
    print_slow(f"The {host} sneers at your approach.\n")
    print_slow("Enter 1 to formally offer a gift-insult.\n"
               "Enter 2 to come back better, stronger.\n"
               "What would you like to do?", 1)
    response = valid_input("(Please enter 1 or 2).\n", ['1', '2'])
    if response == '1':
        if 'lint' in items:
            print_slow("You smugly pull a bit of lint out of your "
                       f"pocket and hand it to the {host}.")
            print_slow("Rather than rage, you see their smirk shift to "
                       "a syrupy smile: the face of victory.")
            print_slow("\"Is this all you could afford? You poor dear.\"")
            print_slow("You are laughed out of the party.", 1)
            print_slow(f"Your {victim} will never be avenged.", 1)
            play_again()
        if 'book' in items:
            print_slow("You bow with a flourish and offer your "
                       "revenge: a beautifully wrapped copy of "
                       "\'How To Throw Rapturous Parties\'.")
            print_slow(f"The {host}\'s cheeks color with rage.")
            print_slow("Yes, you have savagely declared their "
                       "party non-rapturous.", 1)
            print_slow("Over your shoulder, someone titters.", 1)
            print_slow("You have won. Honor once more shines "
                       f"upon your beloved {victim} tonight.")
            play_again()
    elif response == '2':
        take_action(items)


def play_again():
    retry = valid_input("Would you like to play again? (y/n)\n", ['y', 'n'])
    if retry == 'n':
        print_slow("Thanks for playing! See you next time.")
        exit(0)


def play_game():
    while True:
        global host
        global victim
        host = random.choice(['Francorc', 'Elfola', 'Mathemagician'])
        victim = random.choice(['adopted parrot', 'wistful muse', 'ailing daisy'])
        items = ['lint']
        intro(host, victim)
        take_action(items)


def game():
    while True:
        play_game()
        play_again()


if __name__ == '__main__':
    game()
