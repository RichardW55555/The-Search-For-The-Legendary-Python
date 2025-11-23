def main_room():
    print("You find yourself in a dark room, you see four ways to go, a door on the left, a door on the right, a hole on the ceiling, and a trapdoor in the ground. What do you do? (Type 'help' if you need help)")
    choice = input().lower()
    
    if choice == "help":
        help()
        main_room()
    elif choice == "inventory":
        items()
        main_room()
    
    elif choice == "left":
        if "ladder" not in inventory:
            print("You go left and find a ladder, there is nothing else of interest, so you go back")
            inventory.append("ladder")
            main_room()
        else:
            print("You already went in there")
            main_room()
    
    elif choice == "right":
        #right_room()
        pass

    elif choice == "ladder":
        if "ladder" in inventory:
            print("You placed the ladder underneath the hole in the ceiling")
            placed_ladder = True
            del inventory[inventory.index("ladder")]
        else:
            main_room()
    elif choice == "up":
        if placed_ladder:
            #up_room()
            pass
        else:
            main_room()
    
    elif choice == "key":
        if "key" in inventory:
            print("You insert the key into the trapdoor")
            inserted_key = True
            del inventory[inventory.index("key")]
        else:
            main_room()
    elif choice == "down":
        if inserted_key:
            #down_room()
            pass
        else:
            main_room()
    
    else:
        print("You dont think that will do anything useful")
        main_room()


def right_room():
    pass


def up_room():
    pass


def down_room():
    pass


def help():
    print("You can type directions, 'up', 'down', 'left', 'right', 'forwards', 'backwards', an item's name, or 'inventory'")


def items():
    print(inventory)

global inventory
global placed_ladder
global inserted_key
inventory = []
placed_ladder = False
inserted_key = False

main_room()