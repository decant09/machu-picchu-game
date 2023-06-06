import os


art = """
  ^    ^    ^    ^    ^
 /M\\  /A\\  /C\\  /H\\  /U\\
<___><___><___><___><___>
  ^    ^    ^    ^    ^    ^
 /P\\  /I\\  /C\\  /C\\  /H\\  /U\\
<___><___><___><___><___><___>
"""


win = """
  ^    ^    ^       ^    ^    ^
 /Y\\  /O\\  /U\\     /W\\  /I\\  /N\\
<___><___><___>   <___><___><___>
"""


lose = """
  ^    ^    ^       ^    ^    ^    ^
 /Y\\  /O\\  /U\\     /L\\  /O\\  /S\\  /E\\
<___><___><___>   <___><___><___><___>
"""


username = ""


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def intro():
    print(art)
    print("Welcome to Machu Picchu, an adventure based game where " +
          "you hike to the ancient")
    print("and magical summit of Machu Picchu. Your adventure " +
          "begins as you are travelling")
    print("through South America and decide to visit the iconic " +
          "ruined city of the Incas.")
    print("Your guide Miguel will accompany you on your Incan journey.\n")
    if username == "":
        pass
    else:
        miguel()


def miguel():
    print("You meet Miguel in Cuzco, the capital of the Incan empire. " +
          "He speaks English")
    print("fairly well, more than you speak Spanish. He seems friendly, "
          "knowledgeable")
    print("and can trace his ancestry to the lost Incan civilization.\n")
    option = ''
    while option != 'y' and option != 'n':
        try:
            option = input("Would you like to continue on your adventure " +
                           "with Miguel? Y or N:\n>>> ").lower().strip()
            if option == 'y':
                clear_terminal()
                print(f"Great {username}! Let your adventure with Miguel " +
                      "begin!\n")
                duration()
            elif option == 'n':
                clear_terminal()
                print(f"Okay {username}, no problem. Have a great day!")
                quit()
            else:
                raise ValueError("Please enter Y or N.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def duration():
    print("Miguel explains to you that you can complete the hike in " +
          "either 3 or 5 days.\n")
    option = ''
    while option != '3' and option != '5' and option != 'q':
        try:
            option = input("How many days would you prfer to spend hiking? " +
                           "3, 5 or Q to quit:\n>>> ").lower().strip()
            if option == '3':
                clear_terminal()
                print(f"Wow {username}, you must be up for the challenge! " +
                      "Hiking to an altitude of 2430m")
                print("in 3 days is no joke!\n")
                three_days()
            elif option == '5':
                clear_terminal()
                print(f"You're taking a more relaxed approcah {username} " +
                      "with opting for 5 days! You")
                print("are on holiday afterall!\n")
                five_days()
            elif option == 'q':
                quit()
            else:
                raise ValueError("Please enter 3, 5 or Q to quit.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def three_days():
    print("The hike is going well but Miguel thinks that you won't make " +
          "the summit in 3")
    print("days. He suggests a shortcut which involves diving into a river " +
          "from on top of")
    print("a bridge.\n")
    option = ''
    while option != 'y' and option != 'n' and option != 'q':
        try:
            option = input("Do you take Miguel's advice and dive into the " +
                           "river? Y, N or Q to quit:\n>>> ").lower().strip()
            if option == 'y':
                clear_terminal()
                print(f"Oh no {username}, the river is treacherous! You get " +
                      "swept away in the rapids\n")
                print("clambering in vain to grab one of boulders " +
                      "protruding out of the river in order")
                print("to escape to safety!")
                game_over_lose()
            elif option == 'n':
                clear_terminal()
                print(f"Good choice {username}! Turns out that river was " +
                      "pretty rapid and shallow!")
                print("What was Miguel thinking?!\n")
                potion()
            elif option == 'q':
                quit()
            else:
                raise ValueError("Please enter Y, N or Q to quit.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def five_days():
    print("So far the hike is beautiful! You sure are glad you chose the " +
          "5 day option. But")
    print(f"wait {username}, you've just run out of insect repellant and " +
          "the mosquitos here")
    print("are vicious! Miguel suggests a natural repellant made by " +
          "smearing orange")
    print("berries, picked from a nearby native tree, over your skin.\n")
    option = ''
    while option != 'y' and option != 'n' and option != 'q':
        try:
            option = input("Would you like to use the berry repellant? " +
                           "Y, N or Q to quit:\n>>> ").lower().strip()
            if option == 'y':
                clear_terminal()
                print(f"Awesome {username}! It works! Turns out the " +
                      "mosquitos don't like those berries!\n")
                waterfall()
            elif option == 'n':
                clear_terminal()
                print(f"Oh no {username}! The mosquitos here carry malaria! " +
                      "You get bitten and fall")
                print("into a frantic fever. You need urgent medical " +
                      "attention!\n")
                game_over_lose()
            elif option == 'q':
                quit()
            else:
                raise ValueError("Please enter Y, N or Q to quit.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def potion():
    print("The hike starts to get a little challenging now as you " +
          "make it closer to the")
    print(f"summit. You begin to feel the effects of the altitude. " +
          "{username}, maybe")
    print("it wasn't such a great idea to complete the hike in 3 days! " +
          "To combat the")
    print("sickness Miguel conjures up a potion made by boiling some " +
          "leaves he picked from")
    print("a bush. You take the potion but it doesn't appear to be " +
          "working! Maybe Miguel")
    print("doesn't realise the severity of your condition?\n")
    option = ''
    while option != 'y' and option != 'n' and option != 'q':
        try:
            option = input("Do you ask Miguel for some more potion?" +
                           "Y, N or Q to quit:\n>>> ").lower().strip()
            if option == 'y':
                clear_terminal()
                print("You take another dose of potion despite Miguel's " +
                      "advice. You start to become")
                print("disorientated from its effects. You wander off into " +
                      "the jungle and never reach")
                print("the summit!\n")
                game_over_lose()
            elif option == 'n':
                clear_terminal()
                print(f"Good choice {username}! You wait a little longer " +
                      "and the potion starts to work")
                print("its magic. You start to feel much better and " +
                      "continue on your journey.\n")
                puzzle()
            elif option == 'q':
                quit()
            else:
                raise ValueError("Please enter Y, N or Q to quit.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def waterfall():
    print("You're almost at the end of your hike and you haven't captured " +
          "any moments on")
    print("camera to remember the trip by! There's a wonderful waterfall " +
          "just up ahead.")
    print("Seems like the perfect opportunity to take a snap!\n")
    option = ''
    while option != 'y' and option != 'n' and option != 'q':
        try:
            option = input("Do you ask Miguel to take your photo? " +
                           "Y, N or Q to quit:\n>>> ").lower().strip()
            if option == 'y':
                clear_terminal()
                print("Miguel willingly obliges and agrees to take your " +
                      "photo. You get as close to the")
                print("waterfall as possible for the perfect snap. But you " +
                      "fail to notice that the")
                print("rocks that you are standing on are extremely slippy. " +
                      "You lose your footing, fall")
                print("into the water, get washed away and you never reach " +
                      "the summit!\n")
                game_over_lose()
            elif option == 'n':
                clear_terminal()
                print(f"You're right {username}, better live in the moment " +
                      "and fully experience the")
                print("hike. You soak up all the glory of the waterfall for " +
                      "a moment before continuing")
                print("on your journey.\n")
                puzzle()
            elif option == 'q':
                quit()
            else:
                raise ValueError("Please enter Y, N or Q to quit.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def puzzle():
    print("Miguel tells you that you are about to reach the summit. " +
          "However, he explains")
    print("that there is a door that you need to pass through in order to " +
          "succeed. The door")
    print("requires a password in order to open it to reach the summit.\n")
    print("The password that is to be entered is 5 characters long, can " +
          "only contain")
    print("letters, and can not be a previous guess.")
    print("You will get 5 attempts to guess the password. Good luck!\n")
    print("Before you proceed to attempt the password, you notice " +
          "something written above")
    print("the door... \"The capital of the Incas\". Could this be a clue " +
          "to the password")
    print("required? You think to yourself, isn't that the place where I " +
          "started my")
    print("adventure with Miquel?\"\n")
    print("Enter Q to quit if you desire.")
    answer = "cuzco"
    attempts = 5
    words_guessed = []
    while attempts > 0:
        guess = input("\nPlease enter the password:\n>>> ").lower()
        if guess.isalpha() and len(guess) == 5 and guess not in words_guessed:
            if guess == answer:
                clear_terminal()
                game_over_win()
                break
            else:
                print("Sorry! That's not the correct password!\n")
                attempts -= 1
                print(f"Attempts remaining: {attempts}")
                words_guessed.append(guess)
                list = ', '.join(words_guessed)
                print(f"Passwords attempted so far: {list}")
                if attempts == 0:
                    clear_terminal()
                    print(f"No attempts remaining. The answer was {answer}!")
                    game_over_lose()
        elif guess == "q":
            quit()
        else:
            print("\nGuess must be 5 characters long, only contain " +
                  "letters and not guessed already.")


def game_over_win():
    print(win)
    print(f"\nCongratulations {username}! The door opens, you made " +
          "it to the summit!\n")
    option = ''
    while option != 'y' and option != 'n':
        try:
            option = input("Play again? Y or N:\n>>> ").lower()
            if option == 'y':
                clear_terminal()
                intro()
            elif option == 'n':
                clear_terminal()
                quit()
            else:
                raise ValueError("Please enter Y or N.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


def game_over_lose():
    print(lose)
    print(f"\nSorry {username}! You didn't reach the summit this time!\n")
    option = ''
    while option != 'y' and option != 'n':
        try:
            option = input("Play again? Y or N:\n>>> ").lower()
            if option == 'y':
                clear_terminal()
                intro()
            elif option == 'n':
                clear_terminal
                quit()
            else:
                raise ValueError("Please enter Y or N.\n")
        except ValueError as e:
            print(f"\nInvalid Entry: {e}")


intro()


while True:
    try:
        username = input("Please enter your name:\n>>> ").capitalize().strip()
        if len(username) <= 2 or not username.isalpha():
            raise ValueError("Username must not have any spaces, be at " +
                             "least 3 characters long,\nand only contain " +
                             "letters.\n")
            continue
    except ValueError as e:
        print(f"\nInvalid Entry: {e}")
    else:
        clear_terminal()
        print(f"Welcome {username}!\n")
        miguel()
        break
