def start():
    # Introduction to the game
    print("Adventure Game")
    print("You find yourself in front of a strange cave.")
    print("Do you want to enter the cave? (yes/no)")

    # To get user input
    user = input().lower()

    if user == "yes":
        enter()
    elif user == "no":
        
        print("You have decided not to enter the cave. As you turn away, a magical force pulls you in, The adventure begins.")
        inside()
    else:
        
        invalid()

def enter():
    # Decision after entering the cave.
    print("As you enter the cave, you can see two paths.")
    print("Do you want to take the left path or the right path?")

   
    user = input().lower()

    if user == "left":
        left()
    elif user == "right":
        right()
    else:
        
        invalid()

def inside():
    # Decision inside the cave with three doors
    print("Inside the cave, you find a dimly lit chamber with three doors: red, blue, and green.")
    print("Which door do you want to enter?")

    
    user = input().lower()

    if user == "red":
        red()
    elif user == "blue":
        blue()
    elif user == "green":
        green()
    else:
        
        invalid()

def left():
    # The player finds a chest full of treasure when the player goes left
    print("You find a chest full of treasure! Congratulations, you win!")
    play()

def right():
    # when the player goes right path , player confronts with a giant spider.
    print("A giant spider blocks your way.")
    print("Do you wish to fight the spider or try to run away?")

   
    user = input().lower()

    if user == "fight":
       
        print("You have defeated the spider and continue on your journey.")
        play()
    elif user == "run":
        
        print("You try to run away but the spider catches up and bites you, Game over.")
    else:
       
        invalid()

def red():
    # When the player enters the  red door, the player faces a choice involving mystical flames
    print("Behind the red door, you find a room filled with mystical flames.")
    print("Do you want to touch the flames or search for another exit?")

    
    user = input().lower()

    if user == "touch":
       
        print("The flames react to your touch and reveal a hidden passage. You continue your adventure.")
        play()
    elif user == "search":
       
        print("You find a secret door. As you open it, a dragon emerges! Game over.")
    else:
       
        invalid()

def blue():
    # When player enters the blue door, the player faces a choice involving a magical pool
    print("Behind the blue door, you find a room with a magical pool.")
    print("Do you wish to drink from the pool or continue exploring?")

  
    user = input().lower()

    if user == "drink":
     
        print("The magical water grants you enhanced abilities. You continue your adventure.")
        play()
    elif user == "explore":
       
        print("You find a hidden tunnel. As you crawl through, you discover a treasure room. Congratulations, you win!")
    else:
        
        invalid()

def green():
    # When the playerenters the green door, the player faces a choice in a garden with strange plants
    print("Behind the green door, you find a garden filled with strange plants.")
    print("Do you want to pick a mysterious flower or leave the garden?")

   
    user = input().lower()

    if user == "pick":
       
        print("The flower grants you a special power. You continue your adventure.")
        play()
    elif user == "leave":
       
        print("As you try to leave, the plants come alive! Game over.")
    else:
       
        invalid()

def play():
    # To ask the player if they want to play again
    print("Do you want to play again? (yes/no)")

    user = input().lower()

    if user == "yes":
      
        start()
    elif user == "no":
       
        print("Thanks for playing.")
    else:
        
        invalid()

def invalid():
    # Inform the player about invalid input
    print("Invalid input. Please enter the given options.")

# To start the game
start()
