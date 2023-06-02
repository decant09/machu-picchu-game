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
    print("Welcome to Machu Picchu, an adventure based game where you hike to the ancient and magical summit of Machu Picchu.")
    print("Your story begins as you are travelling through South America and decide to visit the iconic ruined city of the Incas.")
    print("Your guide Miguel will accompany you on your Incan journey.\n")
    

def miguel():
    print("You have just met Miguel your guide. He speaks some English, more than you do Spanish.") 
    print("He seems friendly, knowledgeable and can trace his ancestry to the lost Incan civilization.\n")
    option = input("Would you like to continue on your adventure with Miguel? Y or N:\n>>> ").lower().strip()
    if option == 'y':
        print(f"Great {username}!\n")
        duration()
    elif option == 'n':
        print(f"Okay {username}. Have a great day!")
        # use a quit()
    else:
        error()
        miguel()


def duration():
    print("Miguel explains to you that you can complete the hike in either 3 or 5 days.")
    option = int(input("How many days would you prfer to spend hiking? 3 or 5:\n>>> "))
    if option == 3:
        print(f"Wow {username}, you must be up for the challenge! Hiking to an altitude of 2430m in 3 days is no joke!\n")
        three_days()
    elif option == 5:
        print(f"You're taking a more relaxed approcah {username} with opting for 5 days! You are on holiday afterall!\n")
        five_days()
        # use a quit()
    else:
        error()
        duration()


def three_days():
    print("The hike is going well but Miguel thinks that you won't make the summit in 3 days.")
    print("He suggests a shortcut which involves diving into a river from on top of a bridge.")
    option = input("Do you take Miguel's advice and dive into the river? Y or N:\n>>> ").lower().strip()
    if option == 'y':
        print(f"Oh no {username}, that river was treacherous!")
        # game over function
    elif option == 'n':
        print(f"Good choice {username}!")
        print("Turns out that river was pretty shallow and rapid!")
        print("What was Miguel thinking?!\n")
        # potion()        
    else:
        error()
        three_days()


def five_days():
    print("So far the hike is beautiful!")
    print(f"But wait {username}, you've just run out of insect repellant")
    print("and the mosquitos here are vicious!")
    print("Miguel suggests a natural repellant made by smearing the orange berries")
    print("picked from a nearby native tree")
    option = input("Would you like to use the berry repellant? Y or N:\n>>> ").lower().strip()
    if option == 'y':
        print(f"Awesome! It works! Turns out the mosquitos don't like those berries!")
        # new function
    elif option == 'n':
        print(f"Oh no {username}! The mosquitos here carry malaria!")
        print("You get bitten and fall into a frantic fever.")
        print("You need urgent medical attention!")
        # game over function
    else:
        error()
        five_days()


def error():
    print("Please enter a valid option")


intro()


while True:
    try:
        username = str(input("Please enter your name:\n>>> ")).capitalize().strip()
        if len(username) <= 2 or not username.isalpha():
            raise ValueError("Username must not have any spaces, be at least 3 characters long, and only contain letters.")
            continue
    except ValueError as e:
        print(f"Invalid Entry: {e}")
    else:
        print(f"Welcome {username}! Let your journey begin!\n")
        miguel()
        break