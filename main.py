from display.shaw_main_menu import shaw_main_menu
from display.display_rooms import display_all_rooms

def main():
    status_loop = True
    while status_loop:
        display_all_rooms("./db/rooms.json")
        break

if __name__ == "__main__":
    main()
