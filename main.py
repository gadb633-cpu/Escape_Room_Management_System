from display.shaw_main_menu import shaw_main_menu
from display.display_all_rooms import display_all_rooms
from display.display_room import display_room

def main():
    status_loop = True
    while status_loop:
        # display_all_rooms("./db/rooms.json")
        display_room("R004","./db/rooms.json")
        break

if __name__ == "__main__":
    main()
