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
    print(f"{username}, you have just met Miguel your guide. He speaks some English, more than you do Spanish.") 
    print("He seems friendly, knowledgeable and can trace his ancestry to the lost Incan civilization.")
    option = input("Would you like to continue on your adventure with Miguel? Y or N:\n>>> ").lower().strip()
    if option == 'y':
        print(f"Great {username}!")
        duration()
    elif option == 'n':
        print(f"Okay {username}. Have a great day!")
        # use a quit()
    else:
        error()

def duration():
    print("Miguel explains to you that you can complete the hike in either 3 or 5 days.")
    option = int(input("How many days would you prfer to spend hiking? 3 or 5:\n>>> "))
    if option == 3:
        print(f"Wow {username}, you must be up for the challenge! Hiking to an altitude of 2430m in 3 days is no joke!")
        three_days()
    elif option == 5:
        print(f"You're taking a more relaxed approcah {username} with opting for 5 days! You are on holiday afterall!")
        five_days()
        # use a quit()
    else:
        error()


def three_days():
    print("potion")



def five_days():
    print("berries")


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