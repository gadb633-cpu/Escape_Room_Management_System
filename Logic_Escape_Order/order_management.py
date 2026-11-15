from display.shaw_orders_menu import shaw_orders_menu
from Helper_functions_and_validations.inputs import get_num,get_str
from display.display_all_orders  import display_all_orders
def order_management():
    status_loop = True
    while status_loop:
        shaw_orders_menu()
        choice = get_num("enter your choice")
        match choice:
            case 1:
                pass
            case 2:
                display_all_orders("./db/bookings.json")
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                status_loop = False    
            case _:
                print("choice only between 1-8")