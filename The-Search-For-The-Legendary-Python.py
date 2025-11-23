def main_room():
    global inventory
    inventory = []
    print("You find yourself in a dark room, you see four ways to go, a door on the left, a door on the right, a hole on the ceiling, and a trapdoor in the ground. What do you do? (Type 'help' if you need help)")
    choice = input().lower()
    if choice == "help":
        help()
    elif choice == "inventory":
        items()
    elif choice == "left":
        if "ladder" not in inventory:
            print("You go left and find a ladder, there is nothing else of interest, so you go back")
            inventory.append("ladder")
            main_room()
        else:
            print("You already went in there")
            main_room()
    

def help():
    print("You can type directions, 'up', 'down', 'left', 'right', 'forwards', 'backwards', an item's name, or 'inventory'")

def items():
    print(inventory)

main_room()