from display.shaw_main_menu import shaw_main_menu
from display.shaw_rooms_menu import shaw_rooms_menu
from display.display_all_rooms import display_all_rooms
from display.display_room import display_room,get_id_to_search
from Helper_functions_and_validations.inputs import get_num,get_str
from Logic_Escape_Room.add_room import add_room
def Room_Management():
    status_loop = True
    while status_loop:
        shaw_rooms_menu()
        choice = get_num("enter your choice")
        match choice:
            case 1:
                display_all_rooms("./db/rooms.json")
            case 2:
                display_room(get_id_to_search(),"./db/rooms.json")
            case 3:
                add_room("./db/rooms.json")
            case 4:
                pass
            case 5:
                pass
            case 6:
                status_loop = False
            case _:
                print("choice only between 1-6") 