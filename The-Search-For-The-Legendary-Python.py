import time, sys

def main_room():
    global inventory, placed_ladder, inserted_key
    print("You find yourself in a dark room, you see four ways to go, a door on the left, a door on the right, a hole on the ceiling, and a trapdoor in the ground. What do you do? (Type 'help' if you need help)")
    choice = input().lower()
    
    if choice == "help":
        help()
    elif choice == "inventory":
        items()
    
    elif choice == "left":
        if "ladder" not in inventory and not placed_ladder:
            print("You go left and find a ladder, there is nothing else of interest, so you go back")
            inventory.append("ladder")
        else:
            print("You already went in there")
    
    elif choice == "right":
        right_room()

    elif choice == "ladder":
        if "ladder" in inventory and not placed_ladder:
            print("You placed the ladder underneath the hole in the ceiling")
            placed_ladder = True
            del inventory[inventory.index("ladder")]
    elif choice == "up":
        if placed_ladder:
            up_room()
            pass
    
    elif choice == "key":
        if "key" in inventory and not inserted_key:
            print("You insert the key into the trapdoor")
            inserted_key = True
            del inventory[inventory.index("key")]
    elif choice == "down":
        if inserted_key:
            down_room()
            pass
    
    elif choice == "backwards":
        if "map" in inventory and "sword" not in inventory:
            print("Suddenly a door appeared behind you and you went in, there was a sword, but nothing else, so you leave")
            inventory.append("sword")
    
    else:
        print("You dont think that will do anything useful")
    
    main_room()


def right_room():
    global inventory, killed_goblins, inserted_key_card
    if not killed_goblins:
        print("You find yourself in a long hallway, there are goblins blocking the way to a door on the other side. What do you do? (Type 'help' if you need help)")
    else:
        print("You find yourself in a long hallway, there is a door on the otherside. What do you do? (Type 'help' if you need help)")
    choice = input().lower()
    
    if choice == "help":
        help()
    elif choice == "inventory":
        items()
    
    elif choice == "backwards":
        main_room()
    
    elif choice == "sword":
        if "sword" in inventory and not killed_goblins:
            print("You kill the goblins with the sword")
            killed_goblins = True
    elif choice == "forwards":
        if killed_goblins:
            print("You go to the door on the other side and find a key, there is nothing else, so you leave")
            inventory.append("key")
        else:
            print("You already went in there")
    
    else:
        print("You dont think that will do anything useful")
    
    right_room()


def up_room():
    global inventory
    print("You go up the ladder and find a room with one door in front of you. What do you do? (Type 'help' if you need help)")
    choice = input().lower()

    if choice == "forwards":
        if "map" not in inventory:
            print("You go into the room and find a map, which says that there is a secret room behind the first room")
            inventory.append("map")
    
    elif choice == "down":
        main_room()
    
    else:
        print("You dont think that will do anything useful")
    
    up_room()


def down_room():
    global finished_falling, legendary_python
    if not finished_falling:
        print("You open the trapdoor and fall down")
        time.sleep(1)
        print("And keep falling...")
        time.sleep(1)
        print("And falling...")
        time.sleep(1)
        print("And falling...")
        time.sleep(1)
    print("You finally finish falling and you see a door in front of you. What do you do? (Type 'help' if you need help)")
    finished_falling = True
    choice = input().lower()

    if choice == "forwards":
        print("You open the door and finally find the legendary python!")
        print(legendary_python)
        input("Press enter to quit")
        sys.exit()
        

    else:
        print("You dont think that will do anything useful")
    
    down_room()


def help():
    print("You can type directions, 'up', 'down', 'left', 'right', 'forwards', 'backwards', an item's name, or 'inventory'")


def items():
    print(inventory)

inventory = ["key"]
placed_ladder = False
inserted_key = False
killed_goblins = False
inserted_key_card = False
unlocked_door = False
finished_falling = False
legendary_python = """
                 .:-==+++++==-:                   
              .-=+++++++++++++++-.                
             .=++++++++++++++++++=.               
             =+=---=++++++++++++++=.              
            .++=.  -++++++++++++++*:              
            :++-   :++++++++++++++*-              
            :++-   :+++++++++++++**=              
            :++=:.:=+++++++++++++**=              
            :++++=++++++++++++++***=              
            :++++++++++++++++++****=              
            :=====++++++++++++*****=              
                        +++++******=              
     .:-----------------++++*******=              
   .-=++++++++++++++++++++++*******= ........     
  .=+++++++++++++++++++++++********= .........    
  =+++++++++++++++++++++++*********= .........    
 :++++++++++++++++++++++***********= ..........   
 =+++++++++++++++++++++************= ..........   
.++++++++++++++++++++++************- ..........   
:+++++++++++++++++++++*************: ...........  
-++++++++++++++++++++*************=. ...........  
=++++++++++++++++++++************+. ............  
=++++++++++++++++++++++++******+=. .............  
++++++++++++++++-:::::::::::--:.  ..............  
++++++++++++++:                 ................  
=++++++++++++:  ................................  
=+++++++++++:  .................................  
-++++++++++=  ..................................  
:++++++++++. ...................................  
.++++++++++  ...................................  
 =+++++++++  ..................................   
 -+++++++++  ..................................   
  +++++++++  .................................    
  :++++++++  .................................    
   :+++++*+  ................................     
    .-=====  ...............................      
             ...........                          
             .......................              
             .......................              
             .......................              
             ................   ....              
             ................    ...              
             ................    ...              
             ................   ..:               
              .....................               
               ...................                
                .................                 
                   ...........                                                                                                                                                                                                                      
"""

if __name__ == "__main__":
    main_room()