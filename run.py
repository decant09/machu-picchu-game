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
    print("Welcome to Machu Picchu, an adventure based game where you hike to the ancient and magical peak of Machu Picchu.")
    print("Your guide Miguel will accompany you on your Incan journey.\n")


intro()


while True:
    try:
        username = str(input("Please enter your name: \n")).capitalize().strip()
        if len(username) <= 2 or not username.isalpha():
            raise ValueError("Username must not have any spaces, be at least 3 characters long, and only contain letters")
            continue
    except ValueError as e:
        print(f"Invalid Entry: {e}")
    else:
        print(f"Welcome {username}!\n")
        # build next funtion()
        break