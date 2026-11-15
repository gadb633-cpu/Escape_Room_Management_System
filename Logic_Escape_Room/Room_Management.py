from display.shaw_main_menu import shaw_main_menu
from display.shaw_rooms_menu import shaw_rooms_menu
from display.display_all_items import display_all_items
from display.display_item import display_item
from Helper_functions_and_validations.inputs import get_num,get_str
from Logic_Escape_Room.add_room import add_room
from Logic_Escape_Room.update_room import update_room,update_is_active

def Room_Management():
    status_loop = True
    while status_loop:
        shaw_rooms_menu()
        choice = get_num("enter your choice")
        match choice:
            case 1:
                display_all_items("./db/rooms.json")
            case 2:
                display_item("room_id","./db/rooms.json")
            case 3:
                print(add_room("./db/rooms.json"))
            case 4:
                print(update_room("./db/rooms.json"))
            case 5:
                print(update_is_active("./db/rooms.json"))
            case 6:
                status_loop = False
            case _:
                print("choice only between 1-6")