from display.shaw_main_menu import shaw_main_menu
from Logic_Escape_Room.Room_Management import Room_Management
from Helper_functions_and_validations.inputs import get_num
def main():
    status_loop = True
    while status_loop:
        shaw_main_menu()
        choice = get_num("enter your choice (1-4)")
        match choice:
            case 1:
                Room_Management()
            case 2:
                pass
            case 3:
                pass
            case 4:
                status_loop = False  
            case _:
                print("choice only between 1-4")       

if __name__ == "__main__":
    main()