art = """
  ^    ^    ^    ^    ^       
 /M\  /A\  /C\  /H\  /U\      
<___><___><___><___><___>     
  ^    ^    ^    ^    ^    ^  
 /P\  /I\  /C\  /C\  /H\  /U\ 
<___><___><___><___><___><___>
                              
"""                              
username = ""


def intro():
    print(art)
    print("Welcome to Machu Picchu, an adventure based game where you hike to the ancient")
    print("and magical summit of Machu Picchu.")
    print("Your story begins as you are travelling through South America and decide to")
    print("visit the iconic ruined city of the Incas.")
    print("Your guide Miguel will accompany you on your Incan journey.\n")
    

def miguel():
    print("You have just met Miguel your guide. He speaks some English, more than you")
    print("speak Spanish.") 
    print("He seems friendly, knowledgeable and can trace his ancestry to the lost Incan")
    print("civilization.\n")
    option = input("Would you like to continue on your adventure with Miguel? Y or N:\n>>> ").lower().strip()
    if option == 'y':
        print(f"Great {username}!\n")
        duration()
    elif option == 'n':
        print(f"Okay {username}. Have a great day!")
        quit()
    else:
        error()
        miguel()


def duration():
    print("Miguel explains to you that you can complete the hike in either 3 or 5 days.")
    option = input("How many days would you prfer to spend hiking? 3, 5 or Q to quit:\n>>> ").lower().strip()
    if option == '3':
        print(f"Wow {username}, you must be up for the challenge! Hiking to an altitude")
        print("of 2430m in 3 days is no joke!\n")
        three_days()
    elif option == '5':
        print(f"You're taking a more relaxed approcah {username} with opting for 5 days!")
        print("You are on holiday afterall!\n")
        five_days()
    elif option == 'q':
        quit()
    else:
        error()
        duration()


def three_days():
    print("The hike is going well but Miguel thinks that you won't make the summit in")
    print("3 days.")
    print("He suggests a shortcut which involves diving into a river from on top of a")
    print("bridge.")
    option = input("Do you take Miguel's advice and dive into the river? Y, N or Q to quit:\n>>> ").lower().strip()
    if option == 'y':
        print(f"Oh no {username}, that river was treacherous!")
        # game over function with do you want to play again
    elif option == 'n':
        print(f"Good choice {username}!")
        print("Turns out that river was pretty shallow and rapid!")
        print("What was Miguel thinking?!\n")
        potion()
    elif option == 'q':
        quit()        
    else:
        error()
        three_days()


def five_days():
    print("So far the hike is beautiful!")
    print(f"But wait {username}, you've just run out of insect repellant")
    print("and the mosquitos here are vicious!")
    print("Miguel suggests a natural repellant made by smearing the orange berries")
    print("picked from a nearby native tree")
    option = input("Would you like to use the berry repellant? Y, N or Q to quit:\n>>> ").lower().strip()
    if option == 'y':
        print("Awesome! It works! Turns out the mosquitos don't like those berries!")
        waterfall()
    elif option == 'n':
        print(f"Oh no {username}! The mosquitos here carry malaria!")
        print("You get bitten and fall into a frantic fever.")
        print("You need urgent medical attention!")
        # game_over function with do you want to play again
    elif option == 'q':
        quit()
    else:
        error()
        five_days()


def potion():
    print("The hike starts to get a little challenging now as you make it")
    print("closer to the summit. You begin to feel the effects of the")
    print(f"altitude. {username}, maybe it wasn't such a great idea to")
    print("complete the hike in 3 days! To combat the sickness Miguel")
    print("conjures up a potion made by boiling some leaves he picked from")
    print("a bush. You take the potion but it doesn't appear to be working!")
    print("Maybe Miguel doesn't realise the severity of your condition?")
    option = input("Do you ask Miguel for some more potion? Y, N or Q to quit:\n>>> ").lower().strip()
    if option == 'y':
        print("You take another dose of potion despite Miguel's advice. You")
        print("start to become disorientated from the effects of the potion")
        print("You wander off into the jungle and never reach the summit!")
        # game_over() function with do you want to play again
    elif option == 'n':
        print(f"Good choice {username}! You wait a little longer and the")
        print("potion starts to work its magic. You start to feel much")
        print("better and continue on your journey.")
        # new function
    elif option == 'q':
        quit()
    else:
        error()
        potion()


def waterfall():
    print(f"{username} you're almost at the end of your hike and you haven't")
    print("captured and moments on camera to remember the trip by! There's")
    print("wonderful waterfall just up ahead. Seems like the perfect")
    print("opportunity to take a snap!")
    option = input("Do you ask Miguel to take your photo? Y, N or Q to quit:\n>>> ").lower().strip()
    if option == 'y':
        print("Miguel willingly obliges and agrees to take your photo. You get")
        print("as close to the waterfall as possible for the perfect snap. But")
        print("you fail to notice that the rocks that you are standing on are")
        print("extremely slippy. You lose your footing, fall into the water, get")
        print("washed away and you never reach the summit!")
        # game_over() function with do you want to play again
    elif option == 'n':
        print(f"You're right {username}, better live in the moment and fully")
        print("experience the hike. You soak up all the glory of the waterfall")
        print("for a moment before continuing on your journey")
        # new function
    elif option == 'q':
        quit()
    else:
        error()
        waterfall()



def error():
    print("Please enter a valid option")


intro()


while True:
    try:
        username = str(input("Please enter your name:\n>>> ")).capitalize().strip()
        if len(username) <= 2 or not username.isalpha():
            raise ValueError("Username must not have any spaces, be at least 3 characters long,\nand only contain letters.")
            continue
    except ValueError as e:
        print(f"Invalid Entry: {e}")
    else:
        print(f"Welcome {username}! Let your journey begin!\n")
        miguel()
        break