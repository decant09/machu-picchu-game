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
        print("Bye")
        # use a quit()
    else:
        error()


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


def error():
    print("Please enter a valid option")
