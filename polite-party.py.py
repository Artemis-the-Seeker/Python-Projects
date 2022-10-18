import time
import random
from sys import exit


def print_slow(message, length):
    print(message)
    time.sleep(length)


def valid_input(prompt, option1, option2):
    while True:
        global response
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_slow("(Please enter 1 or 2).\n", 1)
    return response


def intro(host, victim):
    print_slow("\nThe full moon has risen.", 2)
    print_slow(f"It is a beautiful night for a noble {host} feast, "
               f"but the host has just insulted your {victim}.", 2)
    print_slow("The only hope of satisfaction is to return "
               "fire under the guise of proper politeness.", 2)
    print_slow("You must deliver a perfectly plausible present of pique.\n", 2)


def take_action(items):
    valid_input("Enter 1 to approach the host.\n"
                "Enter 2 to prowl the boutiques.\n"
                "What would you like to do?\n"
                "(Please enter 1 or 2).\n", '1', '2')
    if response == '1':
        gift_phase(items)
    elif response == '2':
        boutique(items)


def boutique(items):
    if 'lint' in items:
        print_slow("Many shops are closed at this time of night, "
                   "but you locate one stately bookstore.", 2)
        print_slow("It takes careful deliberation, but soon "
                   "you select your weapon: a title so cold, "
                   "so incisive, you get a papercut.", 1)
        print_slow("Ouch!", 1)
        print_slow("It hurts - but not as badly as your foe will.", 2)
        print_slow("It\'s time to return to the party.\n", 2)
        items.remove('lint')
        items.append('book')
        gift_phase(items)
    else:
        print_slow("Even the bookstore has closed now, leaving "
                   "you a lone prowler in the night.", 1)
        print_slow("Get back to the party and take your revenge!", 1)
        take_action(items)


def gift_phase(items):
    print_slow(f"The {host} sneers at your approach.\n", 2)
    print_slow("Enter 1 to formally offer a gift-insult.\n"
               "Enter 2 to come back better, stronger.\n"
               "What would you like to do?", 1)
    valid_input("(Please enter 1 or 2).\n", '1', '2')
    if response == '1':
        if 'lint' in items:
            print_slow("You smugly pull a bit of lint out of your "
                       f"pocket and hand it to the {host}.", 2)
            print_slow("Rather than rage, you see their smirk shift to "
                       "a syrupy smile: the face of victory.", 2)
            print_slow("\"Is this all you could afford? You poor dear.\"", 2)
            print_slow("You are laughed out of the party.", 1)
            print_slow(f"Your {victim} will never be avenged.", 1)
            play_again()
        if 'book' in items:
            print_slow("You bow with a flourish and offer your "
                       "revenge: a beautifully wrapped copy of "
                       "\'How To Throw Rapturous Parties\'.", 2)
            print_slow(f"The {host}\'s cheeks color with rage.", 2)
            print_slow("Yes, you have savagely declared their "
                       "party non-rapturous.", 1)
            print_slow("Over your shoulder, someone titters.", 1)
            print_slow("You have won. Honor once more shines "
                       f"upon your beloved {victim} tonight.", 2)
            play_again()
    elif response == '2':
        take_action(items)


def play_again():
    retry = valid_input("Would you like to play again? (y/n)\n", 'y', 'n')
    if retry == 'y':
        play_game()
    elif retry == 'n':
        print_slow("Thanks for playing! See you next time.", 2)
        exit()


def play_game():
    global host
    global victim
    host = random.choice(['Francorc', 'Elfola', 'Mathemagician'])
    victim = random.choice(['adopted parrot', 'wistful muse', 'ailing daisy'])
    items = ['lint']
    intro(host, victim)
    take_action(items)


play_game()
